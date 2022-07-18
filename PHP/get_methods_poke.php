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

if(isset($_GET['get_img'])){
    echo get_img($_GET['get_img'], $link);

}

function get_img($poke_id, $link){
    $sql = "SELECT * FROM poke_stat WHERE id_name='$poke_id'";
    $result = mysqli_query($link, $sql);
    if (!$result){
        echo "NULL";
    }else{
        $row = $result->fetch_assoc();
        return $row['img_link'];
    }

}