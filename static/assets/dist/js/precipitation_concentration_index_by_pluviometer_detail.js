// Variable con el token
const csrfToken = document.cookie
  .split(";")
  .find((c) => c.trim().startsWith("csrftoken="))
  ?.split("=")[1];
axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
// url del endpoint principal
const url = `/business-gestion/precipitation-concentration-index-by-pluviometer/`;
console.log(url)
$(function () {
  bsCustomFileInput.init();
});



let form = document.getElementById("precipitation-concentration-index-by-pluviometer-detail");

// Realizar la petición con Axios
axios
  .get(`${url}${pluviometer_id}/`)
  .then(function (response) {
    // Recibir la respuesta
    const selected_element = response.data;
    document.getElementById("pluviometer").value = selected_element.pluviometer_name;
    document.getElementById("years_considered").value = selected_element.years_considered;
    document.getElementById("a_value").value = selected_element.a_value;
    document.getElementById("b_value").value = selected_element.b_value;
    document.getElementById("r_2_value").value = selected_element.r_2_value;
    document.getElementById("ci_value").value = selected_element.ci_value;
    document.getElementById("rainy_days").value = selected_element.rainy_days;
    document.getElementById("max_rain_value").value = selected_element.max_rain_value + 'mm';
    document.getElementById("rainy_days_percent").value = selected_element.rainy_days_percent + '%';
    document.getElementById("rain_by_period_avg").value = selected_element.rain_by_period_avg;
    document.getElementById("rainy_days_by_period_avg").value = selected_element.rainy_days_by_period_avg;
    document.getElementById("total_rain_value").value = selected_element.total_rain_value;
  })
  .catch((error) => {
    alert(error);
  });


// crear Modelo


