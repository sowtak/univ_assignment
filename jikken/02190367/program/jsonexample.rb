#!/usr/bin/env ruby
# coding: utf-8

require 'json'

text = "[1,2,3]"
json = JSON.parse(text)
puts "json = #{text}"
p json
print "Size of json (#{json.class}) "
puts json.size
print "json[0] = "
puts json[0]
text = "{\"red\":1, \"blue\":2, \"green\":3}"
json = JSON.parse(text)
puts "json = #{text}"
p json
print "keys of json (#{json.class}) "
puts json.keys.join(",")
print "json[\"red\"] = "
puts json["red"]
text = "{\"red\":[1,2,3], \"blue\":{\"a\":2}, \"green\":3}"
json = JSON.parse(text)
puts "json = #{text}"
p json
print "keys of json (#{json.class}) "
puts json.keys.join(",")
print "json[\"red\"] = "
p json["red"]
print "json[\"red\"][1] = "
puts json["red"][1]
print "json[\"blue\"][1] = "
p json["blue"]
print "json[\"blue\"][\"a\"] = "
puts json["blue"]["a"]


