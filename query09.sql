-- Show which industries in which states (except DC)
-- employed at least 7.5% of the state's 2019 population,
-- ordered by the total payroll for that industry
-- in that state.
-- 1.1 marks: <26 operators
-- 1.0 marks: <30 operators
-- 0.9 marks: <35 operators
-- 0.8 marks: correct answer

select abbr, name, total_payroll as 'Total Payrolls', (employees / total_population) * 100  as '% of Population' from 
(select abbr, industry.name, sum(employees) as employees,  sum(payroll) as total_payroll, total_population 
from countyindustries join county on (county = fips)join state on (state = state.id) join industry on (industry = industry.id) 
natural join (select abbr, sum(population) as total_population from countypopulation join county on (county = fips) 
join state on (state = state.id) where year = 2019 group by abbr) as sub1 group by abbr, industry) 
 as sub2 where (employees / total_population) * 100 >= 7.5 and abbr <> 'DC' order by total_payroll desc;
