#coding: utf-8
require 'sqlite3'
db=SQLite3::Database.new("sandbox.db")
lab_name=gets.chomp
member_names=Array.new
db.execute("SELECT member_name FROM lab_members INNER JOIN labs ON labs.id = lab_members.lab_id WHERE lab_name = ?", [lab_name]) do |member_name|
  member_names.push(member_name)
end
puts member_names
db.close
