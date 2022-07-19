function get_moveset(name_id){

    console.log(name_id);

    $.ajax({
        url: '../PHP/get_methods_poke.php',
        data: {"get_all_move":name_id},
        async: false,
        success(e){
            console.log(e)
        }
    });
}