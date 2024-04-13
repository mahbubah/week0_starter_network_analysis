import psycopg2

# Database connection parameters
host = 'localhost'
port = '5000'
database = 'postgres'
user = 'postgres'
password = 'Mahi@0938'

# Establish a connection to the database
conn = psycopg2.connect(
    host=host,
    port=port,
    database=database,
    user=user,
    password=password
)

# Create a cursor object
cur = conn.cursor()

# Define SQL statements to create tables
create_source_table = """
CREATE TABLE IF NOT EXISTS source (
    source_id SERIAL PRIMARY KEY,
    source_name VARCHAR
);
"""

create_author_table = """
CREATE TABLE IF NOT EXISTS author (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR
);
"""

create_article_table = """
CREATE TABLE IF NOT EXISTS article (
    article_id SERIAL PRIMARY KEY,
    source_id INT,
    author_id INT,
    title VARCHAR,
    description TEXT,
    url VARCHAR,
    url_to_image VARCHAR,
    published_at TIMESTAMP,
    content TEXT,
    category VARCHAR,
    title_sentiment VARCHAR,
    FOREIGN KEY (source_id) REFERENCES source(source_id),
    FOREIGN KEY (author_id) REFERENCES author(author_id)
);
"""
# Execute SQL statements to create tables
cur.execute(create_source_table)
cur.execute(create_author_table)
cur.execute(create_article_table)

# Execute SQL query to retrieve list of tables
cur.execute("""
    SELECT table_name 
    FROM information_schema.tables 
    WHERE table_schema = 'public' 
    AND table_type = 'BASE TABLE'
""")

# Fetch all results
tables = cur.fetchall()

# Print the list of tables
for table in tables:
    print(table[0])


# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
