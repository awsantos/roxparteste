SELECT P.FirstName,
       P.MiddleName,
       P.LastName,
       count(S.SalesOrderID) AS 'Pedidos'
FROM Person AS P
JOIN Customer AS C ON P.BusinessEntityID = C.PersonID
JOIN SalesOrderHeader AS S ON C.CustomerID = S.CustomerID
GROUP BY P.FirstName,
         P.MiddleName,
         P.LastName
ORDER BY pedidos DESC