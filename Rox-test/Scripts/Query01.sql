WITH orders(salesorderid, soma) AS
  (SELECT a.salesorderid,
          count(a.salesorderid)
   FROM salesorderdetail AS a
   GROUP BY salesorderid
   HAVING count(a.salesorderid) > 2)
SELECT count(*)
FROM orders