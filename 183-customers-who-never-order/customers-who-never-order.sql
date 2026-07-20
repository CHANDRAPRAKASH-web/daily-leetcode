# Write your MySQL query statement below
SELECT C.name as Customers FROM Customers C LEFT JOIN Orders on C.id=Orders.customerId WHERE Orders.id IS NULL;
