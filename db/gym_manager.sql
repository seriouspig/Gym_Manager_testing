DROP TABLE events;
DROP TABLE members;
DROP TABLE activities;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    date_of_birth VARCHAR(255),
    age VARCHAR(255),
    photo VARCHAR(255),
    platinum BIT
);

