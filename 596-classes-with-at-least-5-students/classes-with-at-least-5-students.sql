# Write your MySQL query statement below
SELECT CLASS FROM Courses GROUP BY class HAVING COUNT(class)>=5;
