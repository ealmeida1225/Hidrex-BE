// Variable con el token
const csrfToken = document.cookie
  .split(";")
  .find((c) => c.trim().startsWith("csrftoken="))
  ?.split("=")[1];
axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
// url del endpoint principal
const url = "/business-gestion/area/";

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
          className: " btn btn-primary btn-info",
          action: function (e, dt, node, config) {
            $("#modal-create-area").modal("show");
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
        { data: "name", title: "Nombre" },
        { data: "area_type_name", title: "Tipo" },
        { data: "sub_name", title: "Sub nombre" },
        { data: "centroid_lat", title: "Centroide (Latitud)" },
        { data: "centroid_lon", title: "Centroide (Longitud)" },
        { data: "description", title: "Descripción" },

        {
          data: "",
          title: "Acciones",
          render: (data, type, row) => {
            return `<div class="btn-group">
                        <button type="button" title="edit" class="btn bg-olive active" data-toggle="modal" data-target="#modal-create-area" data-id="${row.id}" data-type="edit" data-name="${row.name}" id="${row.id}"  >
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

$("#modal-create-area").on("hide.bs.modal", (event) => {
  const form = event.currentTarget.querySelector("form");
  form.reset();
  edit_area = false;
  const elements = [...form.elements];
  elements.forEach((elem) => elem.classList.remove("is-invalid"));
});

let edit_area = false;
$("#modal-create-area").on("show.bs.modal", function (event) {
  var button = $(event.relatedTarget); // Button that triggered the modal

  var modal = $(this);
  if (button.data("type") == "edit") {
    var dataName = button.data("name"); // Extract info from data-* attributes
    selected_id = button.data("id"); // Extract info from data-* attributes
    edit_area = true;

    modal.find(".modal-title").text("Editar " + dataName);

    // Realizar la petición con Axios
    axios
      .get(`${url}` + selected_id + "/")
      .then(function (response) {
        // Recibir la respuesta
        const selected_area = response.data;
        console.log(form.elements);

        form.elements.name.value = selected_area.name;
        form.elements.sub_name.value = selected_area.sub_name;
        form.elements.area_type.value = selected_area.area_type;
        form.elements.centroid_lat.value = selected_area.centroid_lat;
        form.elements.centroid_lon.value = selected_area.centroid_lon;
        form.elements.description.value = selected_area.description;

        // document.getElementById("selectbrands").select= models.brand;
      })
      .catch(function (error) {});
  } else {
    modal.find(".modal-title").text("Crear");
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

  $("#form-create-area").validate({
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

// crear Modelo

let form = document.getElementById("form-create-area");
form.addEventListener("submit", function (event) {
  event.preventDefault();
  var table = $("#tabla-de-Datos").DataTable();
  const csrfToken = document.cookie
    .split(";")
    .find((c) => c.trim().startsWith("csrftoken="))
    ?.split("=")[1];
  axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
  let data = new FormData();
  data.append("name", document.getElementById("name").value);
  data.append("sub_name", document.getElementById("sub_name").value);
  data.append("centroid_lat", document.getElementById("centroid_lat").value);
  data.append("centroid_lon", document.getElementById("centroid_lon").value);
  data.append("area_type", document.getElementById("area_type").value);
  data.append("description", document.getElementById("description").value);

  if (edit_area) {
    axios
      .patch(`${url}` + selected_id + "/", data)
      .then((response) => {
        if (response.status === 200) {
          $("#modal-create-area").modal("hide");
          Swal.fire({
            icon: "success",
            title: "Actualizado con éxito  ",
            showConfirmButton: false,
            timer: 1500,
          });
          table.ajax.reload();

          edit_area = false;
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
          title: "Error al crear",
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
            title: "Área creada con éxito",
            showConfirmButton: false,
            timer: 1500,
          });
          table.ajax.reload();
          $("#modal-create-area").modal("hide");
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
          title: "Error al crear",
          text: textError,
          showConfirmButton: false,
          timer: 1500,
        });
      });
  }
});

function poblarListas() {
  var $area_types = document.getElementById("area_type");
  axios.get("../../business-gestion/area-type/").then(function (response) {
    response.data.results.forEach(function (element) {
      var option = new Option(element.name, element.id);
      $area_types.add(option);
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
