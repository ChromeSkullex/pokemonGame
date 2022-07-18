$(document).ready(function(){
    $.ajax({
        url: '../PHP/db_config.php',
        async: false,
        success(e) {
            console.log(e);
        }
    })
});

