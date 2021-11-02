#encoding: utf-8
require 'sqlite3'
db = SQLite3::Database.new("sandbox.db")
id, new_name = gets.chomp.split(",")
str = "UPDATE students SET name = \"#{new_name}\" WHERE student_id = #{id}"
db.execute_batch(str)
db.close

