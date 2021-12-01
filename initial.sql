-- ----------------------------------------------------
-- AÑADO USUARIO MULTIHOST
-- ----------------------------------------------------
CREATE USER 'dbadmin'@'%' IDENTIFIED BY 'DBadminpass'; GRANT ALL PRIVILEGES ON *.* TO 'dbadmin'@'%' WITH GRANT OPTION;


-- -----------------------------------------------------
-- Schema django
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `django` DEFAULT CHARACTER SET utf8 ;
USE `django` ;
