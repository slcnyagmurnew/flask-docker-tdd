CREATE DATABASE IF NOT EXISTS tddflask;
use tddflask;

CREATE TABLE favorite_colors (
  name VARCHAR(20) PRIMARY KEY,
  color VARCHAR(10)
);

INSERT INTO favorite_colors
  (name, color)
VALUES
  ('Lancelot', 'blue'),
  ('Galahad', 'yellow');
