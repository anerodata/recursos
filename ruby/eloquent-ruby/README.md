# _Eloquent Ruby_

Notas sobre el libro de 2011 escrito por Russ Oslen para Addison-Wesley Professional. Está en la web de [O'Reilly](https://www.oreilly.com/library/view/eloquent-ruby/9780321700308/).

>  It’s easy to write “correct” Ruby code. But it’s far harder to gain the fluency needed to write great Ruby code. To do that, you need to go beyond syntax and absorb the “Ruby way” of thinking and problem solving. In Eloquent Ruby, Russ Olsen helps you understand Ruby like true Rubyists do—so you can leverage its immense, surprising power.
Olsen draws on years of experience internalizing the Ruby culture and teaching Ruby to other programmers. He guides you to the “Ah Ha!” moments when it suddenly becomes clear why Ruby works the way it does and how you can take advantage of its unique approach.
Eloquent Ruby starts small, answering tactical questions focused on a single statement, method, test, or bug. You’ll learn how to write code that actually looks like Ruby (not Java); why Ruby has so many control structures; how to use strings, expressions, and symbols; and what dynamic typing is really good for.

## 1 - Convenciones de Ruby

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