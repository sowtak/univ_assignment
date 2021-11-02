require 'webrick'

srv=WEBrick::HTTPServer.new({:DocumentRoot => './',
                             :BindAddress => '127.0.0.1',
                             :Port => 2000 })
srv.mount('/time', WEBrick::HTTPServlet::FileHandler, './time.html')
srv.mount_proc('/fizzbuzz') do |req, res|
  res.body+="<html><meta charset='utf-8'><body>"
  for n in 1..req.query['num'].chomp.to_i
    res.body+="<table border=1><tr>
      <td>#{n}</td>
      <td> #{ 'Fizz ' if n % 3 == 0}#{ 'Buzz' if n % 5 == 0}#{'     ' if n%5!=0 and n%3!=0}  </td>
    </tr></table>"
  end
  res.status=200
  res['Content-Type']='text/html'
end
trap("INT") {srv.shutdown}
srv.start
