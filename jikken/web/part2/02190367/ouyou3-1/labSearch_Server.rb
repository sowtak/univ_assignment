#coding: utf-8
require 'webrick'
require 'sqlite3'

srv=WEBrick::HTTPServer.new({:DocumentRoot => './',
                             :BindAddress => '127.0.0.1',
                             :Port => 2000})
srv.mount_proc('/lab_search') do |req, res|
  db=SQLite3::Database.new("sandbox.db")
	member_names={}
  lab_name=req.query['lab_name']
	db.execute("SELECT id FROM labs WHERE lab_name = ?", [lab_name]) do |lab_id|
	  member_names = db.execute("SELECT member_name 
                              FROM lab_members 
                              WHERE lab_id = ?", [lab_id])
	end
  res.body+="<html><meta charset='utf-8'><body>\n"
  for name in member_names
    res.body+="<p>#{name}</p>"
  end
  res.body+="</body></html>"
	db.close
  res.status=200
  res.content_type='text/html'
end

srv.mount_proc('/member_search') do |req, res|
  db=SQLite3::Database.new("sandbox.db")
  name=req.query['member_name']
	lab_id=0
	lab_mates={}
	db.execute("SELECT lab_id 
            FROM lab_members 
             WHERE member_name = ?", [name]) do |lab_id| 
	  lab_mates = db.execute("SELECT member_name 
                           FROM lab_members 
                           WHERE lab_id = ? 
                           AND member_name != ?", [lab_id], [name])
  end
  res.body+="<html><meta charset='utf-8'><body>\n"
  for name in lab_mates
    res.body+="<p>#{name}</p>"
  end
  res.body+="</body></html>"
  res.status=200
  res.content_type="text/html"
	db.close
end


trap("INT") {srv.shutdown}
srv.start
