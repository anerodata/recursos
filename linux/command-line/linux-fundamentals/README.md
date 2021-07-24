# Linux Fundamentals

Algunas notas sobre el libro [_Linux Fundamentals_](http://linux-training.be/files/books/LinuxFun.pdf).

## 8 - Directorios

`pushd dir_name` y `popd` son dos comandos interesantes. El primero añade el directorio al _stack_ de directorios. El segundo retrocede al directorio añadido en `pushd dir_name`.

`dirs` muesta la pila actual de directorios.

## 9 - Ficheros

En Linux todos los elementos son considerados ficheros: directorios, programas, imágenes, archivos de texto... etc.
Tenemos información sobre su tipo con el comando `file`.ç

En Ubuntu podemos usar el programa `rename` para renombrar muchos ficheros utilizando expresiones regulares: `rename 's/conf/backup/' *.conf` sustituye `.conf` por `.backup` en todos los ficheros con la extensión `.conf`.