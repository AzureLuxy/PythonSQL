SELECT name_author, title, COALESCE(bcount,0) as Количество from book
LEFT JOIN author USING (author_id)
LEFT JOIN (SELECT count(amount) as bcount, book_id
    from buy_book
    GROUP BY book_id) as ss USING (book_id)
ORDER BY name_author, title;