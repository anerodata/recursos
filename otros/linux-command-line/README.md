# Introducción a Linux y a la línea de comandos

[Curso de Frontend Masters](https://frontendmasters.com/courses/linux-command-line/). El curso está documentado [aquí](https://btholt.github.io/complete-intro-to-linux-and-the-cli/) por Brian Holt.

Sitemas operativos como Windows u otros de tipo Unix como MacOS o Linux en cualquiera de sus distribuciones incluyen un _shell_ o _Command Line Interface (CLI)_. El programa donde este _shell_ es ejecutado se conoce como emulador (Terminator para Linux, Terminal para MacOS O Windows Terminal para windows). 

En el caso de Linux, el _shell_ se llama _Bourne Against Shell (bash)_ en honor a Bourne, el antiguo _shell_. _bash_ es un CLI que tiene 30 años y es el más común. ZSH o _Z shell_ es el _shell_ de MacOS (basado en UNIX como Linux). Windows tiene _Windows PowerShell_ y _Command Prompt_ (cmd.exe).

### Comandos

- `pwd --help`: Información sobre `pwd`
- `ls anerodata`: `ls` es un comando `anerodata` sería un parámetro
- `which ls`: dónde está ese programa? está en `bin` (binary): la carpeta dónde están todos los programas ejecutables
- `ls -l`: `-l` es una bandera. Te da información como la fecha de creación, la hora
- `ls -l -a`: Lo anterior más los directorios y los archivos ocultos. `ls --all` es la manera larga de escribir la bandera como `-a`. Una manera comprimida de ejecutar el comando sería `ls -la`. `--all` es una bandera con dos guiones porque si fuera uno, `bash` entendería que quieres concatenar banderas como en `ls -la`.
- `tail ~/.bash_history`: imprime las diez últimas lineas de un fichero
- `!!`: ejecuta el último comando ejecutado

### Atajos

- `CTRL + R`: _reverse search_. Para buscar comandos.
- `CTRL + SHIFT + C` y `CTRL + SHIFT + C`: _copy_ y _paste_ en el _bash_ cuando estamos en Windows. 
