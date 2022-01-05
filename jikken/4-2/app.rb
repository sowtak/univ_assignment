require 'json'
require 'open-uri'
require 'uri'

require 'sinatra'
require 'sinatra/reloader'
require 'active_record'

require './yolp.rb'

def change_url(target)
    target=target.gsub(/^http:/, "https:")
    if /\.json/ !~ target
        target+=".json"
    end
end


get '/' do
    erb :index
end

post '/search' do
    yolp = YOLP.new
    id=change_url(params[:ID])
    appID="jsqAbSa3aKX49y0tRjEY"

    library_names=[]
    library_addresses=[]
    longitudes=[]
    latitudes=[] 

    URI.open(id) { |f|
        books=JSON.parse(f.read)
        libraries_json=books["@graph"][0]["bibo:owner"]
    
        libraries_json.each { |library|
            library_name=library["foaf:name"]
            library_id=library["@id"]

            URI.open(change_url(library_id)) { |library_f|
                library_json = JSON.parse(library_f.read)
                library_address = library_json["@graph"][0]["v:adr"]["v:label"]

                library_names.push(library_name)
                library_addresses.push(library_address)
            }
        }
    }
  

    for address in library_addresses do
        coord = yolp.coordinate(address)
        #エラー処理
        if coord == nil then
            next
        end
        
        longitudes.push(coord[0])
        latitudes.push(coord[1])
    end
  
    @longitudes = longitudes
    @latitudes = latitudes
    @library_names = library_names

    erb :search
end

post '/result' do
    str=params[:str]
    appID="jsqAbSa3aKX49y0tRjEY"

    titles=[]
    bookid=[] 
    URI.open("https://ci.nii.ac.jp/books/opensearch/search?title=#{CGI.escape(str)}&format=json&appid=#{appID}") { |f|
        json = JSON.parse(f.read)
        items = json["@graph"][0]["items"]
        
        i = 1
        items.each { |item|
            titles.push(item["title"])
            bookid.push(item["link"]["@id"])
          
            if i>20 then
                break
            end
        }
    }

    @titles = titles
    @bookids = bookid

    erb :result
end
