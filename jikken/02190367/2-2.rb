require 'json'
require 'open-uri'

def change_url(target)
    target=target.gsub(/^http:/,"https:")
    if /\.json/ !~ target
        target+=".json"
    end
end

id=change_url(ARGV[0].chomp)
app_id="jsqAbSa3aKX49y0tRjEY"

name=[]
address=[]

URI.open(id) {|x|
    books_json=JSON.parse(x.read)
    libraries_json=books_json["@graph"][0]["bibo:owner"]

    libraries_json.each {|library|
        library_name=library["foaf:name"]
        library_ID=library["@id"]

        URI.open(change_url(library_ID)) {|library_f|
            library_json=JSON.parse(library_f.read)
            library_address=library_json["@graph"][0]["v:adr"]["v:label"]

            name.push(library_name)
            address.push(library_address)
        }
    }
}

name.zip(address).each do |name, address|
    print "#{name}"
    puts "#{address}"
    puts ""
end