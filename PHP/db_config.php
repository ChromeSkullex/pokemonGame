<?php

    $server='localhost';
    $username = 'root';
    $password = '';
    $db_name = 'pokemon_game';
    try {
        // Create database if it hasn't been created, saved locally
        try{

            $link = new PDO("mysql:host=$server", $username, $password);
            $link->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Creating Database and table, initilizing
            $db_name = "`".str_replace("`","``",$db_name)."`";
            $link->query("CREATE DATABASE IF NOT EXISTS $db_name");
            $link->query("use $db_name");
            /*
            $sql = "CREATE TABLE IF NOT EXISTS poke_stat(
            id INT NOT NULL PRIMARY KEY NOT NULL,
            id_name VARCHAR(20),
            display_name VARCHAR(20),
            type_name JSON,
            allowed_moveset JSON,
            efficiency JSON,
            base_stat JSON
        
            )";*/
            $sql = file_get_contents("db_ini.sql");
        if ($link->exec($sql)){
            echo "error";
        }else {
            echo "Created";
        }
        }
        catch (PDOException $e){

        }    } catch(PDOException $e){
        echo "Connection Failed 404: ". $e->getMessage();
    }