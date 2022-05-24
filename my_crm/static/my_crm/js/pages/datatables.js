$(document).ready(function() {

    "use strict";

    $('#datatable1').DataTable();

    $('#datatable2').DataTable({ 
        "scrollY": "300px",
        "scrollCollapse": true,
        "paging": false
    });

    var table = $('#datatable3').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.11.4/i18n/ru.json'
        },
		scrollX: true,
        dom: 'Bfrtip',
        buttons: ['excel', 'copy', 'pdf', 'print'],
    });

    $('#datatable4 tfoot th').each( function () {
        var title = $(this).text();
        $(this).html( '<input type="text" class="form-control" placeholder="Search '+title+'" />' );
    } );
 
    // DataTable
    $('#datatable4').DataTable({
        initComplete: function () {
            // Apply the search
            this.api().columns().every( function () {
                var that = this;
 
                $( 'input', this.footer() ).on( 'keyup change clear', function () {
                    if ( that.search() !== this.value ) {
                        that
                            .search( this.value )
                            .draw();
                    }
                } );
            } );
        }
    });

    var table = $('#datatable5').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/1.11.4/i18n/ru.json'
        },
        dom: 'Bfrtip',
        buttons: ['excel', 'copy', 'pdf', 'print'],
    });
});