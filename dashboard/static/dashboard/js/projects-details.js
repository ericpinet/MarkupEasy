
// Close project
$('#btn-close').on('click', function(event) {
    event.preventDefault();
    window.location.href = "/dashboard/";
});

// Upload file
$('#btn-import-file').on('click', function(event) {

    $('#upload-file').modal({ backdrop: 'static', keyboard: false })
        .one('click', '#btn-upload-file', function() {

            delete_file($row.attr('id'));

            $row.addClass("danger");
            $row.fadeOut(150, function(){
                $td.remove();
            });

        });
});


// Delete file
$('.btn-delete').on('click', function(e){

    var $row = $(this).parent('td').parent('tr');
    var $td = $(this);

    $('#confirm-delete-file').modal({ backdrop: 'static', keyboard: false })
        .one('click', '#btn-confirm-delete-file', function() {

            delete_file($row.attr('id'));

            $row.addClass("danger");
            $row.fadeOut(150, function(){
                $td.remove();
            });

        });
});


// AJAX for posting
function delete_file( file_id ) {
    $.ajax({
        url : "/api/files/"+file_id+"/", // the endpoint
        type : "DELETE", // http method
        data : {
               }, // data sent with the post request

        // handle a successful response
        success : function(json) {

            //window.location.href = "?projects_page=deleted";
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {

            $('#file-result').html('<div class="alert alert-danger" id="alert-danger"><small>Error: ' + xhr.status + '. Save data failed!</small></div>');
            $("#alert-danger").fadeTo(2000, 500).slideUp(500, function(){
                $("#alert-danger").slideUp(500);
            });
        }
    });
};