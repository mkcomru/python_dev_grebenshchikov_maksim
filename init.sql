CREATE DATABASE authors_db;
\c authors_db;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE,
    login VARCHAR UNIQUE
);

CREATE TABLE blog (
    id SERIAL PRIMARY KEY,
    owner_id INTEGER REFERENCES users(id),
    name VARCHAR,
    description VARCHAR
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    header VARCHAR,
    text VARCHAR,
    author_id INTEGER REFERENCES users(id),
    blog_id INTEGER REFERENCES blog(id)
);

INSERT INTO users (email, login) VALUES 
    ('user1@example.com', 'user1'),
    ('user2@example.com', 'user2');

INSERT INTO blog (owner_id, name, description) VALUES 
    (1, 'First Blog', 'Blog for user1'),
    (2, 'Second Blog', 'Blog for user2');

INSERT INTO post (header, text, author_id, blog_id) VALUES 
    ('Hello World', 'First post content', 1, 1),
    ('Second Post', 'Another post', 2, 2);

CREATE DATABASE tech_info_db;
\c tech_info_db;

CREATE TABLE space_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR UNIQUE
);

CREATE TABLE event_type (
    id SERIAL PRIMARY KEY,
    name VARCHAR UNIQUE
);

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    datetime TIMESTAMP,
    user_id INTEGER,
    space_type_id INTEGER REFERENCES space_type(id),
    event_type_id INTEGER REFERENCES event_type(id)
);

INSERT INTO space_type (name) VALUES 
    ('global'),
    ('blog'),
    ('post');

INSERT INTO event_type (name) VALUES 
    ('login'),
    ('comment'),
    ('create_post'),
    ('delete_post'),
    ('logout');

INSERT INTO logs (datetime, user_id, space_type_id, event_type_id) VALUES 
    (NOW(), 1, 3, 2),
    (NOW(), 2, 3, 2),
    (NOW(), 1, 1, 1),
    (NOW(), 2, 1, 1); 