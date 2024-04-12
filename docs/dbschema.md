CREATE TABLE articles (
    article_id SERIAL PRIMARY KEY,
    source_id VARCHAR(255),
    source_name VARCHAR(255),
    author VARCHAR(255),
    title VARCHAR(255),
    description TEXT,
    url TEXT,
    url_to_image TEXT,
    published_at TIMESTAMP WITH TIME ZONE,
    content TEXT,
    category VARCHAR(255),
    article TEXT,
    title_sentiment FLOAT
);
