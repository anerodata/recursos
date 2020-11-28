# TODO: Should have a program that fetch a particular HTML
# article of Wikipedia.

require 'net/http'
uri = URI('https://en.wikipedia.org/wiki/List_of_Olympic_Games_host_cities')

# Request the data with Net::HTTP class
res = Net::HTTP::get_response(uri)
puts res.body if res.is_a?(Net::HTTPSuccess)