BEGIN;

CREATE TABLE noah.hello(
   hello_id serial PRIMARY KEY,
   world VARCHAR (255) UNIQUE NOT NULL
);

COMMIT;
