-- ------------------------------------------------------------------------------------------------
-- Task: Extend the previous query to show these values for all stations in the years 2010 to 2019. 
-- ------------------------------------------------------------------------------------------------

SELECT AQ.`SiteID` StationNumber, LOC.`Location` StationName, FORMAT(AVG(AQ.`NO2`), 2) MEAN_NO2 , FORMAT(AVG(AQ.`NO`), 2) MEAN_NO 
FROM `airquality` AQ , `location` LOC 
WHERE AQ.`SiteID` = LOC.`Id` 
AND YEAR(AQ.`Date Time`) BETWEEN 2010 AND 2019 
AND HOUR(AQ.`Date Time`) = 8 
GROUP BY AQ.`SiteID`
ORDER BY AQ.`SiteID` ASC




