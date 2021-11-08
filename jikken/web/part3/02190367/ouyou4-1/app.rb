# coding: utf-8
require "time"
require 'sinatra'
require 'sinatra/reloader'
require 'active_record'


ActiveRecord::Base.establish_connection(
    adapter: 'sqlite3',
    database: 'bulletin_board.db'
)

class Account < ActiveRecord::Base
end

class Message < ActiveRecord::Base
end

get '/' do
  @title = 'ログインフォーム'
  @world = ''
  erb :index
end

get '/r' do
  @title = 'ログインフォーム'
  @world = 'ログインに失敗しました'
  erb :index
end

post '/judge' do
  if !Account.where(:name => params[:name], :password => params[:password]).empty?
    @title = '掲示板'
    @message = Message.all
    @username = params[:name]
    erb :login
  else
    redirect '/r'
  end
end

post '/message' do
  t = Time.new
  now = t.strftime("%Y/%m/%d")
  Message.create(:date => now, :name => params[:name], :message => params[:message])

  @title = '掲示板'
  @message = Message.all
  erb :login
end
