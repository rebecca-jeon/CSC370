-- Retrieve by life expectancy all
-- counties that have no industry data
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

select * from county where fips not in (select county from countyindustries) order by life_expectancy;