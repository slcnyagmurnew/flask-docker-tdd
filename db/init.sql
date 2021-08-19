CREATE DATABASE IF NOT EXISTS tddflask;
use tddflask;

CREATE TABLE favorite_colors (
  primary key name VARCHAR(20),
  color VARCHAR(10)
);

INSERT INTO favorite_colors
  (name, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');
