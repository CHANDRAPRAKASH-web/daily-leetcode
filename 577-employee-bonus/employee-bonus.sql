# Write your MySQL query statement below
SELECT name,bonus FROM Employee left join Bonus on Employee.empId = Bonus.empId WHERE bonus is NULL or bonus<1000;
