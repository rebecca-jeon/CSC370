-- Retrieve alphabetically the states that had
-- over 100 counties with unemployment rates above 6.0%
-- in 2008.
-- Hint: Unemployment rate = unemployed / labour force
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.9 marks: <11 operators
-- 0.8 marks: correct answer

select abbr from countylabourstats join county on (county = fips) join state on (state = state.id) 
where year = 2008 and ((unemployed / labour_force) * 100) > 6 group by abbr having count(*) > 100 order by abbr;