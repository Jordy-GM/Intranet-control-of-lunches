// Datos de ejemplo (puedes reemplazarlos con tus datos dinámicos)
const selectionsByDayData = {
    labels: ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"],
    datasets: [{
        label: "Selecciones",
        data: [120, 150, 180, 90, 200],
        backgroundColor: "#007aff",
        borderColor: "#005bb5",
        borderWidth: 1,
    }]
};

const selectionsByMonthData = {
    labels: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    datasets: [{
        label: "Selecciones por Mes",
        data: [100, 200, 150, 300, 250, 400, 350, 450, 500, 600, 550, 700],
        backgroundColor: "#ff6384",
        borderColor: "#cc3255",
        borderWidth: 1,
    }]
};

const selectionsByDepartmentData = {
    labels: ["Ventas", "Marketing", "TI", "Recursos Humanos"],
    datasets: [{
        label: "Selecciones",
        data: [300, 150, 200, 100],
        backgroundColor: ["#007aff", "#34c759", "#ff9500", "#ff3b30"],
        borderWidth: 1,
    }]
};

// Configuración común para los gráficos
const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: "bottom",
        },
    },
};

// Gráfico de barras para Selecciones por Día
const selectionsByDayChart = new Chart(document.getElementById("selectionsByDayChart"), {
    type: "bar",
    data: selectionsByDayData,
    options: chartOptions,
});

// Renderizar gráfico de selecciones por mes
const ctxMonth = document.getElementById('selectionsByMonthChart').getContext('2d');
new Chart(ctxMonth, {
    type: 'bar',
    data: selectionsByMonthData,
    options: chartOptions,
});

// Gráfico de dona para Selecciones por Departamento
const selectionsByDepartmentChart = new Chart(document.getElementById("selectionsByDepartmentChart"), {
    type: "doughnut",
    data: selectionsByDepartmentData,
    options: chartOptions,
});

// Hacer los gráficos desplegables
document.querySelectorAll('.section h2').forEach(header => {
    header.addEventListener('click', () => {
        const card = header.nextElementSibling;
        card.style.display = card.style.display === 'none' ? 'block' : 'none';
    });
});