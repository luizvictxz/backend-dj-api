CREATE TABLE student(
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(254) NOT NULL,
    cpf VARCHAR(11) NOT NULL UNIQUE,
    date_into DATE NOT NULL
);

CREATE TABLE course(
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    workload INTEGER NOT NULL,
    registration_fee DECIMAL(10, 2) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE registration(
    id SERIAL PRIMARY KEY,
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(10) NOT NULL DEFAULT 'PENDENT',

    CONSTRAINT fk_student FOREIGN KEY (student_id) REFERENCES student(id),
    CONSTRAINT fk_course FOREIGN KEY (course_id) REFERENCES course(id),

    CONSTRAINT unique_registration UNIQUE (student_id, course_id)

)