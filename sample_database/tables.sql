CREATE TABLE `book_genre` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `name` varchar(255) NOT NULL COMMENT 'genre name',
  PRIMARY KEY (`id`)
);

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

CREATE TABLE `member` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT 'primary key',
  `first_name` varchar(255) NOT NULL COMMENT 'member first name',
  `last_name` varchar(255) NOT NULL COMMENT 'member last name',
  `email` varchar(255) NOT NULL COMMENT 'member email',
  PRIMARY KEY (`id`)
);

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