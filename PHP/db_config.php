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
            $sql = file_get_contents("db_ini.sql");
            // Once initialized, populate tables
            if ($link->exec($sql)){
                echo "Server Error: Database not Initialized correctly";
            }else {

                $json_obj = file_get_contents("../RAWDATA/pokemon.json");
                $json_poke = json_decode($json_obj, true);
                foreach ($json_poke as $key=> $poke_name){

                    $poke_name_id = $key;
                    //echo ($json_a[$poke_name_id]['title']);
                    $display_name = $json_poke[$poke_name_id]['title'];
                    $img_link = $json_poke[$poke_name_id]['img'];
                    $type_name =json_encode( $json_poke[$poke_name_id]['type']) ;
                    $allowed_moveset = json_encode($json_poke[$poke_name_id]['efficiency']);
                    $efficiency = json_encode($json_poke[$poke_name_id]['allowed_moves']);
                    $base_stat = json_encode($json_poke[$poke_name_id]['base_stat']);
                    echo "$display_name, $img_link    ";
                    $sql_find = "SELECT COUNT(*) FROM poke_stat WHERE id_name='".$poke_name_id. "'";
                    $result = $link->query($sql_find);
                    $num_find = $result->fetch();
                    print_r($num_find[0]);
                    if ($num_find[0] < 1){
                        $sql = "INSERT INTO poke_stat(id_name, display_name, img_link, type_name, allowed_moveset, efficiency, 
                      base_stat) VALUES ('$poke_name_id', '$display_name', '$img_link', '$type_name', '$allowed_moveset', '$efficiency', '$base_stat')";
                        $link->exec($sql);

                        echo "Created<p>";
                    }
                    echo "<p>";
                    /*
                    $sql_find = "SELECT COUNT(*) FROM poke_stat WHERE id_name='".$poke_name_id. "'";
                    $result = $link->query($sql_find);
                    $num_find = $result->fetch();
                    print_r($num_find[0]);

                    $sql = "INSERT IGNORE INTO poke_stat(id_name, display_name, img_link, type_name, allowed_moveset, efficiency, 
                      base_stat) VALUES ('$poke_name_id', '$display_name', '$img_link', '$type_name', '$allowed_moveset', '$efficiency', '$base_stat')";
                    $link->exec($sql);

                    echo "Created";*/
                    /*
                    if ($num_find[0] < 1){
                        $sql = "INSERT IGNORE INTO poke_stat(id_name, display_name, img_link, type_name, allowed_moveset, efficiency, 
                      base_stat) VALUES ('$poke_name_id', '$display_name', '$img_link', '$type_name', '$allowed_moveset', '$efficiency', '$base_stat')";
                        $link->exec($sql);

                        echo "Created";
                    }*/
                }


            }
        }
        catch (PDOException $e){

        }    } catch(PDOException $e){
        echo "Connection Failed 404: ". $e->getMessage();
    }