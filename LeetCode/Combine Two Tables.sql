 Title: Combine Two Tables
 Runtime: 229 ms
 Memory: N/A

# Write your MySQL query statement below
SELECT FirstName, LastName, City, State
FROM Person
LEFT JOIN Address
ON Person.PersonId = Address.PersonId;