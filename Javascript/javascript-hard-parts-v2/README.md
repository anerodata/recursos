# Javascript: The Hard Parts 2

Curso de Front end masters impartido por Will Sentance

## 1. Javascript principles

Algunos conceptos básicos sobre Javascript:

- Identifier: nombre con el que se almacena la variable o la constante en memoria
- Value: valor del _identifier_. _Anything stored_.
- Parameter: _placeholder_ que representará el nombre del valor que se le pasa a una función.
- Argument: valor que se le pasa a una función y que se le asigna en memoria local al _parameter_ dentro de un contexto de ejecución dado. Su alteriación implica una alteración de ella (funciona como un link) en el contexto global (_side efect_).
- Command: _any line with parenthesis_. Ej: `const name = getName()`. No se almacena en memoria y `name` permanece _uninitialized_ hasta que el hilo de ejecución pasa por ella y se crea el contexto de ejecucion `getName`. Cuando termina la ejecución de `getName`, se asigna el valor en memoria a `name` entendiendo que `getName()` tiene un `return`. Se retornaría el valor asignado al identificador en la sentencia `return`.
Lo que si queda almacenado en memoria es la función y su contenido que después se utilizara en la invocación.

`const output = multyplyBy2(10)`

Cuando el _execution thread_ (solo puede haber uno), llega a la línea de arriba, declara `output`, no almacena nada en memoria, sino que se crea un nuevo contexto de ejecución con el nombre `multyplyBy2`. Está función tendría un parámetro al que se le asigna el argumento `10`. En un contexto local, la función retorna un valor que se le asigna a `output`, entonces su valor queda almacenado en la memoria del contexto de ejecución en el que se encuentre (global o local).

Cuando una función termina de ejecutarse, se borran de la memoria los datos de ese contexto de ejecución concreto. Sabemos en qué contexto de ejecución nos encontramos gracias a la pila de llamada o _call stack_.

## 2. Functions and callbacks

Principios básicos a la hora de escribir funciones:

- DRY (_Don't Repeat Yourself_).
- Escribir código reusable. _Save them once use it again_.
