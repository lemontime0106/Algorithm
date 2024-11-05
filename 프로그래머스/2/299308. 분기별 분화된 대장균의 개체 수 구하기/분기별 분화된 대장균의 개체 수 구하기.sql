-- 코드를 작성해주세요
SELECT 
CASE 
    WHEN DATE_FORMAT(DIFFERENTIATION_DATE, "%m") BETWEEN 1 AND 3 THEN "1Q"
    WHEN DATE_FORMAT(DIFFERENTIATION_DATE, "%m") BETWEEN 4 AND 6 THEN "2Q"
    WHEN DATE_FORMAT(DIFFERENTIATION_DATE, "%m") BETWEEN 7 AND 9 THEN "3Q"
    WHEN DATE_FORMAT(DIFFERENTIATION_DATE, "%m") BETWEEN 10 AND 12 THEN "4Q"
END AS QUARTER, COUNT(ID) AS ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER ASC;