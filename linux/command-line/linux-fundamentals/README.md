# Linux Fundamentals

Algunas notas sobre el libro [_Linux Fundamentals_](http://linux-training.be/files/books/LinuxFun.pdf).

## 8 - Directorios

`pushd dir_name` y `popd` son dos comandos interesantes. El primero añade el directorio al _stack_ de directorios. El segundo retrocede al directorio añadido en `pushd dir_name`.

`dirs` muesta la pila actual de directorios.

## 9 - Ficheros

En Linux todos los elementos son considerados ficheros: directorios, programas, imágenes, archivos de texto... etc.
Tenemos información sobre su tipo con el comando `file`.ç

En Ubuntu podemos usar el programa `rename` para renombrar muchos ficheros utilizando expresiones regulares: `rename 's/conf/backup/' *.conf` sustituye `.conf` por `.backup` en todos los ficheros con la extensión `.conf`.

## 10 - El contenido de ficheros

1. Display the first 12 lines of `/etc/services`.

`head -12 /etc/services`

2. Display the last line of `/etc/passwd`.

`tail -1 /etc/passwd`

3. Use cat to create a file named count.txt that looks like this:

`echo -e "one\ntwo" > count.txt`

4. Use cp to make a backup of this file to cnt.txt.

`cp count-txt count-backup.txt`

5. Use cat to make a backup of this file to catcnt.txt.

`cat count-backup.txt > catcnt.txt`

6. Display catcnt.txt, but with all lines in reverse order (the last line first).

`tac count-backup.txt`

7. Use more to display /etc/services.

`more /etc/services`

8. Display the readable character strings from the /usr/bin/passwd command.

`strings /usr/bin/passwd`

9. Use ls to find the biggest file in /etc.

`ls -lS /etc/ | head`

11. Use cat to create a file named tailing.txt that contains the contents of tailing.txt followed
by the contents of /etc/passwd.

`cat /etc/passwd >> tailing.txt`

12. Use cat to create a file named tailing.txt that contains the contents of tailing.txt preceded
by the contents of /etc/passwd.

`mv tailing.txt tmp.txt ; cat /etc/passwd tmp.txt > tailing.txt `