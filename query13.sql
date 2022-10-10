-- Retrieve alphabetically all states
-- with at least one hundred counties.
-- 1.1 marks: <6 operators
-- 1.0 marks: <8 operators
-- 0.8 marks: correct answer

select abbr from county join state on (state = state.id) group by abbr having count(*) >= 100 order by abbr;