#coding: utf-8
require 'sqlite3'
db = SQLite3::Database.new("sandbox.db")
db.execute("CREATE TABLE students(name char, student_id integer);")
db.execute("INSERT INTO students(name, student_id) VALUES('田所浩二', 810);")
db.execute("SELECT * FROM students;") do |row|
  puts row.join(",")
end
db.close
