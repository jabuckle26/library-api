CREATE TABLE `book_genre` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `name` varchar(255) NOT NULL COMMENT 'genre name',
  PRIMARY KEY (`id`)
);

INSERT INTO `book_genre` (name) VALUES ('Horror'),
 ('Fantasy'),
 ('Classics'),
 ('Biography'),
 ('History'),
 ('Science-Fiction'),
 ('Crime'),
 ('Young-Adult'),
 ('War'),
 ('Romance');

CREATE TABLE `book` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `title` varchar(255) NOT NULL COMMENT 'book title',
  `author` varchar(255) DEFAULT NULL COMMENT 'book author',
  `page_count` int DEFAULT NULL COMMENT 'number of pages',
  `book_genre` int DEFAULT NULL COMMENT 'foreign key book genre',
  PRIMARY KEY (`id`),
  KEY `book_genre` (`book_genre`),
  CONSTRAINT `book_ibfk_1` FOREIGN KEY (`book_genre`) REFERENCES `book_genre` (`id`)
);

INSERT INTO `book` (title, author, page_count, book_genre) VALUES 
('Harry Potter & The Philosophers Stone', 'J.K. Rowling', 234, 2),
('The Lord of the Rings - The Fellowship of the Ring', 'J.R.R Tolkien', 769, 2),
('The Subtle Knife', 'Philip Pullman', 548, 8),
('Wuthering Heights', 'Emily Bronte', 345, 3),
('Julius Caesar', 'William Shakespeare', 500, 3),
('Animal Farm', 'George Orwell', 100, 3),
('1984', 'George Orwell', 210, 3),
('A Storm of Swords', 'George R.R. Martin', 890, 2),
('Dracula', 'Bram Stoker', 300, 1),
('Catching Fire', 'Suzanne Collins', 473, 8),
('Woman in the Making: Pantis Memoir', 'Panti', 183, 4);

CREATE TABLE `member` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `first_name` varchar(255) NOT NULL COMMENT 'member first name',
  `last_name` varchar(255) NOT NULL COMMENT 'member last name',
  `email` varchar(255) NOT NULL COMMENT 'member email',
  PRIMARY KEY (`id`)
);

INSERT INTO `member` (first_name, last_name, email) VALUES
('Jon', 'Smith', 'jon.smith@email.com'),
('Jane', 'Smith', 'jane.smith@email.com'),
('Sam', 'Johnson', 'sam.johnson@email.com'),
('Sarah', 'Smith', 'sara.smith@email.com'),
('Patrick', 'Doe', 'pat.doe@email.com'),
('Peter', 'Roberts', 'peter.roberts@email.com'),
('Olivia', 'Church', 'olivia.church@email.com'),
('Phil', 'Yeung', 'phil.yeung@email.com'),
('Joe', 'Summers', 'joe.summers@email.com'),
('Darienne', 'Summers', 'darienne.summers@email.com'),
('Kay', 'Nguyen', 'kay.nguyen@email.com'),
('Rachel', 'Green', 'rachel.green@email.com'),
('Josh', 'Patel', 'josh.patel@email.com');

CREATE TABLE `borrowed_books` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `book_id` int NOT NULL COMMENT 'book withdrawn',
  `member_id` int NOT NULL COMMENT 'the member',
  `withdraw_date` datetime NOT NULL COMMENT 'date book taken out',
  `due_date` datetime NOT NULL COMMENT 'date book due for return',
  `is_overdue` tinyint NOT NULL COMMENT 'is book overdue',
  `is_returned` tinyint NOT NULL COMMENT 'is book returned',
  `returned_date` datetime DEFAULT NULL COMMENT 'date book returned',
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `borrowed_books_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `book` (`id`),
  CONSTRAINT `borrowed_books_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
);

INSERT INTO `borrowed_books` (book_id, member_id, withdraw_date, due_date, is_overdue, is_returned, returned_date) VALUES
(1, 2, '2008-7-04', '2008-8-04', TRUE, FALSE, NULL),
(2, 2, '2008-7-04', '2008-8-04', TRUE, FALSE, NULL),
(3, 2, '2008-7-04', '2008-8-04', TRUE, FALSE, NULL),
(4, 5, '2010-11-01', '2010-12-01', TRUE, FALSE, NULL),
(8, 6, '2021-7-30', '2008-8-030', TRUE, FALSE, NULL),
(11, 5, '2018-1-01', '2018-2-01', FALSE, TRUE, '2018-1-31'),
(11, 4, '2016-1-01', '2018-2-01', FALSE, TRUE, '2018-1-31'),
(11, 2, '2016-10-01', '2018-11-01', FALSE, TRUE, '2018-10-28'),
(5, 2, '2019-1-01', '2019-2-01', FALSE, TRUE, '2019-1-29'),
(7, 5, '2021-9-01', '2021-11-01', FALSE, FALSE, NULL),
(11, 5, '2021-9-12', '2021-11-30', FALSE, FALSE, NULL),
(5, 5, '2021-10-14', '2021-11-20', FALSE, FALSE, NULL),
(10, 5, '2021-10-20', '2021-11-02', FALSE, FALSE, NULL);