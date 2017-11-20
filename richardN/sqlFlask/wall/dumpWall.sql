SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema wall
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `wall` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci ;
USE `wall` ;

-- -----------------------------------------------------
-- Table `wall`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wall`.`users` (
  `id` INT NOT NULL,
  `first_name` VARCHAR(255) NULL,
  `last_name` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` VARCHAR(255) NULL,
  `updated_at` VARCHAR(255) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wall`.`messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wall`.`messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `users_id` INT NOT NULL,
  `message` TEXT NULL,
  `created_at` VARCHAR(255) NULL,
  `updated_at` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_messages_users1_idx` (`users_id` ASC),
  CONSTRAINT `fk_messages_users1`
    FOREIGN KEY (`users_id`)
    REFERENCES `wall`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `wall`.`comments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wall`.`comments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `users_id` INT NOT NULL,
  `messages_id` INT NOT NULL,
  `comment` TEXT NULL,
  `created_at` VARCHAR(255) NULL,
  `updated_at` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comments_users_idx` (`users_id` ASC),
  INDEX `fk_comments_messages1_idx` (`messages_id` ASC),
  CONSTRAINT `fk_comments_users`
    FOREIGN KEY (`users_id`)
    REFERENCES `wall`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_comments_messages1`
    FOREIGN KEY (`messages_id`)
    REFERENCES `wall`.`messages` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
