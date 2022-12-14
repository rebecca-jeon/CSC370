-- Retrieve alphabetically the names of industries that
-- employ at least five million workers across
-- the US, excluding California.
-- 1.1 marks: <9 operators
-- 1.0 marks: <11 operators
-- 0.9 marks: <14 operators
-- 0.8 marks: correct answer

select industry.name from countyindustries join industry on (industry = industry.id) join county on (county = fips)
where state <> 5 group by industry having sum(employees) > 5000000 order by industry.name;