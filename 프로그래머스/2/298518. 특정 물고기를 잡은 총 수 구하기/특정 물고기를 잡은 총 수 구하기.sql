-- 코드를 작성해주세요
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO A
WHERE A.FISH_TYPE IN (SELECT FISH_TYPE FROM FISH_NAME_INFO WHERE FISH_NAME = "BASS" OR FISH_NAME = "SNAPPER")

