#coding: utf-8

require 'sinatra'
require 'sinatra/reloader'
require 'active_record'

ActiveRecord::Base.establish_connection(
  adapter: "sqlite3",
  database: "sandbox.db"
)

class Lab < ActiveRecord::Base
end

class LabMember < ActiveRecord::Base
end

get '/' do 
  @title = 'Hello, world!'
  @world = 'WORLD!'
  erb :index
end

get '/lab_search' do
  if !Lab.where(:lab_name => params[:lab_name]).empty?
    @lab = Lab.where(:lab_name => params[:lab_name])
    @lab_members = LabMember.where(:lab_id => @lab.id)
  else
    redirect '/'
  end
  erb :lab_search
end

get '/member_search' do
  if !Lab.where(:member_name => params[:member_name]).empty?
    @lab = Lab.where(:member_name => params[:member_name])
    @lab_members = LabMember.where(:lab_name => @lab.lab_name)
  else
    redirect '/'
  end
end