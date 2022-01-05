#!/usr/bin/env ruby
# coding: utf-8

require 'json'

def usage
  STDERR.puts "ruby testjson.rb <jsonfile>"
end

filename = ARGV.shift or usage

open(filename, "r"){|f|
  json = JSON.parse(f.read)
  p json
  begin
    puts json.keys
  rescue
    puts json.join("::")
  end
}



