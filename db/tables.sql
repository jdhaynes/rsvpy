DROP TABLE rsvp_attendee;
DROP TABLE rsvp_event;
DROP TABLE rsvp_response;
DROP TABLE rsvp_user;

CREATE TABLE rsvp_user (
    id                  SERIAL PRIMARY KEY,
    first_name          VARCHAR(20) NOT NULL,
    last_name           VARCHAR(20) NOT NULL,
    email               VARCHAR(50) NOT NULL,
    password_hash       TEXT NOT NULL,
    password_salt       TEXT NOT NULL
);

CREATE TABLE rsvp_event (
    id                  SERIAL PRIMARY KEY,
    event_name          TEXT,
    close_date          TIMESTAMP NOT NULL,
    allow_tentative     BOOLEAN,
    owner_id            BIGINT NOT NULL REFERENCES rsvp_user(id),
    event_timestamp     TIMESTAMP NOT NULL,
    created_timestamp   TIMESTAMP NOT NULL
);

CREATE TABLE rsvp_response (
    id                  SERIAL PRIMARY KEY,
    label               VARCHAR(50)
);

CREATE TABLE rsvp_attendee (
    id                  SERIAL PRIMARY KEY,
    first_name          VARCHAR(20) NOT NULL,
    last_name           VARCHAR(20) NOT NULL,
    email               VARCHAR(50),
    response_id         BIGINT NOT NULL REFERENCES rsvp_response(id)
);