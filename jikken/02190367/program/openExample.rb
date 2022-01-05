#!/usr/bin/env ruby
# encoding: utf-8
require "open-uri"

baseidURL = ARGV.shift or exit

# http:で始まっている場合は、https:に書き直す。
target = baseidURL.gsub(/^http:/, "https:")

# .jsonで終わっていないときには、.jsonを追加する。
if /\.json/ !~ target 
  target += ".json"
end

# open-uriのライブラリを読み込んでいると、open()の引数にURIを与えると、
# 中身を読み出すためのストリームが開かれるので、readをすれば、中身が得られる。
open(target){|f|
  puts f.read
}
