# Expresiones Regulares

Este [artículo](https://www.cyberciti.biz/faq/grep-regular-expressions/) explica algunas. Este [otro](https://regexone.com/lesson/) incluye ejemplos prácticos

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

- `[[:alnum:]]` – Alphanumeric characters.
- `[[:alpha:]]` – Alphabetic characters
- `[[:blank:]]` – Blank characters: space and tab.
- `[[:digit:]]` – Digits: ‘0 1 2 3 4 5 6 7 8 9’.
- `[[:lower:]]` – Lower-case letters: ‘a b c d e f g h i j k l m n o p q r s t u v w x y z’.
- `[[:space:]]` – Space characters: tab, newline, vertical tab, form feed, carriage return, and space.
- `[[:upper:]]` – Upper-case letters: ‘A B C D E F G H I J K L M N O P Q R S T U V W X Y Z’.
- `grep [[:digit:]] files/mocion-de-censura.html` Encontraría todos los caracteres numéricos

### Negación grupal

- `grep '[aB]ascal[^0-9]' files/mocion-de-censura.html` encuentra abascal y Abascal, pero no abascal1. Porque los números se ignoran.

### _Wildcards_

Se puede usar `.` para reemplazar caracteres

- `grep '\<S.....z\>' files/mocion-de-censura.html`: Encontraría todo lo que empieze y termine por esas letras
- `grep '^..$' files/mocion-de-censura.html` Encuentra todas las líneas con dos caracteres
- `grep '^\.[0-9]' file.html` Encuentra las líneas con un punto y un número. `\.` escapa el punto. Ya que el punto coincide con cualquier caracter.  

### `egrep` o `grep -E`

Los patrones son expresiones regulares

- `egrep [[:digit:]]{4} files/mocion-de-censura.html` busca cuatro dígitos juntos.
- `egrep word1|word2 files/mocion-de-censura.html`: una palabra o la otra. Es lo mismo que `egrep 'word1\|word2' files/mocion-de-censura.html`.

### Secuencias

- `grep -E A{1} files/mocion-de-censura.html` encuentra todas las líneas con A una vez
- `grep -E A{,3} files/mocion-de-censura.html` encuentra todas las líneas con A tres veces
- `grep -E 's{,2}' files/mocion-de-censura.html` encuentra la s una o dos veces. Sería igual que `grep 's\{,2\}' files/mocion-de-censura.html`
- `grep -E 's{2,4}' files/mocion-de-censura.html` encuentra la s dos, tres o cuatro veces.
- `grep -E 'co{1,2}l' files/mocion-de-censura.html` encuentra col o cool.

### Contar

`grep -c Abascal files/mocion-de-censura.html` Cuenta cuántas veces sale Abascal (161).

## Expresiones regulares en [RegexOne](https://regexone.com/lesson/)

Son patrones que buscan atajar partes de un texto.

El índice de caracteres básicos de la web de [RegexOne](https://regexone.com/lesson/) es el siguiente:

|Character|Meaning|
|---|---|
|abc…|Letters|
|123…|Digits|
|\d|Any Digit|
|\D|Any Non-digit character|
|.|Any Character|
|\\.|Period|
|[abc]|Only a, b, or c|
|[^abc]|Not a, b, nor c|
|[a-z]|Characters a to z|
|[0-9]|Numbers 0 to 9|
|\w|Where the w stands for “word character,” will match any letter, number or the
underscore.|
|\W|Any Non-alphanumeric character|
|{m}|m Repetitions|
|{m,n}|m to n Repetitions|
|*|Zero or more repetitions|
|+|One or more repetitions|
|?|Optional character|
|\s|Will match any white space character including the vanilla space, the tab, and
the newline|
|\S|Any Non-whitespace character|
|^…$|Starts and ends|
|(…)|Capture Group. Set characters off from the rest of the pattern|
|(a(bc))|Capture Sub-group|
|(.*)|Capture all|
|(abc\|def)|Matches abc or def|
|\||Alternatives: A\|B will match either A or B|

\d\d:\d\d (AM|PM)

`Any string that starts with two digits, followed by a colon, followed by two more digits, followed by a space, followed by either AM or PM .`

- `\d` busca un dígito del 0 al 9.
- `.` coincide con cualquier caracter. Si quisiéramos omitirlo tendríamos que escaparlo como he comentado arriba.
- `[]` sirve para buscar coincidencias con unos caracteres determinados `[cmf]` por ejemplo ligaría con can, man y fan. Pero no con dan, ran o pan, porque no tiene ni un caracter-
- `[^bog]`. El corcherte con el circunflejo sirve para descartar. Es decir, esa expresión regular ligaría con cualquier texto que no tuviera ninguno de esos caracteres
- `[A-C]` ligaría con Abc pero no con abc ya que tiene una A. Es una forma'de secuenciar caracteres. Con el guión expresamos series. `[A-Za-z0-9ñ]` Coincidiría con cualquier caracter alfanumérico. es igual que hacer `\w`.
- `z{3,5}`: repeticiones. En el ejemplo, una z entre 3 y 5 veces. Matchearía con "wazzzzzup", o "wazzzup", pero no con wazzup. Se puede usar en combinación con cualquier otro caracter especial. _For example `w{3}` (three w's), `[wxy]{5}` (five characters, each of which can be a w, x, or y) and `.{2,6}` (between two and six of any character)_.
- `a*[bc]+`: _Kleene Star and Kleene Plus_. La estrella busca la "a" 0 o infintias veces a continuación. El más, 1 o infinitas veces a continuación. `\d+` Coincidiría con un número e infinitas veces a continuación (25 o 25000).
- `?`: Busca opcionalmente un caracter.

>_This metacharacter allows you to match either zero or one of the preceding character or group_.

Por ejemplo `found\??` coincidiría con found? y con found. _`ab?c` will match either the strings "abc" or "ac"_.

- `\s`: Espacios.

>_The most common forms of whitespace you will use with regular expressions are the space ( ), the tab (\t), the new line (\n) and the carriage return (\r) (useful in Windows environments), and these special characters match each of their respective whitespaces. In addition, a whitespace special character `\s` will match any of the specific whitespaces above and is extremely useful when dealing with raw input text._

- `^...$`: Comienzo y final. Se usa mucho para evitar falsos positivos. Combinados los dos se puede hacer una expresión regular que coincida con una línea entera o parrafo de principio a final.

Por ejemplo: `^Mission. successful$` puede servir para encontrar un párrafo o línea que empiece y acabe por ambas palabras con cualquier caracter entre medias.

- `(...)`: grupos. Sirve para capturar una información dentro de un patrón. Cuándo introduces una parte de la expersión entre paréntesis, la aíslas del resto de la expresión. 

Por ejemplo `^(file.*)\.pdf$`. Lo que hay dentro de los paréntesis captura todo lo que empiece con "file" hasta el ".pdf". Es decir:  `file_record_transcript` o ` file_20200312`. 

Lo que hay fuera del paréntesis determina el final de la coincidencía y lo que no quedaría capturado: `.pdf`. `testfile_fake.pdf.tmp` quedaría fuera del patrón y por lo tanto de la captura.

- `(a(bc))`: subgrupos. En ocasiones puede ser necesario extraer diferentes capas dentro de un patrón en concreto. Generalmente van el orden de extracción es el siguiente: la primera parte en ser capturada es la más amplia y dentro de sus paréntesis se define de nuevo una segunda parte con otros dos paréntesis. 

Por ejemplo `(\D*(\d*))` capturaría dentro de la fecha `Jan 2019` los dos siguientes grupos `Jan 2019` y `2019` de cara a extraer ambos datos de manera independiente dentro de una lista de fechas o dentro de un texto. Dentro de un texto, la expresión coincidiría con `Jan 2019`

>_If I knew that a phone number may or may not contain an area code, the right pattern would test for the existence of the whole group of digits (\d{3})? and not the individual characters themselves (which would be wrong)._

En un supuesto en el que quisieramos el número de telefóno sin ningún prefijo.