CREATE TABLE IF NOT EXISTS poke_stat(
    id INT NOT NULL PRIMARY KEY NOT NULL,
    id_name VARCHAR(20),
    display_name VARCHAR(20),
    type_name JSON,
    allowed_moveset JSON,
    efficiency JSON,
    base_stat JSON
)