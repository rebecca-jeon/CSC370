-- Retrieve the state with the median number of
-- employees in 'Education Services'
-- 1.1 marks: < 10 operators
-- 1.0 marks: < 11 operators
-- 0.8 marks: correct answer

select state.abbr, sum(employees) as TotalEmployees 
from countyindustries join county on (county = fips) join state on (state = state.id) where industry = 10 
group by state order by TotalEmployees limit 25, 1;





