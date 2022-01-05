#!/usr/bin/env ruby
# coding: utf-8

require 'json'
text = "[1,2,3]"
json = JSON.parse(text)
puts json.size
puts json[0]
text = "{\"red\":1, \"blue\":2, \"green\":3}"
json = JSON.parse(text)
puts json.keys
puts json["red"][0]
