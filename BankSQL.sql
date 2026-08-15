CREATE TABLE users(
    user_id SERIAL PRIMARY KEY,
    profile_pic_url VARCHAR(500),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    user_name VARCHAR(25) UNIQUE NOT NULL,
    password VARCHAR(16) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    account_number VARCHAR(9) UNIQUE NOT NULL,
    account_amount DECIMAL(10,2) DEFAULT 0 NOT NULL
    );


INSERT INTO users(
    profile_pic_url,
    first_name,
    last_name,
    user_name,
    password,
    email,
    account_number
) VALUES (
    'https://www.reddit.com/r/Spiderman/comments/1j9yfr7/how_would_you_want_a_new_spiderman_show_to_happen/',
    'Darcel',
    'Sanders',
    'Darcel93',
    'password123',
    'darcel.d.sanders@gmail.com',
    'DS5432111'
);

DROP TABLE users;