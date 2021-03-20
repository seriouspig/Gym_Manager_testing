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
    platinum VARCHAR(255)
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    trainer VARCHAR(255)
);

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    activity_id INT REFERENCES activities(id) ON DELETE CASCADE,
    day VARCHAR(255),
    time VARCHAR(255),
    room VARCHAR(255),
    capacity INT
);

