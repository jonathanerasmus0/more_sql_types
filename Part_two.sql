-- Exercise 1 for PART 2 

SELECT name
FROM site_user
WHERE array_length(siblings, 1) > 1;

