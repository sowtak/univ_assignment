require 'webrick'

srv=WEBrick::HTTPServer.new({:DocumentRoot => './',
                             :BindAddress => '127.0.0.1',
                             :Port => 2000 })

messages=Hash.new
idx=0

srv.mount_proc('/write') do |req, res|
  #messages[:idx]=req.query['msg']
  messages.store(:idx.to_s, req.query['msg']) if !req.query['msg'].eql?('ban')
  idx=idx.to_i+1
  puts idx
  res.status=200
  puts "Success"
  res['Content-Type']='text/plain'
end

srv.mount_proc('/index') do |req, res|
  messages.each do |k,_|
    puts "id: #{k.to_i}"
  end
  res.status=200
  res['Content-Type']='text/plain'
end

srv.mount_proc('/read') do |req, res|
  puts messages[req.query['id'].to_s]
  res.status = 200
  res['Content-Type']='text/plain'

end

trap("INT") {srv.shutdown}
srv.start
