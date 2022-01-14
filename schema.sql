DROP TABLE IF EXISTS directors;
DROP TABLE IF EXISTS films;

CREATE TABLE films (
  id SERIAL PRIMARY KEY,
  title_en VARCHAR(255),
  title_hu VARCHAR(255),
  year INTEGER,
  was_banned BOOLEAN,
  directed_by INTEGER,
  restored BOOLEAN,
  is_documentary BOOLEAN
);

CREATE TABLE directors (
  id SERIAL PRIMARY KEY,
  director_id INTEGER,
  name VARCHAR(255),
  birth VARCHAR(255)
);