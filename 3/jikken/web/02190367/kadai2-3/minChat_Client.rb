# coding: utf-8
require 'socket'

sock = TCPSocket.new('127.0.0.1', 2000)
loop do
  line = gets
  sock.puts line
end
sock.close
