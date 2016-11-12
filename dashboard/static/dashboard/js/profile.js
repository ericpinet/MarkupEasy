
// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// Submit post on submit
$('#perso-form').on('submit', function(event) {
    event.preventDefault();
    create_post();
});

// AJAX for posting
function create_post() {
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

