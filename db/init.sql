CREATE DATABASE IF NOT EXISTS tddflask;
use tddflask;

CREATE TABLE favorite_colors (
  name VARCHAR(20) NOT NULL,
  color VARCHAR(10) NOT NULL,
  Primary Key(name)
);

INSERT INTO favorite_colors
  (name, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');
