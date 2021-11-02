CREATE TABLE student_records(
  id integer PRIMARY KEY,
  student_id integer,
  klass text,
  score integer,
  grade text);

CREATE TABLE students(
  student_id integer PRIMARY KEY,
  name text
);

.separator , 

.import student_records.csv student_records
.import students.csv students
