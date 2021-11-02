#coding: utf-8
require 'sqlite3'
db=SQLite3::Database.new("sandbox.db")
lab_name=gets.chomp
member_names={}
db.execute("SELECT id FROM labs WHERE lab_name = ?", [lab_name]) do |lab_id|
  member_names = db.execute("SELECT member_name FROM lab_members WHERE lab_id = ?", [lab_id])
end
puts member_names
db.close
