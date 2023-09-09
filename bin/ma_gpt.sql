CREATE TABLE MA_GPT (
    id SERIAL PRIMARY KEY,
    file_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    last_modified TIMESTAMPTZ NOT NULL,
    size BIGINT NOT NULL,
    prompt TEXT,
    content TEXT
);

