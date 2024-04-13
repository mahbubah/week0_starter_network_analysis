CREATE TABLE Source (
    source_id SERIAL PRIMARY KEY,
    source_name VARCHAR(255)
);

CREATE TABLE Author (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(255)
);

CREATE TABLE Article (
    article_id SERIAL PRIMARY KEY,
    source_id INT,
    author_id INT,
    title VARCHAR(255),
    description TEXT,
    url VARCHAR(255),
    url_to_image VARCHAR(255),
    published_at TIMESTAMP,
    content TEXT,
    category VARCHAR(255),
    title_sentiment VARCHAR(50),
    FOREIGN KEY (source_id) REFERENCES Source(source_id),
    FOREIGN KEY (author_id) REFERENCES Author(author_id)
);