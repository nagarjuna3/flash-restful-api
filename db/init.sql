CREATE DATABASE headers;
use headers;

CREATE TABLE  uuid (id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY, uuid text NOT NULL , body text, created DATETIME);

INSERT INTO uuid
  (uuid, id, body, created)
VALUES
  ('G5G74W', 1, 'body-1abc', 2017-05-26),
  ('G5G74E', 2, 'body-1xyz', 2017-05-25);
