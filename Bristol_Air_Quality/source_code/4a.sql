
-- -----------------------------------------------------
-- Task: Select a specific stations data for the year 2019
-- Put SiteID for a specific stations data 
-- -----------------------------------------------------

SELECT * 
FROM `airquality` 
WHERE YEAR(`Date Time`) = 2019 
AND `SiteID` = 203





