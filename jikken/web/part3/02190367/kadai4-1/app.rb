#coding: utf-8

require 'sinatra'
require 'sinatra/reloader'
require 'active_record'

ActiveRecord::Base.establish_connetcion(
  adapter: 'sqlite3'
  database: 'seiseki.db'
)

class StudentRecord < ActiveRecord::Base
end

get '/' do 
  @title = 'Hello, world!'
  @world = 'world!'
  erb :index
end

get '/lab_search' do
  @lab_name = params['lab_name']
  erb :lab_search
end

get '/member_search' do 
  @member_name = params['member_name']
  erb :member_search

get '/seiseki/' do
  @title = 'Seiseki view'
  @students = StudentRecord.all
  erb :seiseki
end

