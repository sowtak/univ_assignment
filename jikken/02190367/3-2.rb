require 'json'
require 'open-uri'
require 'uri'

require_relative "./yolp.rb"

def change_url(target)
    target=target.gsub(/^http:/,"https:")
    if /\.json/ !~ target
        target+=".json"
    end
end

id=change_url(ARGV[0].chomp)
state=ARGV[1]

app_id="jsqAbSa3aKX49y0tRjEY"

yolp=YOLP.new
state_coord=yolp.coordinate(state.chomp)
state_coord[0]=state_coord[0].round(5).to_f
state_coord[1]=state_coord[1].round(5).to_f

tmp=state_coord[1]
state_coord[1]=state_coord[0]
state_coord[0]=tmp

records=[]

URI.open(id) {|f|
    books_json=JSON.parse(f.read)
    libraries_json=books_json["@graph"][0]["bibo:owner"]

    libraries_json.each {|library|
        library_name=library["foaf:name"]
        library_ID=library["@id"]

        URI.open(change_url(library_ID)) {|library_f|
            library_json = JSON.parse(library_f.read)
            library_address = library_json["@graph"][0]["v:adr"]["v:label"]
            
            library_coord=yolp.coordinate(library_address)
            if library_coord == nil then
                next
            end

            tmp=library_coord[1]
            library_coord[1]=library_coord[0]
            library_coord[0]=tmp

            distance=yolp.distance(state_coord,library_coord)

            info=[library_name,library_address,distance]
            records.push(info)
        }    
    }
}


records=records.sort_by {|a,b,c,| c}

i=0
records.each do |name,address,distance|
    puts "[#{i+1}]"
    print "#{name}"
    puts "#{address}"
    puts ""
    i=i+1
end