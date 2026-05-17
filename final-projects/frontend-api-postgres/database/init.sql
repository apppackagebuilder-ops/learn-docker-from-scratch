CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL
);

INSERT INTO products (name, description, price)
VALUES
    ('Starter Notebook', 'A small notebook for sketching Docker ideas.', 9.99),
    ('Container Mug', 'A mug for long debugging sessions.', 14.50),
    ('Compose Poster', 'A desk poster that explains service relationships.', 19.00)
ON CONFLICT DO NOTHING;
