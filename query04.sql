-- Retrieve alphabetically all states in which
-- every county has a name not found anywhere else
-- in the US
-- 1.1 marks: <8 operators
-- 1.0 marks: <9 operators
-- 0.8 marks: correct answer


-- Replace this comment line with the actual query

select distinct state.abbr from county join state on (state = state.id) 
where state not in (select distinct state from county where name in (select name from county group by name having count(*) > 1)) 
order by abbr;