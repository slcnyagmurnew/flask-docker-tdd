CREATE DATABASE IF NOT EXISTS tddflask;
use tddflask;

CREATE TABLE favorite_colors (
  name VARCHAR(20),
  color VARCHAR(10),
  Primary Key (name)
);

INSERT INTO favorite_colors
  (name, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');
