// Variable con el token
const csrfToken = document.cookie
  .split(";")
  .find((c) => c.trim().startsWith("csrftoken="))
  ?.split("=")[1];
axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
// url del endpoint principal
const url = "/business-gestion/register/";

$(function () {
  bsCustomFileInput.init();
  poblarListas();
});

$(document).ready(function () {
  $("table")
    .addClass("table table-hover")
    .DataTable({
      dom: '<"top"l>Bfrtip',
      buttons: [
        {
          text: "Crear",
          className: "btn btn-primary btn-info",
          action: function (e, dt, node, config) {
            $("#modal-create-registers").modal("show");
          },
        },
        {
          extend: "excel",
          text: "Excel",
        },
        {
          extend: "pdf",
          text: "PDF",
        },
        {
          extend: "print",
          text: "Print",
        },
      ],
      // Adding server-side processing
      serverSide: true,
      search: {
        return: true,
      },
      processing: true,
      ajax: function (data, callback, settings) {
        dir = "";

        if (data.order[0].dir == "desc") {
          dir = "-";
        }

        axios
          .get(`${url}`, {
            params: {
              page_size: data.length,
              page: data.start / data.length + 1,
              search: data.search.value,
              ordering: dir + data.columns[data.order[0].column].data,
            },
          })
          .then((res) => {
            callback({
              recordsTotal: res.data.count,
              recordsFiltered: res.data.count,
              data: res.data.results,
            });
          })
          .catch((error) => {
            alert(error);
          });
      },
      columns: [
        { data: "pluviometer_name", title: "Pluviómetro" },
        { data: "register_date", title: "Fecha" },
        { data: "rain_value", title: "Valor registrado" },
        {
          data: "",
          title: "Acciones",
          render: (data, type, row) => {
            return `<div class="btn-group">
                        <button type="button" title="edit" class="btn bg-olive active" data-toggle="modal" data-target="#modal-create-registers" data-id="${row.id}" data-type="edit" data-name="${row.pluviometer}" id="${row.id}">
                          <i class="fas fa-edit"></i>
                        </button>  
                        <button type="button" title="delete" class="btn bg-olive" onclick="function_delete('${row.id}','${row.product}')" >
                          <i class="fas fa-trash"></i>
                        </button>                                          
                      </div>`;
          },
        },
      ],
      //  esto es para truncar el texto de las celdas
      columnDefs: [],
    });
});

let selected_id;

$("#modal-create-registers").on("hide.bs.modal", (event) => {
  const form = event.currentTarget.querySelector("form");
  form.reset();
  edit_register = false;
  const elements = [...form.elements];
  elements.forEach((elem) => elem.classList.remove("is-invalid"));
});

let edit_register = false;
$("#modal-create-registers").on("show.bs.modal", function (event) {
  var button = $(event.relatedTarget); // Button that triggered the modal

  var modal = $(this);
  if (button.data("type") == "edit") {
    var dataName = button.data("name"); // Extract info from data-* attributes
    selected_id = button.data("id"); // Extract info from data-* attributes
    edit_register = true;

    modal.find(".modal-title").text("Editar Registro diario " + dataName);

    // Realizar la petición con Axios
    axios
      .get(`${url}` + selected_id + "/")
      .then(function (response) {
        // Recibir la respuesta
        const registry = response.data;
        form.elements.register_date.value = registry.register_date;
        form.elements.rain_value.value = registry.rain_value;
        form.elements.pluviometer.value = registry.pluviometer;
      })
      .catch(function (error) {});
  } else {
    modal.find(".modal-title").text("Crear Registro diario");
  }
});

// form validator
// form validator
$(function () {
  $.validator.setDefaults({
    language: "es",
    submitHandler: function () {
      // alert("Form successful submitted!");
    },
  });

  $("#form-create-register").validate({
    rules: {
      rain_value: {
        required: true,
        number: true, // Solo números
      },
      register_date: {
        required: true, // Campo no obligatorio
      },
      pluviometer: {
        required: true, // Campo no obligatorio
      },
    },
    messages: {
      rain_value: {
        required: "Este campo es obligatorio.",
        digits: "Por favor, introduzca solo números.",
      },
      register_date: {
        required: "Este campo es obligatorio.",
        number: "Por favor, introduzca un número válido.",
      },
      pluviometer: {
        required: "Este campo es obligatorio.",
        number: "Por favor, introduzca un número válido.",
      },
    },
    submitHandler: function (form) {},

    errorElement: "span",
    errorPlacement: function (error, element) {
      error.addClass("invalid-feedback");
      element.closest(".form-group").append(error);
    },
    highlight: function (element, errorClass, validClass) {
      $(element).addClass("is-invalid");
    },
    unhighlight: function (element, errorClass, validClass) {
      $(element).removeClass("is-invalid");
    },
  });
});

// crear Registro diario

let form = document.getElementById("form-create-register");
form.addEventListener("submit", function (event) {
  event.preventDefault();
  var table = $("#tabla-de-Datos").DataTable();
  const csrfToken = document.cookie
    .split(";")
    .find((c) => c.trim().startsWith("csrftoken="))
    ?.split("=")[1];
  axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
  let data = new FormData();
  data.append("pluviometer", document.getElementById("pluviometer").value);
  data.append("rain_value", document.getElementById("rain_value").value);
  data.append("register_date", document.getElementById("register_date").value);

  if (edit_register) {
    axios
      .patch(`${url}` + selected_id + "/", data)
      .then((response) => {
        if (response.status === 200) {
          $("#modal-create-registers").modal("hide");
          Swal.fire({
            icon: "success",
            title: "Registro diario actualizada con éxito",
            showConfirmButton: false,
            timer: 1500,
          });
          table.ajax.reload();

          edit_register = false;
        }
      })
      .catch((error) => {
        let dict = error.response.data;
        let textError = "Revise los siguientes campos: ";
        for (const key in dict) {
          textError = textError + ", " + key;
        }

        Swal.fire({
          icon: "error",
          title: "Error al crear la Registro diario",
          text: textError,
          showConfirmButton: false,
          timer: 1500,
        });
      });
  } else {
    axios
      .post(`${url}`, data)
      .then((response) => {
        if (response.status === 201) {
          Swal.fire({
            icon: "success",
            title: "Registro diario creada con éxito",
            showConfirmButton: false,
            timer: 1500,
          });
          table.ajax.reload();
          $("#modal-create-registers").modal("hide");
        }
      })
      .catch((error) => {
        let dict = error.response.data;
        let textError = "Revise los siguientes campos: ";
        for (const key in dict) {
          textError = textError + ", " + key;
        }

        Swal.fire({
          icon: "error",
          title: "Error al crear la Registro diario",
          text: textError,
          showConfirmButton: false,
          timer: 1500,
        });
      });
  }
});

function poblarListas() {
  // Poblar la lista de tiendas
  var $pluviometers = document.getElementById("pluviometer");
  axios.get("/business-gestion/pluviometer/").then(function (response) {
    response.data.results.forEach(function (element) {
      var option = new Option(element.__str__, element.id);
      $pluviometers.add(option);
    });
  });
}

function function_delete(id, name) {
  const table = $("#tabla-de-Datos").DataTable();
  Swal.fire({
    title: "Eliminar",
    text: `¿Está seguro que desea eliminar el elemento ${name}?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Sí, Eliminar",
  }).then((result) => {
    if (result.isConfirmed) {
      axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
      axios
        .delete(`${url}${id}/`)
        .then((response) => {
          if (response.status === 204) {
            table.row(`#${id}`).remove().draw();
            Swal.fire({
              icon: "success",
              title: "Eliminar Elemento",
              text: "Elemento eliminado satisfactoriamente",
              showConfirmButton: false,
              timer: 1500,
            });
          }
        })
        .catch((error) => {
          Swal.fire({
            icon: "error",
            title: "Error eliminando elemento",
            text: error.response.data.detail,
            showConfirmButton: false,
            timer: 3000,
          });
        });
    }
  });
}
