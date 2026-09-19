// Variable con el token
const csrfToken = document.cookie
  .split(";")
  .find((c) => c.trim().startsWith("csrftoken="))
  ?.split("=")[1];
axios.defaults.headers.common["X-CSRFToken"] = csrfToken;
// url del endpoint principal
// const url = "/business-gestion/pluviometer/";
const url = "/business-gestion/pluviometer/";
function getDayOfWeek(date) {
    // Crear un objeto Date si la entrada es una cadena
    const dateObj = typeof date === 'string' ? new Date(date) : date;

    // Asegurarse de que la fecha es válida
    if (isNaN(dateObj)) {
        throw new Error('Fecha inválida');
    }

    // Array con los nombres de los días de la semana
    const daysOfWeek = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];

    // Obtener el índice del día de la semana (0-6)
    const dayIndex = (dateObj.getUTCDay() + 7) % 7; // Usar getUTCDay para evitar problemas de zona horaria

    // Retornar el nombre del día correspondiente
    return daysOfWeek[dayIndex];
}


$(document).ready(function () {
       let pluviometerChart = new Chart(document.getElementById('pluviometerChart'), {
        type: 'bar', // Tipo de gráfica (puede ser 'line', 'bar', etc.)
        data: {
            labels: [], // Etiquetas de los días
            datasets: [{
                label: 'Precipitaciones Diarias',
                data: [], // Datos
                backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 99, 132, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)',
                        'rgba(255, 99, 132, 1)'
                    ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

        axios.get(url, {})
        .then(response => {
            // Procesar las ganancias por día
            const pluviometer_info = response.data.result; // Asumiendo que la respuesta es un array de objetos con ganancias por día

           
            // Limpiar datos anteriores
            pluviometerChart.data.labels = [];
            pluviometerChart.data.datasets[0].data = [];

            // Llenar datos de la gráfica
            pluviometer_info.forEach(day => {
                pluviometerChart.data.labels.push(getDayOfWeek(day.frequency)); // Asegúrate de que 'date' es la propiedad correcta
                pluviometerChart.data.datasets[0].data.push(day.total); // Asegúrate de que 'total' es la propiedad correcta
            });

            // Actualizar la gráfica
            pluviometerChart.update();
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});



