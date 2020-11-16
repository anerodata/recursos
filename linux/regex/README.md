# Regular expressions

Este [artículo](https://www.cyberciti.biz/faq/grep-regular-expressions/) explica algunas.

## `grep`

Con `grep` podemos filtrar y así podríamos buscar todas las lineas que empiecen por "amp" `grep -Po '(?<=amp).*' los40.html`.

### Ejemplos básicos

- `grep -iw 'empleo' files/mocion-de-censura.html` devuelve todas las líneas en las que sale la palabra empleo en mayúsculas o minúsculas (`-i`). Sin `-w` también saldría subempleo.
- `grep -iwE 'abascal|arrimadas|IGLESIAS' files/mocion-de-censura.html` devuelve todas las líneas con algunas de esas palabras. `-E` significa _extended expresion_.
- `grep 'Señor...' files/mocion-de-censura.html`. Coincidiría con Señor y con tres caracteres más. El punto es cualquier caracter, pero si quisiéramos matchear con un punto? Lo haríamos así `grep '\.' file.html`

### _Anchors_

- `grep '^<' files/mocion-de-censura.html` filtra todas las líneas que empiecen por '<'.
- `grep -w '^$' files/mocion-de-censura.html` Todas las líneas vacías.
- `grep -w '^Abascal$' files/mocion-de-censura.html` las líneas que solo contengan Abascal.

### _Grupos de caracteres_

- `grep [aA]hí files/mocion-de-censura.html` el `[]` sirve para acotar caracteres. Es decir, encontrar ahí o Ahí
- `grep [A-Z]bascal files/mocion-de-censura.html` definimos rangos. Es decir, Abascal y Obascal coincidirían aquí. `grep [1-9]bascal files/mocion-de-censura.html` pillaría 1bascal

Las clases se definen de la siguiente manera:

- [[:alnum:]] – Alphanumeric characters.
- [[:alpha:]] – Alphabetic characters
- [[:blank:]] – Blank characters: space and tab.
- [[:digit:]] – Digits: ‘0 1 2 3 4 5 6 7 8 9’.
- [[:lower:]] – Lower-case letters: ‘a b c d e f g h i j k l m n o p q r s t u v w x y z’.
- [[:space:]] – Space characters: tab, newline, vertical tab, form feed, carriage return, and space.
- [[:upper:]] – Upper-case letters: ‘A B C D E F G H I J K L M N O P Q R S T U V W X Y Z’.
- `grep [[:digit:]] files/mocion-de-censura.html` Encontraría todos los caracteres numéricos

#### Negación grupal

- `grep '[aB]ascal[^0-9]' files/mocion-de-censura.html` encuentra abascal y Abascal, pero no abascal1. Porque los números se ignoran.


