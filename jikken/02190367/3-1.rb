require 'json'
require 'open-uri'
require 'uri'

require './yolp'

def change_url(target)
    target=target.gsub(/^http:/,"https:")
    if /\.json/ !~ target
        target+=".json"
    end
end

id=change_url(ARGV[0].chomp)

yolp=YOLP.new
app_id="jsqAbSa3aKX49y0tRjEY"

name=[]
address=[]

URI.open(id) {|f|
    books_json=JSON.parse(f.read)
    libraries_json=books_json["@graph"][0]["bibo:owner"]

    libraries_json.each {|library|
        library_name=library["foaf:name"]
        library_ID=library["@id"]

        URI.open(change_url(library_ID)) {|library_f|
            library_json = JSON.parse(library_f.read)
            library_address = library_json["@graph"][0]["v:adr"]["v:label"]
            
            name.push(library_name)
            address.push(library_address)
        }    
    }
}
coord=yolp.coordinate(address[0])
longitude=coord[0]
latitude=coord[1]

file=File.open("map3-1.html","w")
file.puts '<!DOCTYPE html>'
file.puts '<html lang="ja">'
file.puts '<head>'
file.puts '<meta charset="utf-8">'
file.puts '<title>map3-1.html</title>'
file.puts '<script type="text/javascript" src="iframe.js?var=1.0"></script>'
file.puts '</head>'
file.puts '<body>'
file.puts '<h1>地図を表示</h1>'
file.puts '<div style="float:left;">'
file.puts '<iframe width="800" height="600" frameborder="0" scrolling="no"mar\
ginheight="0" marginwidth="0"'
file.print 'src="https://www.openstreetmap.org/export/embed.html?bbox='
file.print "#{longitude}%2C#{latitude}%2C#{longitude}%2C#{latitude}&amp;layer\
=mapnik&amp;marker=#{latitude}%2C#{longitude}"
file.puts '"'
file.puts 'style="border: 1px solid black" name="map"></iframe>'
file.puts '</div>'
file.print '<h2>'
file.print name[0]
file.puts '</h2>'
file.print '<h3>'
file.print address[0]
file.puts '</h3>'
file.print '<h4>緯度: '
file.print coord[1]
file.print '　経度: '
file.print coord[0]
file.puts '</h4>'
file.puts '</body>'
file.puts '</html>'
file.close
