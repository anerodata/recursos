# Regular expressions

## `grep`

Con `grep` podemos filtrar y así podríamos buscar todas las lineas que empiecen por "amp" `grep -Po '(?<=amp).*' los40.html`.
- `grep -iw 'empleo' files/mocion-de-censura.html` devuelve todas las líneas en las que sale la palabra empleo en mayúsculas o minúsculas (`-i`). Sin `-w` también saldría subempleo.wq



