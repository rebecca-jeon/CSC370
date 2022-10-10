-- Out of those counties with at least 25000 residents,
-- retrieve the pair from the same state
-- that had the absolute closest
-- population in 2018
-- 1.1 marks: <11 operators
-- 1.0 marks: <12 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer


select p1.name, p1.population, p2.name, p2.population from 
( select * from countypopulation join county on (county = fips) where population > 25000 and year = 2018) as p1,
 (select * from countypopulation join county on (county = fips) where population > 25000 and year = 2018) as p2 
 where p1.state = p2.state and p1.county <> p2.county  and p1.population < p2.population 
 order by abs(p1.population - p2.population) asc limit 1;


