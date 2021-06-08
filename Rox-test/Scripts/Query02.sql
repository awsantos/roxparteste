SELECT top 3 P.Name,
           P.DaysToManufacture,
           sum(D.OrderQty) AS Quantidade
FROM SalesOrderDetail AS D
JOIN SpecialOfferProduct AS O ON D.ProductID = O.ProductID
JOIN Product AS P ON D.ProductID = P.ProductID
GROUP BY P.Name,
         P.DaysToManufacture
ORDER BY Quantidade DESC