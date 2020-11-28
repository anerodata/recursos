require 'nokogiri'
doc = Nokogiri::HTML(open('List_of_Olympic_Games_host_cities.html', 'r:UTF-8'))
table = doc.css('table')[2]