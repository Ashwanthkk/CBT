CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,

    profile_id VARCHAR(20) NOT NULL UNIQUE,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(255) NOT NULL UNIQUE,

    phone_number VARCHAR(15),

    university_id INT,

    department_id INT,

    course VARCHAR(100),

    semester INT,

    roll_number VARCHAR(50) UNIQUE,

    password_hash VARCHAR(255) NOT NULL,

    status ENUM('ACTIVE', 'INACTIVE') DEFAULT 'ACTIVE',

    last_login_at DATETIME NULL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
) AUTO_INCREMENT = 1000;
