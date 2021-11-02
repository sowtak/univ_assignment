# coding: utf-8
require 'socket'

sock=TCPServer.new 2000

client=sock.accept
loop do
  line = client.gets.chomp 
  if line.eql?('bye')
    break
  else 
    puts line
  end
end
client.close
