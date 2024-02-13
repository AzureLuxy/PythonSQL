Данный скрипт предлагает пользователю выбрать номер запроса, отправляет запрос на localhost, где его получает сервер MySQL.
Сделала больше из любопытства, может ли оно так работать :)

Список запросов из [интерактивного тренажера](https://stepik.org/course/63054/syllabus):

База [отсюда](https://stepik.org/lesson/308891/step/4?unit=291017).

1. [Вложенные запросы в операторах соединения](https://stepik.org/lesson/308886/step/8?thread=solutions&unit=291012):
Вывести информацию о книгах (название книги, фамилию и инициалы автора, название жанра, цену и количество экземпляров книги), написанных в самых популярных жанрах, в отсортированном в алфавитном порядке по названию книг виде. Самым популярным считать жанр, общее количество экземпляров книг которого на складе максимально.
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
2. [Запросы для нескольких таблиц с группировкой](https://stepik.org/lesson/308886/step/6?unit=291012):
Посчитать количество экземпляров  книг каждого автора из таблицы author.  Вывести тех авторов,  количество книг которых меньше 10, в отсортированном по возрастанию количества виде. Последний столбец назвать Количество.
```SQL
SELECT a.name_author, sum(b.amount) as Количество from author a
LEFT JOIN book b
ON a.author_id = b.author_id
GROUP BY a.name_author
HAVING Количество<10 OR Количество IS NULL
ORDER BY Количество;
```
3. [Задание](https://stepik.org/lesson/308891/step/6?unit=291017): Посчитать, сколько раз была заказана каждая книга, для книги вывести ее автора (нужно посчитать, в каком количестве заказов фигурирует каждая книга).  Вывести фамилию и инициалы автора, название книги, последний столбец назвать Количество. Результат отсортировать сначала  по фамилиям авторов, а потом по названиям книг.
```SQL
SELECT name_author, title, COALESCE(bcount,0) as Количество from book
LEFT JOIN author USING (author_id)
LEFT JOIN (SELECT count(amount) as bcount, book_id
    from buy_book
    GROUP BY book_id) as ss USING (book_id)
ORDER BY name_author, title;
```
