-- Retrieve in descending order of labour force size
-- all counties that had unemployment rates over 10%
-- in the 2008 census.
-- Hint: Unemployment rate = unemployment / labour force
-- 1.1 marks: <9 operators
-- 1.0 marks: <10 operators
-- 1.0 marks: <15 operators
-- 0.8 marks: correct answer
select county.name, state.abbr, temp.labour_force, temp.unemploymentrate as 'Unemployment Rate' from 
(select county, labour_force, (unemployed/labour_force) * 100 as unemploymentrate from countylabourstats 
where (unemployed/labour_force) * 100 > 10 and year = 2008) as temp join county on  (county = fips) 
join state on (state = state.id) order by labour_force desc;
