SELECT a.name_author, sum(b.amount) as Количество from author a
LEFT JOIN book b
ON a.author_id = b.author_id
GROUP BY a.name_author
HAVING Количество<10 OR Количество IS NULL
ORDER BY Количество;