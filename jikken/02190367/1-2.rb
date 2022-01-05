require './yolp.rb'

yolp=YOLP.new
address=ARGV[0].chomp
name=ARGV[1]

coord=yolp.coordinate(address)
longitude=coord[0]
latitude=coord[1]

file=File.open("map.html","w")
file.puts '<!DOCTYPE html>'
file.puts '<html lang="ja">'
file.puts '<head>'
file.puts '<meta charset="utf-8">'
file.puts '<title>kadai1-2.html</title>'
file.puts '<script type="text/javascript" src="iframe.js?var=1.0"></script>'
file.puts '</head>'
file.puts '<body>'
file.puts '<h1>地図を表示</h1>'
file.puts '<div style="float:left;">'
file.puts '<iframe width="800" height="600" frameborder="0" scrolling="no"marginheight="0" marginwidth="0"'
file.print 'src="https://www.openstreetmap.org/export/embed.html?bbox='
file.print "#{longitude}%2C#{latitude}%2C#{longitude}%2C#{latitude}&amp;layer=mapnik&amp;marker=#{latitude}%2C#{longitude}"
file.puts '"'
file.puts 'style="border: 1px solid black" name="map"></iframe>'
file.puts '</div>'
file.print '<h2>'
file.print address
file.puts '</h2>'
file.print '<h2>'
file.print name
file.puts '</h2>'
file.puts '</body>'
file.puts '</html>'
file.close