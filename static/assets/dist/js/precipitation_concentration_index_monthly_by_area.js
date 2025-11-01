// Variable con el token
const csrfToken = document.cookie
  .split(";")
  .find((c) => c.trim().startsWith("csrftoken="))
  ?.split("=")[1];
axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
// url del endpoint principal
const url = "/business-gestion/precipitation-concentration-index-monthly-by-area/";

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
            $("#modal-create-precipitation-concentration-index-monthly-by-area").modal("show");
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
        { data: "area_name", title: "Área" },
        { data: "month", title: "Mes" },
        { data: "years_considered", title: "Años considerados" },
        { data: "a_value", title: "Valor de a" },
        { data: "b_value", title: "Valor de b" },
        { data: "r_2_value", title: "Valor de r^2" },
        { data: "ci_value", title: "Índice de concentración de precipitaciones" },
        { data: "rainy_days", title: "Total de días con lluvia" },
        { data: "max_rain_value", title: "Mayor lluvia registrada" },
        { data: "rainy_days_percent", title: "% de días lluviosos" },
        { data: "rain_by_period_avg", title: "mm promedio de lluvia diaria" },
        { data: "rainy_days_by_period_avg", title: "Cant. Prom. de días con lluvias" },
        { data: "total_rain_value", title: "Total de días lluviosos" },

        {
          data: "",
          title: "Acciones",
          render: (data, type, row) => {
            return `<div class="btn-group">
                        <button type="button" title="edit" class="btn bg-olive active" data-toggle="modal" data-target="#modal-create-precipitation-concentration-index-monthly-by-area" data-id="${row.id}" data-type="edit" data-name="${row.name}" id="${row.id}"  >
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

$("#modal-create-precipitation-concentration-index-monthly-by-area").on("hide.bs.modal", (event) => {
  const form = event.currentTarget.querySelector("form");
  form.reset();
  edit_element = false;
  const elements = [...form.elements];
  elements.forEach((elem) => elem.classList.remove("is-invalid"));
});

let edit_element = false;
$("#modal-create-precipitation-concentration-index-monthly-by-area").on("show.bs.modal", function (event) {
  var button = $(event.relatedTarget); // Button that triggered the modal

  var modal = $(this);
  if (button.data("type") == "edit") {
    selected_id = button.data("id"); // Extract info from data-* attributes
    edit_element = true;

    modal.find(".modal-title").text("Editar");

    // Realizar la petición con Axios
    axios
      .get(`${url}` + selected_id + "/")
      .then(function (response) {
        // Recibir la respuesta
        const selected_element = response.data;
        console.log(selected_element)
        form.elements.area.value = selected_element.area;
        form.elements.month.value = selected_element.month;
        form.elements.years_considered.value = selected_element.years_considered;
        form.elements.a_value.value = selected_element.a_value;
        form.elements.b_value.value = selected_element.b_value;
        form.elements.r_2_value.value = selected_element.r_2_value;
        form.elements.ci_value.value = selected_element.ci_value;
        form.elements.rainy_days.value = selected_element.rainy_days;
        form.elements.max_rain_value.value = selected_element.max_rain_value;
        form.elements.rainy_days_percent.value = selected_element.rainy_days_percent;
        form.elements.rain_by_period_avg.value = selected_element.rain_by_period_avg;
        form.elements.rainy_days_by_period_avg.value = selected_element.rainy_days_by_period_avg;
        form.elements.total_rain_value.value = selected_element.total_rain_value;

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

  $("#form-create-precipitation-concentration-index-monthly-by-area").validate({
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

let form = document.getElementById("form-create-precipitation-concentration-index-monthly-by-area");
form.addEventListener("submit", function (event) {
  event.preventDefault();
  var table = $("#tabla-de-Datos").DataTable();
  const csrfToken = document.cookie
    .split(";")
    .find((c) => c.trim().startsWith("csrftoken="))
    ?.split("=")[1];
  axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
  let data = new FormData();
  data.append("area", document.getElementById("area").value);
  data.append("month", document.getElementById("month").value);
  data.append("years_considered", document.getElementById("years_considered").value);
  data.append("a_value", document.getElementById("a_value").value);
  data.append("b_value", document.getElementById("b_value").value);
  data.append("r_2_value", document.getElementById("r_2_value").value);
  data.append("ci_value", document.getElementById("ci_value").value);
  data.append("rainy_days", document.getElementById("rainy_days").value);
  data.append("max_rain_value", document.getElementById("max_rain_value").value);
  data.append("rainy_days_percent", document.getElementById("rainy_days_percent").value);
  data.append("rain_by_period_avg", document.getElementById("rain_by_period_avg").value);
  data.append("rainy_days_by_period_avg", document.getElementById("rainy_days_by_period_avg").value);
  data.append("total_rain_value", document.getElementById("total_rain_value").value);

  if (edit_element) {
    axios
      .patch(`${url}` + selected_id + "/", data)
      .then((response) => {
        if (response.status === 200) {
          $("#modal-create-precipitation-concentration-index-monthly-by-area").modal("hide");
          Swal.fire({
            icon: "success",
            title: "Actualizado con éxito  ",
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
            title: "Pluviómetro creado con éxito",
            showConfirmButton: false,
            timer: 1500,
          });
          table.ajax.reload();
          $("#modal-create-precipitation-concentration-index-monthly-by-area").modal("hide");
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
  var $areas = document.getElementById("area");
  axios.get("../../business-gestion/area/").then(function (response) {
    response.data.results.forEach(function (element) {
      var option = new Option(element.__str__, element.id);
      $areas.add(option);
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
