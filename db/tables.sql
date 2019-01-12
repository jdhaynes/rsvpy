/* Drop existing tables. */
DROP TABLE IF EXISTS rsvp_attendee;
DROP TABLE IF EXISTS rsvp_event;
DROP TABLE IF EXISTS rsvp_response;
DROP TABLE IF EXISTS rsvp_user;

/* Extensions. */
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

/* Tables. */
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
    attendee_secret     UUID NOT NULL DEFAULT uuid_generate_v4(),
    event_id            BIGINT NOT NULL REFERENCES rsvp_event(id),
    response_id         BIGINT NOT NULL REFERENCES rsvp_response(id)
);