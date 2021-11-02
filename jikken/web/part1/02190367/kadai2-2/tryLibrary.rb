#!/usr/bin/ruby

require 'profile' #Rubyプログラム用のプロファイラライブラリ

total=0 #処理全体にかかった時間

# a, b, cを含む部分文字列を数える
('a'..'zz').each do |seq|
  ['a','b','c'].each do |i|
    if seq.index(i)
      total += 1
      break
    end
  end
end
puts "合計: #{total}"
