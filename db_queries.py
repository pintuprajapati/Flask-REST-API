# Here I've written some SQL queries for the reference
# Here "flask_db" is my db name

####### USER table #######

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

####### ROLES table #######
## Create "Roles" table
# Create `id` and `title` column into roles table
"""
CREATE TABLE flask_db.roles (
	`id` bigint unsigned NOT NULL AUTO_INCREMENT,
	`title` varchar(45) NULL,
    PRIMARY KEY (`id`)
)
"""

## Add foreign key of `roles table's` id field's to the user's table
"""
# Create a 'role_id' field in `users` table then add foreign key to that
ALTER TABLE flask_db.users ADD CONSTRAINT users_FK FOREIGN KEY (`role_id`) REFERENCES flask_db.roles(`id`) ON DELETE NO ACTION ON UPDATE CASCADE;
"""


####### ENDPOINT table #######
## Create "Endpoint" table
# Create id, endpoint, method
"""
CREATE TABLE flask_db.endpoints (
	`id` bigint unsigned NOT NULL AUTO_INCREMENT,
	`endpoint` varchar(100) NULL,
	`method` varchar(20) NULL,
    PRIMARY KEY (`id`)
)
"""
  
####### ACCESSIBILITY table #######
## Create "Accessibility" table
# Create id, endpoint, method
"""
CREATE TABLE flask_db.acceessibility (
	`id` bigint unsigned NOT NULL AUTO_INCREMENT,
	`endpoint_id` bigint unsigned NULL,
	`roles` LONGTEXT NULL,
    PRIMARY KEY (`id`)
)
"""

# Add foreign key of endpint's table to the id of accessibility table
"""
ALTER TABLE flask_db.acceessibility ADD CONSTRAINT acceessibility_FK FOREIGN KEY (id) REFERENCES flask_db.endpoint(id) ON UPDATE CASCADE;
"""

####### Create View #######
# Create a VIEW after joining two tables: endpoints and accessibility
"""
CREATE VIEW `accessibility_view` AS SELECT
endponts.endpoint,
accessibility.roles
FROM endpoints join accessibility
WHERE endpoints.id = accessibility.endpoint_id;
"""

