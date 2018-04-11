CREATE DATABASE mealplanner_recipe_system;

USE mealplanner_recipe_system;

CREATE table user_profile(
    user_id int AUTO_INCREMENT PRIMARY KEY,
    first_name varchar(20),
    last_name varchar(30),
    gender varchar(10),
    username varchar(50),
    meal_preference varchar(50),
    password varchar(255)
    ) AUTO_INCREMENT=10000 ;
    
-- DELIMITER $$
-- CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_createUser`(
--     IN p_name VARCHAR(20),
--     IN p_username VARCHAR(20),
--     IN p_password VARCHAR(20)
-- )
-- BEGIN
--     if ( select exists (select 1 from tbl_user where user_username = p_username) ) THEN
     
--         select 'Username Exists !!';
     
--     ELSE
     
--         insert into tbl_user
--         (
--             user_name,
--             user_username,
--             user_password
--         )
--         values
--         (
--             p_name,
--             p_username,
--             p_password
--         );
     
--     END IF;
-- END$$
-- DELIMITER ;