-- ----------------------------------------------------------------------
-- Task: Return the station number, station name and date/time of the 
-- highest recorded value of carbon monoxide (CO) found in the dataset.
-- ----------------------------------------------------------------------

SELECT AQ.`SiteID` StationNumber, LOC.`Location` StationName, AQ.`Date Time`,  AQ.`CO` MAX_CO 
FROM `airquality` AQ , `location` LOC 
WHERE AQ.`SiteID` = LOC.`Id` 
AND AQ.`CO` = (SELECT MAX(`CO`) FROM `airquality`)
ORDER BY AQ.`Date Time` ASC





