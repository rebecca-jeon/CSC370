-- Show which county has the largest relative population decrease
-- from 2010 to 2019.
-- 1.1 marks: <11 operators
-- 1.0 marks: <13 operators
-- 0.9 marks: <16 operators
-- 0.8 marks: correct answer



select county.name, y10.population as '2010', y19.population as '2019', state.abbr, ((y10.population - y19.population)
/y10.population * 100) as 'Loss (%)'
from (select * from countypopulation where year = 2010) as y10 join (select * from countypopulation where year
= 2019) as y19 on (y10.county = y19.county) join county on (y10.county = fips) join state on (state = state.id)
order by  ((y10.population - y19.population)
/y10.population * 100) desc limit 1;

