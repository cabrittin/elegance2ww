-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Emmons_N2U
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Emmons_N2U
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Emmons_N2U` ;
USE `Emmons_N2U` ;

-- -----------------------------------------------------
-- Table `Emmons_N2U`.`contin`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Emmons_N2U`.`contin` (
  `idcontin` INT NOT NULL,
  `continname` VARCHAR(45) NULL,
  `type` VARCHAR(45) NULL,
  PRIMARY KEY (`idcontin`),
  UNIQUE INDEX `idcontin_UNIQUE` (`idcontin` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Emmons_N2U`.`image`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Emmons_N2U`.`image` (
  `idimage` INT NOT NULL,
  `imagename` VARCHAR(45) NULL,
  `sectionnumber` INT NULL,
  `series` VARCHAR(45) NULL,
  PRIMARY KEY (`idimage`),
  UNIQUE INDEX `idimage_UNIQUE` (`idimage` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Emmons_N2U`.`object`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Emmons_N2U`.`object` (
  `idobject` INT NOT NULL,
  `x` INT(10) NULL,
  `y` INT(10) NULL,
  `idimage` INT NULL,
  `idcontin` INT NULL,
  PRIMARY KEY (`idobject`),
  INDEX `fk_object_1_idx` (`idcontin` ASC),
  INDEX `fk_object_ image_idx` (`idimage` ASC),
  UNIQUE INDEX `idobject_UNIQUE` (`idobject` ASC),
  CONSTRAINT `fk_object_contin`
    FOREIGN KEY (`idcontin`)
    REFERENCES `Emmons_N2U`.`contin` (`idcontin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_object_ image`
    FOREIGN KEY (`idimage`)
    REFERENCES `Emmons_N2U`.`image` (`idimage`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Emmons_N2U`.`synapse`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Emmons_N2U`.`synapse` (
  `idsynapse` INT NULL,
  `idcontin` INT NULL,
  `idpre` INT NULL,
  `idpost` INT NULL,
  INDEX `fk_synapse_contin_idx` (`idcontin` ASC),
  INDEX `fk_synapse_object_1_idx` (`idpre` ASC),
  INDEX `fk_synapse_object_2_idx` (`idpost` ASC),
  CONSTRAINT `fk_synapse_contin`
    FOREIGN KEY (`idcontin`)
    REFERENCES `Emmons_N2U`.`contin` (`idcontin`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_synapse_object_1`
    FOREIGN KEY (`idpre`)
    REFERENCES `Emmons_N2U`.`object` (`idobject`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_synapse_object_2`
    FOREIGN KEY (`idpost`)
    REFERENCES `Emmons_N2U`.`object` (`idobject`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Emmons_N2U`.`relationship`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Emmons_N2U`.`relationship` (
  `idrelationship` INT NOT NULL,
  `idobject1` INT NULL,
  `idobject2` INT NULL,
  PRIMARY KEY (`idrelationship`),
  INDEX `fk_relationship_object_1_idx` (`idobject1` ASC),
  INDEX `fk_relationship_object_2_idx` (`idobject2` ASC),
  UNIQUE INDEX `idrelationship_UNIQUE` (`idrelationship` ASC),
  CONSTRAINT `fk_relationship_object_1`
    FOREIGN KEY (`idobject1`)
    REFERENCES `Emmons_N2U`.`object` (`idobject`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_relationship_object_2`
    FOREIGN KEY (`idobject2`)
    REFERENCES `Emmons_N2U`.`object` (`idobject`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Emmons_N2U`.`display`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Emmons_N2U`.`display` (
  `idcontin` INT NULL,
  `idobject1` INT NULL,
  `x1` INT NULL,
  `y1` INT NULL,
  `z1` INT NULL,
  `cellbody1` INT(1) NULL DEFAULT 0,
  `remarks1` VARCHAR(45) NULL,
  `idobject2` INT NULL,
  `x2` INT NULL,
  `y2` INT NULL,
  `z2` INT NULL,
  `cellbody2` INT(1) NULL,
  `remarks2` VARCHAR(45) NULL,
  INDEX `fk_display_object_idx` (`idobject1` ASC),
  CONSTRAINT `fk_display_object`
    FOREIGN KEY (`idobject1`)
    REFERENCES `Emmons_N2U`.`object` (`idobject`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
