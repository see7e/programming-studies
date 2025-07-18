// datatable *******************************************
window.addEventListener('DOMContentLoaded', event => {
    // Simple-DataTables
    // https://github.com/fiduswriter/Simple-DataTables/wiki

    const datatablesSimple = document.getElementById('datatablesSimple');
    if (datatablesSimple) {
        new simpleDatatables.DataTable(datatablesSimple);
    }
    // htmx datatable
    const htmxDataTable = document.getElementById('htmxDataTable');
    if (htmxDataTable) {
        document.addEventListener('htmx:afterSwap', function() {
            let dataTable = new simpleDatatables.DataTable(htmxDataTable);
        });
    }
});
