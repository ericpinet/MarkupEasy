
// On create project
$('#btn-create-project').on('click', function(event) {
    window.location.href = "?projects_page=add";
});

// Add project
$('#btn-add').on('click', function(event) {
    event.preventDefault();
    window.location.href = "?projects_page=add";
});

// Cancel add
$('#btn-cancel-add').on('click', function(event) {
    event.preventDefault();
    window.location.href = "?projects_page=";
});

// Submit post on submit
$('#project-form').on('submit', function(event) {
    event.preventDefault();
    save_project();
});

// Delete project
$('.btn-delete').on('click', function(e){

    var $row = $(this).parent('tr');
    var $td = $(this);

    $('#confirm-delete').modal({ backdrop: 'static', keyboard: false })
        .one('click', '#btn-confirm-delete', function() {

            delete_project($row.attr('id'));

            $row.addClass("danger");
            $row.fadeOut(150, function(){
                $td.remove();
            });

        });

});

// Delete project
/*$(".btn-delete").on("click", function(){

});
*/

// AJAX for posting
function save_project() {
    $.ajax({
        url : "/api/projects/", // the endpoint
        type : "POST", // http method
        data : {    name: $('#project-name').val(),
                    creation_date: get_date(),
                    user: '/api/users/'+$('#user-id').val()+'/'
               }, // data sent with the post request

        // handle a successful response
        success : function(json) {

            window.location.href = "?projects_page=";
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {

            $('#project-results').html('<div class="alert alert-danger" id="alert-danger"><small>Error: ' + xhr.status + '. Save data failed!</small></div>');
            $("#alert-danger").fadeTo(2000, 500).slideUp(500, function(){
                $("#alert-danger").slideUp(500);
            });

        }
    });
};

// AJAX for posting
function delete_project( project_id ) {
    $.ajax({
        url : "/api/projects/"+project_id+"/", // the endpoint
        type : "DELETE", // http method
        data : {
               }, // data sent with the post request

        // handle a successful response
        success : function(json) {

            window.location.href = "?projects_page=";
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {

            $('#project-results').html('<div class="alert alert-danger" id="alert-danger"><small>Error: ' + xhr.status + '. Save data failed!</small></div>');
            $("#alert-danger").fadeTo(2000, 500).slideUp(500, function(){
                $("#alert-danger").slideUp(500);
            });

        }
    });
};

function get_date() {
    return '2016-11-11 11:11'
}