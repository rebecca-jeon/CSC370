-- Retrieve by increasing snowfall the number of employees
-- in 'Mining, quarrying, and oil and gas extraction' for all
-- counties that have the words 'iron', 'coal', or 'mineral'
-- in their name.
-- 1.1 marks: <13 operators
-- 1.0 marks: <15 operators
-- 0.9 marks: <20 operators
-- 0.8 marks: correct answer

select name, abbr, employees from 

(select * from county join state on (state = state.id) where name like '%coal%' or name like '%mineral%' or name like '%iron%') as sub1

left join (select employees,county from countyindustries where industry = 19) as sub2 on (fips = county) order by snow;
