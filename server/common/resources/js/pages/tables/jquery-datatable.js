$(function () {

      $('.js-expor').DataTable({
        pageLength: 100,
        dom: 'Bfrtip',
        buttons: [
                {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: [ 0, 1, 2,3,4]
                }},
                {
                extend: 'excel',
                exportOptions: {
                    columns: [ 0, 1, 2,3,4]
                }
            }
        ]
    });

    $('.js-basic-example').DataTable({
        language:{
            "sProcessing":     "Procesando...",
	"sLengthMenu":     "Mostrar _MENU_ registros.",
	"sZeroRecords":    "No se encontraron resultados.",
	"sEmptyTable":     "Ningún dato disponible en esta tabla.",
	"sInfo":           "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros.",
	"sInfoEmpty":      "Mostrando registros del 0 al 0 de un total de 0 registros.",
	"sInfoFiltered":   "(filtrado de un total de _MAX_ registros).",
	"sInfoPostFix":    "",
	"sSearch":         "Buscar:",
	"sUrl":            "",
	"sInfoThousands":  ",",
	"sLoadingRecords": "Cargando...",
	"oPaginate": {
		"sFirst":    "Primero",
		"sLast":     "Último",
		"sNext":     "Siguiente",
		"sPrevious": "Anterior"
	},
	"oAria": {
		"sSortAscending":  ": Activar para ordenar la columna de manera ascendente.",
		"sSortDescending": ": Activar para ordenar la columna de manera descendente."
	}
        }
    });

    //Exportable table
     $('.js-exportable').DataTable({
        dom: 'Bfrtip',
        pageLength: 100,
        buttons: [
                {
                extend: 'pdfHtml5',
                exportOptions: {
                    columns: [ 0, 1, 2,3,4]
                }},
                {
                extend: 'excel',
                exportOptions: {
                    columns: [ 0, 1, 2,3,4]
                }
            }
        ]
    });
});