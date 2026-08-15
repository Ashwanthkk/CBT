
CREATE DATABASE IF NOT EXISTS cbt;
USE cbt;

CREATE TABLE professors (
    professor_id BIGINT PRIMARY KEY AUTO_INCREMENT,
    profile_id VARCHAR(50) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    university_id BIGINT,
    department_id BIGINT,
    designation VARCHAR(100),
    employee_id VARCHAR(50),
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(30) DEFAULT 'PROFESSOR',
    status VARCHAR(20) DEFAULT 'ACTIVE',
    last_login_at TIMESTAMP NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

