SELECT SalesOrderID,
       OrderDate,
       TotalDue
FROM SalesOrderHeader
WHERE TotalDue >= 1000
  AND month(OrderDate) = 9
  AND year(OrderDate) = 2011
ORDER BY TotalDue DESC