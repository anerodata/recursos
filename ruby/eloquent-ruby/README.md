# _Eloquent Ruby_

Notas sobre el libro de 2011 escrito por Russ Oslen para Addison-Wesley Professional. Está en la web de [O'Reilly](https://www.oreilly.com/library/view/eloquent-ruby/9780321700308/).

>  It’s easy to write “correct” Ruby code. But it’s far harder to gain the fluency needed to write great Ruby code. To do that, you need to go beyond syntax and absorb the “Ruby way” of thinking and problem solving. In Eloquent Ruby, Russ Olsen helps you understand Ruby like true Rubyists do—so you can leverage its immense, surprising power.
Olsen draws on years of experience internalizing the Ruby culture and teaching Ruby to other programmers. He guides you to the “Ah Ha!” moments when it suddenly becomes clear why Ruby works the way it does and how you can take advantage of its unique approach.
Eloquent Ruby starts small, answering tactical questions focused on a single statement, method, test, or bug. You’ll learn how to write code that actually looks like Ruby (not Java); why Ruby has so many control structures; how to use strings, expressions, and symbols; and what dynamic typing is really good for.

## 1. Convenciones de Ruby

Aquí un ejemplo de clase en Ruby:

```
# A class

class Document
  attr_accessor :title, :author, :content

    def initialize(title, author, content)
      @title = title
      @author = author
      @content = content
    end

    def words
      @content.split
    end

    def word_count
      words.size
    end
  end
```

Algunas convenciones de Ruby:

- Código **claro y conciso**
- **Identaciones con 2 espacios**, no con tabuladores ya que los espacios siempre tienen el mismo valor. Los tabuladores pueden valer diferentes números en función del usuario.
- Los **comentarios** empiezan por `#`. Los comentarios son _how to_. Explican cómo se usa cuando sea necesario. También para explicar _background_ del código (autor), o cómo funciona un código en concreto. En ambos casos tienen que ser independientes de los _how to comments_.

```
# Using ngram analysis, compute the probability
# that this document and the one passed in were
# written by the same person. This algorithm is
# known to be valid for American English and will
# probably work for British and Canadian English.
#
def same_author_probability( other_document )
  # Implementation left as an exercise for the reader...
end
```

Los comentarios también se pueden poner sobre el código o a continuación de la línea.
- **Nombres**: _`CamelCase` for classes `snakes_everywhere_else`_. Las constantes `PUEDEN_IR_ASÍ`.
- **Paréntesis**: suelen envolver los parámetros de los métodos cuando hay parámetros por claridad, aunque no hacen falta ni en la declaración ni en la llamada. Si no hay, no se ponen:

```
def words 
  @content.split
end
```

`puts`, que es parecido al `print` de Python, tampoco lleva paréntesis `puts 'Hello world'`. Los condicionales y _control statements_ no llevan paréntesis:

```
if words.size < 100
  puts 'The document is not very long.'
end
```

- **Líneas**: Cada línea es para una sentencia, aunque se pueden escribir más de una separada por `;`. No se suele hacer, menos para definir clases o métodos muy sencillos o vacíos

```
class DocumentException < Exception; end

def method_to_be_overriden; end
```

- **Bloques de código**: si es una sentencia, puede ir en una línea `10.times { |n| puts "The number is #{n}" }`. Pero si no, conviene que vaya en varias así:

```
10.times do |n|
  puts "The number is #{n}"
  puts "Twice the number is #{n*2}"
end
```

Estas convenciones están sometidas al principio de **fácil lectura y claridad**, por eso no son fijas y hay que aplicarlos con pragmatismo. Se pueden ver algunas de estas convenciones en el código de ruby, en la clase `set.rb` por ejemplo.

## 2. Estructuras de control

### `If`, `if not`, `unless`, `while`, `until`

Un ejemplo con `if not`:

```
def title=( new_title )
  if not @writable
    @title = new_title
  end
end
```

El mismo con `unless`, más simple. Solo se ejecuta si la sentencia es falsa:

```
def title=( new_title )
  unless @writable
    @title = new_title
  end
end
```

Existe una equivalencia para los bucles `while`

```
while ! document.printed?
  document.print_next_page
end
```

Y es `until`

```
until document.printed?
  document.print_next_page
end
```

Existe la forma _modifier_ (_Do this if that._).

`@title = new_title if @writable`
`@title = new_title unless @read_only`

### `for`, `each`

Existe el bucle `for`. Se parece al de Python:

```
fonts = [ 'courier', 'times roman', 'helvetica' ]
for font in fonts
  puts font
end
```

Pero por debajo utiliza `each`, así que se prefiere quitar una capa y usarlo directamente así:

```
fonts.each do |font|
  puts font
end
```

### `case`

El equivalente a `switch` en otros lenguajes.

```
case title
when 'War And Peace'
  puts 'Tolstoy'
when 'Romeo And Juliet'
  puts 'Shakespeare'
else
  puts "Don't know"
end

```

Se puede usar para el valor que computa:

```
author = case title
  when 'War And Peace'
    'Tolstoy'
  when 'Romeo And Juliet'
    'Shakespeare'
  else
    'Don't know'
end
```

Y de una manera más compacta:

```
author = case title
  when 'War And Peace' then 'Tolstoy'
  when 'Romeo And Juliet' then  'Shakespeare'
  else "Don't know"
  end
```

Podría ir sin el `end`, en cuyo caso, el valor asignado en ese caso sería `nil`. En definitiva, esta expresión se puede usar para retornar un valor. Las comparaciones equivalen a realizarlas con `===`. Se puede usar para identificar instancias de una clase. O para detectar una coincidencia con una expresión regular:

```
case title
when /War And .*/
  puts 'Maybe Tolstoy?'
when /Romeo And .*/
  puts 'Maybe Shakespeare?'
else
  puts 'Absolutely no idea...' 
end
```

El caracter de expresión directa que tiene Ruby hace que se utilice hasta para asignarle valor a una variable

```
pass? = if grade >= 5
  true
else
  false
```

Y el operador ternario (bastante usado en Ruby):

```
pass? = grade >= 5 ? true : false
```

Otra expresión muy usada para asignar un valor por defecto a una variable si es igual a `nil`:

```
@first_name = '' unless @first_name
```

Escrita abreviadamente:

```
@first_name ||= ''
```

_Don’t try to use ||= to initialize things to booleans_ porque si `@first_name` es `false` reseteará su valor a ''.
   

### Evitar problemas

Solo `false` y `nil` son evaluados como _false_. Todo lo demás es tratado como _true_.

Por eso este código hay que evitar:

```
if flag == true
  # do something
end
```

Porque es posible que sea el resultado de `flag = defined?( doc )`, cuyo resultado no es true, sino "local-variable", por lo tanto nunca se cumpliría la condición.


## 3. Estructuras de datos con Ruby, el _array_ y el _hash_

- Esto sería un ejemplo de **_array_** literal en Ruby:

`poem_words = [ 'twinkle', 'little', 'star', 'how', 'I', 'wonder' ]`

Pero con un _array_ como este, sin espacios, se podría simplificar con esta sintaxis:

`poem_words = %w{ twinkle little star how I wonder }`

- Esto sería un ejemplo de **_hash_** con _hash rocket_.

`freq = { "I" => 1, "don't" => 1, "like" => 1, "spam" => 963 }`

Otro _hash_ con símbolos como llaves.

`book_info = { :first_name => 'Russ', :last_name => 'Olsen' }`

Que se podría simplificar así:

`book_info = { first_name: 'Russ', last_name: 'Olsen' }`

### Arrays "fabricados" por Ruby

En este ejemplo Ruby estaría creando un Array en base a unos argumentos en el método para después imprimirlos:

```
def echo_all( *args )
  args.each { |arg| puts arg }
end
```

Siguiendo la misma lógica el siguiente método concatenaría elementos de un _array_ para hacer un _String_ con `+=`

```
class Document
  # Most of the class omitted...
  def add_authors( *names )
    @author += " #{names.join(' ')}"
  end
end
```

También se puede pasar un _hash_ como parámetro

```
def load_font( specification_hash )
  # Load a font according to specification_hash[:name] etc.
end

load_font( { :name => 'times roman', :size => 12 })
```

En este caso en el que el argumento es solo un _hash_, se puede simplificar así la llamada:

`load_font( :name => 'times roman', :size => 12 )`

Y más aun, sin paréntesis. Como si fuera un comando de consola.

`load_font :name => 'times roman', :size => 12`


### Recorriendo un _array_ y un _hash_

#### _Array_

Un ejemplo con bucle `for` a través de un índice sería:

```
words = %w{ Mary had a little lamb }
for i in 0..words.size
  puts words[i]
end
```

Con un bucle `each`:

`words.each { |word, i| puts word }`

El mismo bucle `each` pero mostrando el índice:

`words.each_with_index {|word, i| puts i}`

#### _Hash_

En un bucle `each` como este:

```
movie = { title: '2001', genre: 'sci fi', rating: 10 }
movie.each { |entry| pp entry }
```

Devolvería el siguiente `output`:

```
[:title, "2001"]
[:genre, "sci fi"]
[:rating, 10]
```

Se puede utilizar el mismo bucle con un solo bloque _key - value_ así:

```
movie.each { |name, value| puts "#{name} => #{value}"}
```

Si quisieramos hacer un método que retornase el índice de una palabra en cuestión haríamos esto:

```
def index_for( word )
  i= 0
  words.each do |this_word|
    return i if word == this_word
    i += 1
  end
  nil
end
```

Aunque se podría simplificar mucho con el método `find_index` de `array`:

```
def index_for( word )
  words.find_index { |this_word| word == this_word }
end
```

Otros métodos como `map` devuelven un array transformado en función de condiciones. Por ejemplo, el siguiente código retorna un array con la longitud de cada elemento:

```
words = %{Antonio Hernández}
pp words.map { |word| word.size }
=> [7, 9]
```
Este, un array con las palabras en minúscula

```
lower_case_words = doc.words.map { |word| word.downcase }
```

Si quisieramos contar el número total de letras podríamos hacer el clásico bucle que autoincrementa un total desde 0:

```
total = 0.0
words.each { |word| total += word.size }
```

No obstante, el método `inject` proporciona una manera más sencilla de hacer esto, cotejando un bloque con cada elemento del array como `map` pero pasando dos argumentos, el elemento del array y una variable que se autoincrementa. Cada vez que `inject` hace una llamada al bloque, el valor de `total` se sustituye por el último que se ha calculado hasta que se queda sin elementos y `each` retorna el resultado final:

```
total = words.inject(0.0){ |result, word| word.size + result}
```

El argumen `0.0` Es el valor de `result` la primera vez.

Hay más de 100 métodos de _array_ y más de 80 de `hash`.

#### ¿Qué métodos transforman un _array_ en el acto?

Depende, `reverse` y `sort`, no: 

```
a = [1, 2, 3]

pp a.reverse
=> [3, 2, 1]

pp a
=> [1, 2, 3]
```

En ambos casos habría que usar `reverse!`:

```
a.reverse!

pp a
=> [3, 2, 1]
```
Esta regla no siempre funciona así y metodos como `push`, `pop`, `delete` y `shift` operarían igual que `reverse!`

Los _arrays_ y _hashes_ están ordenados según hayan sido creados. Y un elemento introducido dentro de ellos se añade al final

#### Tener en cuenta...

Que 
```
array = []
array[24601] = "Jean Valjean"
```
Creará un _array_ de 24602 elementos `nil`.

Existe un riesgo de usar un array cuando en realidad no es necesario como en esta situación en la que queremos un array de elementos no duplicados. `<< == push`:

```
unique = []
words.each { |word| unique << word unless unique.include?(word)
```

Será mejor en este caso crear un `set`, es decir, una colección que no elimina los elementos duplicados

```
require 'set'
word_set = Set.new( words )
```

## 4. _Strings_ inteligentes

En ruby tenemos los **_single quotes_** que solo muestran texto, hay que utilizar _backslash_ para escapar la comilla. (`pp` imprimiría el _backslash_ no así `puts`).

`single_quote = 'Say it ain\'t so!'`

Los **_double quotes_** son un poco más complejos. Permiten añadir tabulaciones, retornos de carro etc.

`double_quoted = "I have a tab: \t and a newline: \n"`

Estos últimos se puden embeber fácilmente con `#{}`:

```
author = "Ben Bova"
title = "Mars"
puts "#{title} is written by #{author}"
```

En determinados conextos, combinar ambos _strings_ nos permitirá ahorrar en _backslash_:

```
str = '"Stop", she said, "I cannot deal with the backslashes."'
```

El problema viene cuando en el mensaje conviven '' y "":

`str = '"Stop", she said, "I can\'t live without \'s and "s."'`

Para estos casos existe el _arbitrary quote strings_:

`str = %q{"Stop", she said, "I can't live without 's and "s."}`

En el ejemplo delimitan `{}`, pero también valdrían `[]`, `()`, `<>` p `$$`. La letra `q` importa. La minúscula declara un _single quote_. La mayuscula, un _double quote_.

Una carácteristica de todos los strings es que se pueden separar por líneas:

```
another_one = %q{another multi-line
string}
```

Si queremos partirlo solo en el código:

```
yet_another = %Q{another multi-line string with \
no newline}
```

Aunque si vamos a tener muchas lineas de string, quizá lo más adecuado sea usar _document_:

```
heres_one = <<EOF
This is the beginning 
of my here document. 
And this is the end.
EOF
```

### Métodos de _String_

- `' hello'.lstrip` retorna una copia del _string_ sin espacios.
- `' hello'.rstrip` retorna el mismo _string_ ya que este método elimina los espacios del final.
- `"It was a dark and stormy night\n".chomp` hace lo mismo que `rstrip` pero con los espacios. Solo funciona con una línea cada vez, a diferencia de los `strip`
- No confundir con `chop`: `"hello".chop` retorna "hell".
- `upcase` y `downcase` para hacer mayúsculas / minuúsculas.

- `sub` reemplaza la primera coincidencia pot otra: `'It is warm outside warm'.sub( 'warm', 'cold' )`
- `'yes yes'.gsub( 'yes', 'no' )` reemplzaría todas las coincidencias.
- `split` retorna un _array_ con todas las partes del _string_ separadas por espacios: `'It was a dark and stormy  night'.split`
Se le puede pasar un parámetro al método que determine otro separador distinto al espacio.

Muchos de estos métodos pueden transformar la variable si van acompañados de `!` como hemos visto con _arrays_ y _hashes_:

```
title = 'It was a dark and stormy night'
title.sub!( 'dark', 'bright' )
title.sub!( 'stormy', 'clear' )
```

### Líneas, caracteres, _bytes_

`"Antonio".each_char {|c| puts c}` sería la manera de recorrer un _string_ en un bucle. Y para descubrir los _bytes_ que hay detrás `"Antonio".each_byte {|c| puts c}`.

Si el _string_ tiene más de una línea, se puede recorrer así `string.each_line { |line| puts line}`.

### Atención

**_Ruby strings are mutable_**. Es decir, si igualamos dos variables con un _string_ al cambiar una, cambia la otra:

```
first_name = 'Karen'
given_name = first_name
first_name[0] = 'D'
```
cambiará `given_name`

Ruby nos da cierta flexibilidad con el tema de los índices `first_name[first_name.size - 1]` retorna el último caracter. Es igual que `first_name[- 1]`

También se pueden usar los rangos `"abcde"[3..4]` evalua "de".

## 5. Expresiones regulares

[Aquí](https://github.com/anerodata/Resources/tree/master/linux/regex) hablo de esto de manera genérica en distribuciones de tipo Linux.

En Ruby son un tipo de dato con su sintaxis determinada y va entre _forware slash_:

`/\d\d:\d\d (AM|PM)/`

Además, usamos `=~` para ver si una regexp coincide con un _string_:

`puts /\d\d:\d\d (AM|PM)/ =~ '10:25 PM'` retornaría 0.

_That zero is trying to tell us a couple of things. First, it is saying that the regular expression matched, starting at index zero. Second, the zero is telling us is that when you match a regular expression, Ruby scans along the string, searching for a match anywhere in the string._

Si no hay match en ninguna parte, retornará `nil`.

También se pueden usar como si retornaran un valor boleano así:

```
the_time = '10:24 AM'
puts "It's morning!" if /AM/ =~ the_time
```

Usamos `i` después de la expresión para evitar el _case sensitive_: `puts "It matches!" if /AM/i =~ 'am'`

También podemos usar expresiones regulares con `gsub` de esta manera `str.gsub!( /\d\d:\d\d (AM|PM)/, '**:** **' )`. En este caso estaríamos ocultando las horas sobre el mismo `str`.

**Principios y finales**

- `/\AOnce upon a time/`: Buscaría la expresión al principio de un _string_. _Note that the \A doesn’t match
the first character. Instead, it matches the unseen leading edge of the string_.
- `/and they all lived happily ever after\z/`: Igual pero al final.

Tendríamos problemas con `/\AOnce upon a time/` si lo primero en el _string_ fuese el título del cuento. Aquí es donde aparece el acento circunflejo `/^Once upon a time/`, que busca el _string_ al principio del texto o de cualquier línea dentro de él. El opuesto a esto, es el dolar: `/and they all lived happily ever after$/`, que busca la coincidencia al final del texto o de cualquier línea dentro de él.

Si quisieramos econtrar la apertura y el cierre del cuento nos encontraríamos con un _handicap_ ya que `/^Once upon a time.*happily ever after\.$/` no funcionaría porque `.*` encuentra todos los caracteres menos el salto de línea. Salvamos esto añadiendo `/m` al final de la expresión: `/^Once upon a time.*happily ever after\.$/m`.