# coding: utf-8

require 'sinatra'
require 'sinatra/reloader'
require 'active_record'
require './yolp'
require 'open-uri'
require 'json'
require 'uri'

def change_url(target)
    target=target.gsub(/^http:/, "https:")
    if /\.json/ !~ target
        target+=".json"
    end
end

get '/search' do
    erb :search
end

get '/result' do
    yolp = YOLP.new
    id = change_url(params[:id]) 
    appID = "jsqAbSa3aKX49y0tRjEY"
  
    library_names = [] 
    library_addresses = []
    longitudes = [] 
    latitudes = [] 
  
    URI.open(id) { |f|
        books_json = JSON.parse(f.read)
        libraries_json = books_json["@graph"][0]["bibo:owner"]
    
        libraries_json.each { |library|
            library_name = library["foaf:name"]
            library_id = library["@id"]

            URI.open(change_url(library_id)) { |library_f|
                library_json = JSON.parse(library_f.read)
                library_address = library_json["@graph"][0]["v:adr"]["v:label"]
            
                library_names.push(library_name)
                library_addresses.push(library_address)
                puts library_name
            }
        }
    }
    for address in library_addresses do
      
      coord = yolp.coordinate(address)
      
      if coord == nil then
        next
      end
      
      longitudes.push(coord[0])
      latitudes.push(coord[1])
    end
    
    @longitudes = longitudes
    @latitudes = latitudes 
    @library_names = library_names 

    erb :result
end

