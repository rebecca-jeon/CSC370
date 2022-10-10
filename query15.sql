-- Show the percentage of counties that have more
-- females than males.
-- 1.1 marks: <8 operators
-- 1.0 marks: <10 operators
-- 0.9 marks: <13 operators
-- 0.8 marks: correct answer


select count(*)/ 3142 as Fraction from (select c1.county from genderbreakdown as c1, genderbreakdown as c2 where c1.county = c2.county and 
c1.gender = 'female' and c2.gender = 'male' and c1.population > c2.population group by county) as sub;