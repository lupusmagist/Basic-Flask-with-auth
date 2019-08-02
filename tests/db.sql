--
-- File generated with SQLiteStudio v3.2.1 on Fri Aug 2 09:29:36 2019
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: role
DROP TABLE IF EXISTS role;
CREATE TABLE role (
	id INTEGER NOT NULL, 
	name VARCHAR(80), 
	description VARCHAR(255), 
	PRIMARY KEY (id), 
	UNIQUE (name)
);
INSERT INTO role (id, name, description) VALUES (1, 'user', NULL);
INSERT INTO role (id, name, description) VALUES (2, 'admin', NULL);

-- Table: role_users
DROP TABLE IF EXISTS role_users;
CREATE TABLE role_users (
	user_id INTEGER, 
	role_id INTEGER, 
	FOREIGN KEY(role_id) REFERENCES role (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
);
INSERT INTO role_users (user_id, role_id) VALUES (1, 1);
INSERT INTO role_users (user_id, role_id) VALUES (2, 1);

-- Table: user
DROP TABLE IF EXISTS user;
CREATE TABLE user (
	id INTEGER NOT NULL, 
	username VARCHAR(255) NOT NULL, 
	password VARCHAR(255), 
	PRIMARY KEY (id)
);
INSERT INTO user (id, username, password) VALUES (1, 'user', X'243262243132246A6735624F6D72456870544F74542F645470543050757477432E7366365359796E6F484B6779686533655079655034715862704871');
INSERT INTO user (id, username, password) VALUES (2, 'admin', X'243262243132246765724D342E474F4F76354E6736694679706477622E6C693361686147482E54796373795650796656413768536141337268797A69');

-- Index: ix_user_username
DROP INDEX IF EXISTS ix_user_username;
CREATE UNIQUE INDEX ix_user_username ON user (username);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
