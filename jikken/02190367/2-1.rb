require 'json'
require 'open-uri'

str=ARGV[0].chomp
app_id="jsqAbSa3aKX49y0tRjEY"

URI.open("https://ci.nii.ac.jp/books/opensearch/search?title=#{str}&format=json&appid=#{app_id}") { |x| 
    json=JSON.parse(x.read)
    items=json["@graph"][0]["items"]
    puts ""

    i=1

    items.each {|item|
        puts "[#{i}]"
        puts "#{item["title"]}"
        puts "(#{item["link"]["@id"]})"
        puts ""
        i=i+1
        
        if i>20 then
            break
        end
    }
}