CREATE TABLE IF NOT EXISTS users(
    id INT NOT NULL PRIMARY KEY NOT NULL AUTO_INCREMENT,
    display_name VARCHAR(20),
    username VARCHAR(20),
    user_password VARCHAR(20),
    owned_pokemon JSON,
    active_pokemon JSON
);
CREATE TABLE IF NOT EXISTS poke_actor(
    id INT NOT NULL PRIMARY KEY NOT NULL AUTO_INCREMENT,
    user_id INT,
    pokemon_id INT,
    self_stat JSON,
    active_moveset JSON
);
CREATE TABLE IF NOT EXISTS poke_stat(
    id INT NOT NULL PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_name VARCHAR(100),
    display_name VARCHAR(100),
    img_link VARCHAR(2083),
    type_name JSON,
    allowed_moveset JSON,
    efficiency JSON,
    base_stat JSON
);

CREATE TABLE IF NOT EXISTS moveset(
    id INT NOT NULL PRIMARY KEY NOT NULL AUTO_INCREMENT,
    id_name VARCHAR(100),
    title VARCHAR(100),
    type VARCHAR(100),
    cat VARCHAR(100),
    stats JSON,
    effect LONGTEXT
);
