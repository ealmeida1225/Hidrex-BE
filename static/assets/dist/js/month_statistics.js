// Variable con el token
const csrfToken = document.cookie
  .split(";")
  .find((c) => c.trim().startsWith("csrftoken="))
  ?.split("=")[1];
axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
// url del endpoint principal
const url = "/business-gestion/month-statistics/";

$(function () {
  bsCustomFileInput.init();
  poblarListas()
});

$(document).ready(function () {
  $("table")
    .addClass("table table-hover")
    .DataTable({
      dom: '<"top"l>Bfrtip',
      buttons: [
        {
          text: "Crear",
          className: " btn btn-primary btn-info",
          action: function (e, dt, node, config) {
            $("#modal-create-diary-precipitation-classification").modal("show");
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
      //Adding server-side processing
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
        { data: "year_name", title: "Pluviómetro (Año)" },
        { data: "month", title: "Mes" },
        {
          data: "max_registered_value",
          title: "Mayor valor registrado",
        },
          { data: "total_precipit", title: "Total de precipitaciones" },
          { data: "variance", title: "Varianza" },
          { data: "standard_deviation", title: "Desviación estándar" },
          { data: "rainy_streak_med_long", title: "Long media de rachas lluviosas" },
          { data: "rainy_streak_count", title: "Cantidad de rachas lluviosas" },
          { data: "rainy_days_count", title: "Cantidad de días lluviosos" },
          { data: "daily_mean", title: "Media diaria" },


        {
          data: "",
          title: "Acciones",
          render: (data, type, row) => {
            return `<div class="btn-group">
                        <button type="button" title="edit" class="btn bg-olive active" data-toggle="modal" data-target="#modal-create-diary-precipitation-classification" data-id="${row.id}" data-type="edit" data-name="${row.name}" id="${row.id}"  >
                          <i class="fas fa-edit"></i>
                        </button>  
                        <button type="button" title="delete" class="btn bg-olive" onclick="function_delete('${row.id}','${row.name}')" >
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

$("#modal-create-diary-precipitation-classification").on("hide.bs.modal", (event) => {
  // The form element is selected from the event trigger and its value is reset.
  const form = event.currentTarget.querySelector("form");
  form.reset();
  // The 'edit_brands' flag is set to false.
  edit_element = false;
  // An array 'elements' is created containing all the HTML elements found inside the form element.
  const elements = [...form.elements];
  // A forEach loop is used to iterate through each element in the array.
  elements.forEach((elem) => elem.classList.remove("is-invalid"));
});

let edit_element = false;
$("#modal-create-diary-precipitation-classification").on("show.bs.modal", function (event) {
  var button = $(event.relatedTarget); // Button that triggered the modal

  var modal = $(this);
  if (button.data("type") == "edit") {
    var dataName = button.data("name"); // Extract info from data-* attributes
    selected_id = button.data("id"); // Extract info from data-* attributes
    edit_element = true;

    modal.find(".modal-title").text("Editar " + dataName);

    // Realizar la petición con Axios
    axios
      .get(`${url}` + selected_id + "/")
      .then(function (response) {
        // Recibir la respuesta
        const element = response.data;
        form.elements.daily_mean.value = element.daily_mean;
        form.elements.rainy_days_count.value = element.rainy_days_count;
        form.elements.rainy_streak_count.value = element.rainy_streak_count;
        form.elements.rainy_streak_med_long.value = element.rainy_streak_med_long;
        form.elements.standard_deviation.value = element.standard_deviation;
        form.elements.total_precipit.value = element.total_precipit;
        form.elements.variance.value = element.variance;
        form.elements.year.value = element.year;
        form.elements.month.value = element.month;
        form.elements.max_registered_value.value = element.max_registered_value;
      })
      .catch(function (error) {});
  } else {
    modal.find(".modal-title").text("Crear...");
  }
});

// form validator
$(function () {
  $.validator.setDefaults({
    language: "es",
    submitHandler: function () {
      // alert("Form successful submitted!");
    },
  });

  $("#form-create-diary-precipitation-classification").validate({
    rules: {
      name: {
        required: true,
      },
    },
    submitHandler: function (form) {},

    messages: {},
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



let form = document.getElementById("form-create-diary-precipitation-classification");
form.addEventListener("submit", function (event) {
  event.preventDefault();
  var table = $("#tabla-de-Datos").DataTable();
  const csrfToken = document.cookie
    .split(";")
    .find((c) => c.trim().startsWith("csrftoken="))
    ?.split("=")[1];
  axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
  let data = new FormData();
  data.append("variance", document.getElementById("variance").value);
  data.append("daily_mean", document.getElementById("daily_mean").value);
  data.append("rainy_days_count", document.getElementById("rainy_days_count").value);
  data.append("rainy_streak_count", document.getElementById("rainy_streak_count").value);
  data.append("rainy_streak_med_long", document.getElementById("rainy_streak_med_long").value);
  data.append("year", document.getElementById("year").value);
  data.append("rainy_streak_med_long", document.getElementById("rainy_streak_med_long").value);
  data.append("month", document.getElementById("month").value);
  data.append("standard_deviation", document.getElementById("standard_deviation").value);
  data.append("max_registered_value", document.getElementById("max_registered_value").value);
  data.append("total_precipit", document.getElementById("total_precipit").value);

  if (edit_element) {
    axios
      .patch(`${url}` + selected_id + "/", data)
      .then((response) => {
        if (response.status === 200) {
          $("#modal-create-diary-precipitation-classification").modal("hide");
          Swal.fire({
            icon: "success",
            title: "Clasificación actualizada con éxito  ",
            showConfirmButton: false,
            timer: 1500,
          });
          table.ajax.reload();

          edit_element = false;
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
          title: "Error al crear clasificación",
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
            title: "Clasificación creada con éxito",
            showConfirmButton: false,
            timer: 1500,
          });
          table.ajax.reload();
          $("#modal-create-diary-precipitation-classification").modal("hide");
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
          title: "Error al crear clasificación",
          text: textError,
          showConfirmButton: false,
          timer: 1500,
        });
      });
  }
});

function poblarListas() {
  // Poblar la lista de tiendas
  var $year_statistic = document.getElementById("year");
  axios.get("/business-gestion/year-statistics/").then(function (response) {
    response.data.results.forEach(function (element) {
      var option = new Option(element.__str__, element.id);
      $year_statistic.add(option);
    });
  });
}

function function_delete(id, name) {
  const table = $("#tabla-de-Datos").DataTable();
  Swal.fire({
    title: "Eliminar",
    text: `Esta seguro que desea eliminar el elemento ${name}?`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Si, Eliminar",
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
              text: "Elemento eliminado satisfactoriamente ",
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
