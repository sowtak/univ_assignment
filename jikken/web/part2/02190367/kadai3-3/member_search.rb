#coding: utf-8
require 'sqlite3'
db=SQLite3::Database.new("sandbox.db")
name=gets.chomp
lab_id=0
lab_mates={}
db.execute("SELECT lab_id FROM lab_members WHERE member_name = ?", [name]) do |lab_id| 
  lab_mates = db.execute("SELECT member_name FROM lab_members WHERE lab_id = ? AND member_name != ?", [lab_id], [name])
end
puts lab_mates
db.close

