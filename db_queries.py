# Here I've written some SQL queries for the reference
# Here "flask_db" is my db name

"""
CREATE TABLE flask_db.users (
 `id` bigint unsigned NOT NULL AUTO_INCREMENT,
 `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
 `email` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
 `password` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
 `phone` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
 `role` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
 PRIMARY KEY (`id`),
 UNIQUE KEY `users_email_unique` (`email`)
)
"""

"""
INSERT
	INTO
	flask_db.users (name,
	email,
	password,
	phone,
	role)
VALUES('goku',
'goku@toei.com',
'dbz',
'123123',
'admin');
"""