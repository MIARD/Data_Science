-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Measuring_Air_Quality
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Measuring_Air_Quality` ;

-- -----------------------------------------------------
-- Schema Measuring_Air_Quality
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Measuring_Air_Quality` DEFAULT CHARACTER SET utf8 ;
USE `Measuring_Air_Quality` ;

-- -----------------------------------------------------
-- Table `Measuring_Air_Quality`.`Location`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Measuring_Air_Quality`.`Location` (
  `Id` INT NOT NULL,
  `Location` VARCHAR(100) NOT NULL,
  `geo_point_2d` VARCHAR(100) NULL,
  PRIMARY KEY (`Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Measuring_Air_Quality`.`AirQuality`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Measuring_Air_Quality`.`AirQuality` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Date Time` DATETIME NOT NULL,
  `NOx` DOUBLE NULL,
  `NO2` DOUBLE NULL,
  `NO` DOUBLE NULL,
  `SiteID` INT NOT NULL,
  `PM10` DOUBLE NULL,
  `NVPM10` DOUBLE NULL,
  `VPM10` DOUBLE NULL,
  `NVPM2.5` DOUBLE NULL,
  `PM2.5` DOUBLE NULL,
  `VPM2.5` DOUBLE NULL,
  `CO` DOUBLE NULL,
  `O3` DOUBLE NULL,
  `SO2` DOUBLE NULL,
  `Temperature` FLOAT NULL,
  `RH` FLOAT NULL,
  `Air Pressure` DOUBLE NULL,
  `DateStart` DATETIME NULL,
  `DateEnd` DATETIME NULL,
  `Current` VARCHAR(5) NULL,
  `Instrument Type` VARCHAR(100) NULL,
  PRIMARY KEY (`Id`),
  INDEX `fk_AirQuality_Location_idx` (`SiteID` ASC),
  CONSTRAINT `fk_Air Quality_Location`
    FOREIGN KEY (`SiteID`)
    REFERENCES `Measuring_Air_Quality`.`Location` (`Id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
