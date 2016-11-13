
// Submit post on submit
$('#perso-form').on('submit', function(event) {
    event.preventDefault();
    save_personal_information();
});

// AJAX for posting
function save_personal_information() {
    $.ajax({
        url : "/api/users/"+$('#user-id').val()+"/", // the endpoint
        type : "PUT", // http method
        data : {    first_name: $('#first-name').val(),
                    last_name: $('#last-name').val(),
                    email: $('#email').val()
               }, // data sent with the post request

        // handle a successful response
        success : function(json) {

            $('#perso-results').html('<div class="alert alert-success" id="alert-success"><small>Save successful!</small></div>');
            $("#alert-success").fadeTo(2000, 500).slideUp(500, function(){
                $("#alert-success").slideUp(500);
            });

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {

            $('#perso-results').html('<div class="alert alert-danger" id="alert-danger"><small>Error: ' + xhr.status + '. Save data failed!</small></div>');
            $("#alert-danger").fadeTo(2000, 500).slideUp(500, function(){
                $("#alert-danger").slideUp(500);
            });

        }
    });
};

