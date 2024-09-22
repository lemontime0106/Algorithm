-- 코드를 작성해주세요
SELECT SUM(SCORE) AS `SCORE`, A.EMP_NO, A.EMP_NAME, A.POSITION, A.EMAIL
FROM HR_EMPLOYEES AS A
INNER JOIN HR_GRADE AS B
ON A.EMP_NO = B.EMP_NO
GROUP BY YEAR, EMP_NO
HAVING B.YEAR = '2022'
ORDER BY SCORE DESC
LIMIT 1;
