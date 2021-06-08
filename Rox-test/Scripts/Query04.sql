SELECT P.Name,
       sum(D.OrderQty) AS Quantidade,
       S.OrderDate
FROM SalesOrderHeader AS S
INNER JOIN SalesOrderDetail AS D ON S.SalesOrderID = S.SalesOrderID
INNER JOIN Product AS P ON D.ProductID = P.ProductID
GROUP BY P.Name,
         S.OrderDate