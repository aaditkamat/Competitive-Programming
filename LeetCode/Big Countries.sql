 Title: Big Countries
 Runtime: 271 ms
 Memory: N/A

# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE World.area > 3000000 or World.population > 25000000;