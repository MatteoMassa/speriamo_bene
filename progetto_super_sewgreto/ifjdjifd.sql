CREATE TABLE IF NOT EXISTS persone 
(
    id INTEGER, 
    name TEXT, 
    age DATE, 
)


CREATE TABLE IF NOT EXISTS economic
(
    id INTEGER, 
    salary TIMESTAMP, 
    Job TEXT, 
    persona_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY (persona_id) REFERENCES persone(id)
);
