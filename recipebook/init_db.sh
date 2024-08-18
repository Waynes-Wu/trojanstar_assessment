#!/bin/bash

# Wait for SQL Server to start
sleep 5s

# Run the SQL commands to set up the database and tables
/opt/mssql-tools18/bin/sqlcmd -S localhost -U sa -P \!Abc123\! -C -Q "

IF EXISTS (SELECT name FROM sys.databases WHERE name = N'recipebook')
BEGIN
    ALTER DATABASE recipebook SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE recipebook;
END;



CREATE DATABASE recipebook;
GO

USE recipebook;
GO

CREATE TABLE recipe (
    recipe_id INT PRIMARY KEY IDENTITY(1,1), 
    name VARCHAR(255) NOT NULL, 
    ingredients TEXT NOT NULL, 
    steps TEXT NOT NULL, 
    preparation_time INT NOT NULL
);
GO

CREATE TABLE rating (
    rating_id INT PRIMARY KEY IDENTITY(1,1), 
    recipe_id INT FOREIGN KEY REFERENCES recipe(recipe_id), 
    rating INT, 
    user_id INT
);
GO

CREATE TABLE comments (
    comment_id INT PRIMARY KEY IDENTITY(1,1), 
    recipe_id INT FOREIGN KEY REFERENCES recipe(recipe_id), 
    comment_text TEXT,
    user_id INT
);
GO

CREATE TABLE users (
    user_id INT PRIMARY KEY IDENTITY(1,1), 
    username VARCHAR(255) NOT NULL, 
    password VARCHAR(255) NOT NULL
);
GO

INSERT INTO users (username, password) VALUES 
('user1', 'password1'),
('user2', 'password2');

INSERT INTO recipe (name, ingredients, steps, preparation_time) VALUES 
('Scrambled Eggs', 'Eggs, Milk, plant milk, Extra-virgin olive oil or butter, or water, Salt', 'First, beat the eggs, Next, gently preheat the pan, Finally, cook', 5),
('Hard Boiled Eggs', 'Eggs', 'First, boil the eggs, Then, let them sit in the hot water, Finally, move them to an ice bath', 15);

INSERT INTO rating (recipe_id, rating, user_id) VALUES 
(1, 5, 1),
(2, 4, 2);

INSERT INTO comments (recipe_id, comment_text, user_id) VALUES 
(1, 'Delicious!', 1),
(2, 'Tasty but a bit dry', 2);

"
