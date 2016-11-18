

// On change picture

$('#btn-change-picture').on('click', function(event) {

    var win = window.open('https://www.gravatar.com/', '_blank');
    if (win) {
        //Browser has allowed it to be opened
        win.focus();
    } else {
        //Browser has blocked it
        alert('Please allow popups for this website');
    }

});


// On change email

$('#btn-change-email').on('click', function(event) {
    alert('Not implemented yet!');
});