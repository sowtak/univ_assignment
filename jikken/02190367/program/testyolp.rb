#!/usr/bin/env ruby
# encoding: utf-8
require './yolp'

yolp = YOLP.new
#puts yolp.coordinate("北海道札幌市北区北１２条西８丁目")
coord = yolp.coordinate("北海道札幌市北区北１４条西９丁目")
puts coord
puts yolp.address(coord)
coord = yolp.coordinate("北海道札幌市北区北１７条西７丁目")
puts coord
puts yolp.address(coord)
#puts yolp.coordinate("北海道札幌市北区北１４条西８丁目")
#puts yolp.address("43.075,141.35")
puts yolp.distance([43.5,135.4],[43.5,135.5])
puts yolp.distance([43.5,135.3],[43.5,135.5])
puts yolp.distance([43.5,135.2],[43.5,135.5])

