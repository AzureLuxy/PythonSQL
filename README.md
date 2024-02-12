Данный скрипт предлагает пользователю выбрать номер запроса, отправляет запрос на localhost, где его получает сервер MySQL.
Сделала больше из любопытства, может ли оно так работать :)

Список запросов из [интерактивного тренажера](https://stepik.org/course/63054/syllabus):

1. [Вложенные запросы в операторах соединения:](https://stepik.org/lesson/308886/step/8?thread=solutions&unit=291012)
```SQL
SELECT title, name_author, name_genre, price, amount from author a
JOIN book b USING(author_id)
JOIN genre g USING(genre_id)
WHERE g.genre_id IN
    (SELECT query.genre_id from
        (SELECT genre_id, sum(amount) AS total_amount from book GROUP BY genre_id) query
WHERE total_amount = (SELECT MAX(total_amount) FROM (SELECT SUM(amount) AS total_amount FROM book GROUP BY genre_id) subquery))
ORDER by title;
```
2. 
