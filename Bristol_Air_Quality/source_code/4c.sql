-- ---------------------------------------------------------------------------------------------------------
-- Task: Return the mean values of NO2 (nitrogen dioxide) & NO (nitric oxide) by each station for the year 
-- 2019 for readings taken on or near 08:00 hours (peak traffic intensity).
-- ---------------------------------------------------------------------------------------------------------

SELECT AQ.`SiteID` StationNumber, LOC.`Location` StationName, FORMAT(AVG(AQ.`NO2`), 2) MEAN_NO2 , FORMAT(AVG(AQ.`NO`), 2) MEAN_NO 
FROM `airquality` AQ , `location` LOC 
WHERE AQ.`SiteID` = LOC.`Id` 
AND YEAR(AQ.`Date Time`) = 2019 
AND HOUR(AQ.`Date Time`) = 8 
GROUP BY AQ.`SiteID`
ORDER BY AQ.`SiteID` ASC




