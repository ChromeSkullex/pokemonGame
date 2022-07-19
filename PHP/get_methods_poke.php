<?php
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'root');
define('DB_PASSWORD','');
define('DB_NAME', 'pokemon_game');

$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME );

if ($link === false){
    echo "Could not connect";
    die ("could not connect". mysqli_connect_error());
}

if(isset($_GET['get_all_data'])){
    echo get_all_data($_GET['get_all_data'], $link);

}
else if(isset($_GET['get_all_move'])){
    echo $_GET['get_all_move'];
    echo get_all_move($_GET['get_all_move'], $link);

}

function get_all_move($id_name, $link){
    $sql = "SELECT * FROM moveset WHERE id_name='$id_name'";
    $result = mysqli_query($link, $sql);
    if (!$result){
        echo "NULL";
    }else{
        $row = $result->fetch_assoc();
        $json_move = new stdClass();
        $json_move->id = $row['id'];
        $json_move->id_name = $row['id_name'];
        $json_move->title = $row['title'];
        $json_move->type = $row['type'];
        $json_move->cat = $row['cat'];
        $json_move->stats = $row['stats'];
        $json_move->effect = $row['effect'];

        return json_encode($json_move,JSON_UNESCAPED_SLASHES);
    }
}

function get_all_data($id_num, $link){

    $sql = "SELECT * FROM poke_stat WHERE id='$id_num'";
    $result = mysqli_query($link, $sql);
    if (!$result){
        echo "NULL";
    }else{

        $row = $result->fetch_assoc();
        // Create a json for everything
        $json_poke = new stdClass();
        $json_poke->id = $row['id'];
        $json_poke->display_name = $row['display_name'];
        $json_poke->img_link = $row['img_link'];
        $json_poke->type_name = $row['type_name'];
        $json_poke->allowed_moveset = $row['allowed_moveset'];
        $json_poke->efficiency = $row['efficiency'];
        $json_poke->base_stat = $row['base_stat'];

        $json_return = json_encode($json_poke, JSON_UNESCAPED_SLASHES );

        return $json_return;
    }
}