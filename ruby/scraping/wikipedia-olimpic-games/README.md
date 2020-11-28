_Scraper_ de la lista de juegos olímpicos del artículo de Wikipedia

[Este](https://en.wikipedia.org/wiki/List_of_Olympic_Games_host_cities) es el artículo.

1. Usamos la clase [`Net::HTTP`](https://ruby-doc.org/stdlib-2.7.2/libdoc/net/http/rdoc/Net/HTTP.html) en `fetch.rb` para descargar el HTML:

`ruby fetch_html.rb | > List_of_Olympic_Games_host_cities.html`

[`Net::HTTP`] permite construir un HTTP _user agent_ (_a characteristic string that lets servers and network peers identify the application, operating system, vendor, and/or version of the requesting user agent._). Permite hacer peticiones HTTP y obtener la respuesta.