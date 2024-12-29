-- create the database
CREATE DATABASE IF NOT EXISTS itemDb;

-- use the current db
USE itemDb;

-- create a table for items
CREATE TABLE Items
(
    item_id  INT UNSIGNED PRIMARY KEY,
    name     VARCHAR(255) NOT NULL,
    brand    VARCHAR(255),
    price DECIMAL(10, 2) NOT NULL,
    oldPrice DECIMAL(10,2) NOT NULL,
    discount NUMERIC (5,4) NOT NULL,
    UNIQUE (name, brand)
);

ALTER TABLE Items ADD UNIQUE (item_id, price);