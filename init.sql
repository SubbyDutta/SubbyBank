CREATE DATABASE IF NOT EXISTS fraud_db;

USE fraud_db;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL
);

INSERT INTO users (username, password, role)
VALUES ('admin', '$2a$12$Zhsbs5pHoTlw.N7ik82KguBiJgwO0egmJBGOgDVP9vcZX9ssd0Ozu', 'ADMIN');