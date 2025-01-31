document.addEventListener('DOMContentLoaded', () => {
    const toggleButtons = document.querySelectorAll('.toggle-button');

    toggleButtons.forEach(button => {
        button.addEventListener('click', () => {
            const user = button.dataset.user; // Capturar el usuario
            const rows = document.querySelectorAll(`.user-${user}`); // Seleccionar las filas relacionadas

            rows.forEach(row => {
                // Alternar clase para mostrar u ocultar
                if (row.style.display === 'none' || row.style.display === '') {
                    row.style.display = 'table-row'; // Mostrar las filas como parte de la tabla
                } else {
                    row.style.display = 'none'; // Ocultar filas
                }
            });
        });
    });
});


