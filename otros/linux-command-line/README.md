# Introducción a Linux y a la línea de comandos

[Curso de Frontend Masters](https://frontendmasters.com/courses/linux-command-line/). El curso está documentado [aquí](https://btholt.github.io/complete-intro-to-linux-and-the-cli/) por Brian Holt.

Sitemas operativos como Windows u otros de tipo Unix como MacOS o Linux en cualquiera de sus distribuciones incluyen un _shell_ o interprete de comandos y lenguaje de órdenes. El programa donde este _shell_ es ejecutado se conoce como emulador (Terminator para Linux, Terminal para MacOS O Windows Terminal para windows). 

En el caso de Linux, el _shell_ se llama _Bourne Against Shell (bash)_ en honor a Bourne, el antiguo _shell_. _bash_ es un _shell_ que tiene 30 años y es el más común. ZSH o _Z shell_ es el _shell_ de MacOS (basado en UNIX como Linux). Windows tiene _Windows PowerShell_ y _Command Prompt_ (cmd.exe).

_Shell_ tiene una lógica basada en _Read Evaluate Print Loop_ (REPL), es decir, envías un comando una vez y el interprete evalua, ejecuta un proceso y ocasionalmente imprime un resultado. También es posible ejecutar una linea que ejecute multiples lineas (_looping_).

### Comandos

- `pwd --help`: Información sobre `pwd`
- `ls anerodata`: `ls` es un comando `anerodata` sería un parámetro
- `which ls`: dónde está ese programa? está en `bin` (binary): la carpeta dónde están todos los programas ejecutables
- `ls -l`: `-l` es una bandera. Te da información como la fecha de creación, la hora
- `ls -l -a`: Lo anterior más los directorios y los archivos ocultos. `ls --all` es la manera larga de escribir la bandera como `-a`. Una manera comprimida de ejecutar el comando sería `ls -la`. `--all` es una bandera con dos guiones porque si fuera uno, `bash` entendería que quieres concatenar banderas como en `ls -la`.
- `tail -n 3 ~/.bash_history`: imprime las 3 últimas lineas de un fichero. Util para imprimir logs.
- `head`: Imprime las diez primeras líneas de un fichero.
- `tail -f`: Imprime las ultimas lineas del fichero en tiempo real. Útil par logs.
- `!!`: ejecuta el último comando ejecutado
- `less`: + el nombre del archivo, lo lee. Dentro, `/texto` busca el texto en el fichero.
- `more`: la versión antigua de `less`.
- `man`: es un programa que usa `less`. Muestra el manual de un programa
- `cat`: + el nombre del fichero, lo imprime en la consola (_concatenate to the standart out_).
- `rm`: borra directorios
- `rm -f`: borra directorios y su contenido recursívamente
- `rm -rf`: igual pero con _force_. Es decir, no pregunta si estás seguro o no (para módulos de node o repositorios).
- `trash`: [instalar](https://www.tecmint.com/trash-cli-manage-linux-trash-from-command-line/). Manda el fichero a _trash_.
- `cp -R file directory`: lleva el fichero al directorio, lo crea si no existe.
- `rm -r -- !(README.md)`: borra todo menos ese fichero.

#### Archivos comprimidos

- `tar -cf archive.tar pepe/ README.md`: Crea un archivo sin comprimir.
- `tar -zcf archive.tar.gz pepe/ README.md`: crea un archivo comprimido 
- `tar -xzf archive.tar.gz -C some-folder`: extrae un fichero comprimido en `some-folder` (tiene que haber sido creada)

#### _Wildcards and replacements_

- `touch file{1,2,3,pepe}.txt`: {} = _expansion_. Añade _file_ delante de cada valor y crea un fichero para cada uno. Aplica para otros programas como `rm`.
- `ls file*.txt`: * = _wildcard_. Lista todos los ficheros que comiencen por file y terminen por .txt
- `ls file?.txt`: Lista todos los ficheros que comiencen por file y terminen por .txt, descartando `file-1.txt` por ejemplo. `ls file-??.txt`, listaría `file-12.txt`, pero no `file-1.txt`.
- `touch files/file-{1..50}.txt`. Dentro de `files`, crea 50 ficheros.
- `echo {a..z..10}`: imprime `a k u`.
- `echo {a..z}{1..2}`: imprime `a1 a2 b1 b2`...

### Editores de texto

Vim y Nano. Vim tiene varios modos, el modo comando y el modo de edición. Pulsando sobre `ESC` pasamos al modo de comando.

Algunos comandos de vim:

- `:q` - salir.
- `:q!` - salir sin importar que no haya cambios guardados.
- `:qa!` - salir forzadamente.
- `:d` - borrar una línea.
- `:d100` - desde la primera linea, borra desde la primera hasta la 100.
- `:wq!` - escribir y salir.
- [_copy/paste_](https://vim.fandom.com/wiki/Copy,_cut_and_paste)
- `ALT A`: va al final de la línea con `INSERT`.
- `ALT I`: va al principio de la línea con `INSERT`. 

Toda la [documentación](http://vimdoc.sourceforge.net/htmldoc/) de Vim. Y la [Wiki](https://vim.fandom.com/wiki/Vim_Tips_Wiki) de Vim.

Para destacar las búsquedas he creado el fichero `~/.vimrc` y he he escrito `set hlsearch`. Es para que `:set hlsearch`, comando ejecutable en Vim durante una sesión, permanezca siempre.

### Atajos

Para reconfigurar comandos, [aquí](https://btholt.github.io/complete-intro-to-linux-and-the-cli/signals-and-the-power-of-ctrl).

- `CTRL + R`: _reverse search_. Para buscar comandos.
- `CTRL + SHIFT + C` y `CTRL + SHIFT + C`: _copy_ y _paste_ en el _bash_ cuando estamos en Windows.
- `CTRL + A`: takes you to the beginning of the line
- `CTRL + E`: takes you to the end of the line
- `CTRL + K`: "yank" everything after the cursor
- `CTRL + U`: "yank" everything before the cursor
- `CTRL + Y`: "paste" (paste in quotes because it doesn't actually go into your system clipboard) everything you yanked
- `CTRL + L`: clear the screen
- `CTRL + R`: reverse search through history

### Señales

`kill -l` lista todas las señales. Son usadas por los procesos para comunicarse entre ellos o con _shell_, como el caso de SIGALARM.

- `CTRL + C` (SIGINT): interrumpe un proceso.
- `CTRL + D` (SIGQUIT): _quit_. Cierra la sesión del _bash_. Dentro de un programa REPL (Python), este comando lo que haría sería cerrarlo.
- SIGTERM: no tiene atajo, pero es la señal que se envía cuando se usa `kill` + programa. Ocurre cuando el sistema operativo se apaga. Envía SIGTERM  a todos los programas para avisar de que se va a cerrar. Una vez que todos se cierran, cierra la terminal.
- `kill -9` (SIGKILL): detiene un la ejecución de un programa inmediatamente.
-  `echo hi >> README.md`: imprime hi en el fichero, si no existe, lo crea.
- `mkdir -p uno/dos/tres`: anida directorios dentro del directorio uno. `-p` crea una carpeta con ese nombre si no existe.
-  **Detener un programa**: `yes > /dev/null &` Ejecuta yes en el _background_. `ps aux | grep yes` muestra todos los programas que se llamen _yes_ que se están ejecutando. Con su ID lo detenemos así `kill -9 428` en vez de `-9` también valdría `-SIGKILL`.

#### _Streams_

_One of the Linux philosophies is the assumption that the output of a program can be the input to another program through streams and pipes, then is it possible to redirect the output to another file._

##### _Output streams_

- `echo 'text' 1> text.txt`: `>1` redirecciona (_standard out_). Convierte el _output_ del programa _echo_ en el _input_ del fichero `text.txt` y borra todo lo anterior. `echo 'text' 1>> text.txt`: añade el contenido, no borra lo anterior.
- `cat text.text 1> text-2.txt`: con la filosofía anterior, estaríamos copiando un programa.
- `ls -lash 1>> text2.txt`: lleva el output del listado a `text2.txt`.
- `cat non-existant-file.txt 2> error.txt`: `>2` redirecciona (_standard error_). Convierte un _output_ de error en en el _input_ de otro fichero. El fichero no existe, por eso produce un error.
- `ls -lash file.txt 1> ls.txt 2> error.txt`: Separación de _streams_. los errores iran en `error.txt`.
- `ls -lash 1> /dev/null`. Solo imprimirá errores. El resto de mensajes, no. Para ejecutar un programa del que solo queramos saber los errores.

##### _Input streams_

- `cat < file.txt`: `<` = _standard in_. Envia el archivo como _input_ a `cat` y este programa lo devuelve como  _output_.
- `grep ".md\|.txt" < file.txt`: coge el conteindo del fichero y se lo lanza a grep como _input_ el _output_ que devuelve `grep` (programa que filtra) es la línea del fichero que sea `.md` o `.txt`.
- `greap ".md" < file.txt 2> error.txt`: mandamos el error a `error.txt`. `greap` no existe con lo cual el error irá al fichero. Si el comando estuviera bien escrito se mostraría en consola la línea del `README.md` y no escribiría nada en el fichero de errores.
- `grep .md file.txt > output.txt 2> /dev/null`: filtra el `README.md`, se lleva el resultado al `output.txt`

### _Pipes_ o "conductores"

_In order to move from one program to another within the command line, developers have to use pipes._

- `cat output.txt | grep .md`: _`cat` takes the output of the file and pipes into `grep`_. 
- `tasklist.exe | grep firefox`: filtra los procesos de windows en los que ponga "firefox".
- `yes n | rm -i file*`: responde "no" a borrar todos los ficheros.

### Usuarios

- `cat /etc/passwd`: imprime los usuarios de esa máquina. Todos los que no tienen `bash` en la ruta significa que no pueden acceder a ella. Ni siquiera teniendo la credencial. Es positivo para evitar hackeos.

Si intentamos hacer un directorio en `/`, no podemos. Solo el usuario `root` tiene permisos para operar ahí: borrar, crear...

- `whoami`: me dice `anerodata`, pero `sudo whoami`, `root`. `sudo` nos permite operar como `root` y volver a nuestro usuario inicial tras acabar la operación.
- `sudo su`: accedemos a `root`.

Creamos un nuevo usuario para realizar una tarea determinada en un directorio, estando como registrado como `root`.
- `useradd pepe`: crea un nuevo usuario.
- `sudo useradd -s /bin/bash -m -g ubuntu pepe`: crea un nuevo usuario con acceso a `bash`, no `dash`. Crea un `home`. Con los mismos permisos que `ubuntu` con el nombre de `pepe`.
- `passwd pepe`: contraseña.

Al hacer `cat /etc/passwd` podemos leer los usuarios de la máquina. `pepe:x:1001:1001::/home/pepe:/bin/sh`. Las dos primeras cifras son ID de grupo, la penúltima ruta es su _home_ (directorio al que va al loggearse) y la siguiente es su _shell_.

### Grupos

Usamos los grupos para dar x permisos a x usuarios.

- `sudo usermod` -aG sudo pepe: le da permisos de `sudo` a pepe. Ahora puede usar `sudo`. `-aG`: `a` mete en el grupo, `G` indica en cuál.

### Permisos

Estando en un _Windows Subsystem Linux_ esto solo funcionará en _home_ o _root_ pero no en `/mnt/c/`.

- `drwxr-xr-x`: `d` indica directorio, si fuera `-` sería fichero. después `rwx` (_read_, _write_, _execute_ por el usuario en cuestión) + `rwx` (por el grupo del usuario en cuestión) + `rwx` (el resto). _Execute_ se produce al hacer un `ls` sobre el directorio por ejemplo.

- `sudo chown anerodata:anerodata folder/`: _change ownership_. Cambia la propiedad del directorio a `anerodata` y al grupo `anerodata`.

- `sudo chmod u=rwx,g=rwx,o=rwx hello/`: cambiría los permisos a _read, write and execute_ para el usuario, el grupo y los otros en ese directorio.

- `sudo chmod u=rwx, g=rwx, o=rwx file.txt` = `sudo chmod 777 file.txt`.

- `sudo chmod -x`: quita los permisos de ejecutar a todos. `chmod +x` funcionaría al revés.

### _Environments_

- `printenv`: imprime las variables de entorno. Las podemos imprimir diciendo `echo $NAME` por ejemplo
- `sudo vi /etc/environment` permite añadir variables de entorno
- `echo $VARIABLE`: la imprime
- En `~/.bashrc` también añadimos variables de entorno. Solo que para un usuario en cuesión. En lugar de para todos.
- `source ~/.bashrc`: corre ese script para reconocer las novedades o cambios
- La diferencia entre `~/.bashrc` y `~/.bashrc_profile` es que el primero es un script que corre con más frecuencia. Cada vez que abres `bash`. El segundo solo corre la primera vez al abrir la consola por primera vez. Ante la duda, `.bashrc`.

### Procesos

- Ejecutando `ps` mostramos los procesos en consola.
- Ejecutando `sleep 10 & ps` y al acabar los 10 segundos, `ps` de nuevo, vemos como ha terminado.
- En "ejercicios" hay un ejemplo de como se "mata" un proceso.
- `ps aux` permite ver los procesos ejecutados por cualquier usuario en la máquina. `ps aux | less` para mostrarles poco a poco. También se pueden filrar con `grep`
- Para poner procesos en el _background_ usamos `CTRL + Z` y luego `jobs`. Vemos el proceso parado. Decimos `bg 1` 1 sería el ID del proceso y ejecutamos `jobs` de nuevo. Podemos ver como corre ahora en el _background_. `fg 1`. Hace lo contrario. Pone el proceso en el _foreground_.
- `tmux` divide la el bash hace un _split_. No lo recomienda. `screen` Abre otra ventana para navegar en _bash_. Información sobre [`screen`](https://linuxize.com/post/how-to-use-linux-screen/).
- `jobs -l` lista los procesos con el ID, para poder matarlo.
- `kill $(jobs -p)` detiene todos los procesos.
- `sleep 10 &` manda el proceso directamente al _background_.
- `sleep 10 & > output.txt` manda el _output_ al _background_. Evita que aparezca en la pantalla del _bash_.

### Códigos de salida y operadores de proceso

Cada vez que ejecutamos un programa, como `date`, podemos ver ejecutando `echo $?` como ha terminado. Si lo que aparece es 0, eso es que ha tenido éxito.

Podemos hacer la prueba con `yes`, y parándolo con `CTRL + C`. [Aqúí](https://btholt.github.io/complete-intro-to-linux-and-the-cli/process-operators) Están los significados de los códigos.

- `touch status.txt && date >> status.txt && uptime status.txt`. Va ejecutando procesos si el anterior tiene un código de salida = 0. `status` te dice cuanto tiempo lleva la máquina encendida.

- `touch status.txt || date`, con el _OR_ operator. Si no tiene éxito a la primera, se va al siguiente comando.

- `true ; false ; echo hi` ejecuta los programas sin importar el éxito o el fracaso.

### Subcomandos

- `echo I thing $(whoami) is a champ` = `echo I thing anerodata is a champ`. El dolar ejecuta un subcomando. Ejecuta un subcomando separado poniendo lo que devuelva al _standard out_. `echo I thing ``whoami`` is a champ` funcionaría de la misma manera.

- `echo $(date +%x) - $(uptime) >> log.txt` al iniciar un trabajo, guardaría en un log la fecha y la información de la máquina.

### _Secure Shell_ (SSH)

Brian utiliza [`lasspass`](https://multipass.run/) para crear dos máquinas virtuales y conectarlas con `SSH`.

Es un protocolo que permite establecer conexión con un servidor remoto para ejecutar programas desde nuestra máquina. Es una clave criptográfica que crea una versión publica y una privada que no revelas a nadie. Usando ambas, permites conectar ordenadores. A ambas máquinas no les hace falta revelar las claves públicas para comprobar c
ada una que la otra tiene la clave pública que dice tener. [Aquí](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange) está explicado con mayor detale. `ssh-keygen -t rsa` es el comando para crear una clave SSH. Esto genera dos ficheros `id_rsa` es la privada e `id_rsa.pub` es la pública, la que se revela.

En la segunda máquina, Brian crea el fichero `authorized_keys` en `~/.ssh`, copia el `id_rsa.pub` de la otra máquina en este fichero de la otra para comprobar que esta es la clave pública asociada a la privada. La clave privada sería como la llave y la pública el candado que enseñas al otro ordenador.

Ahora necesitamos la `ip` del segundo servidor. Para que el primero se conecte al segundo. `ifconfig` muestra info de red. Entonces con la `inet` genera el siguiente comando `ssh brian@[inet]` brian es el usuario en el que ha dejado la copia de `id_rsa.pub`.

### _Secure File Transfer Protocol_ (SFTP) 

- `sftp brian@[inet]` Inicia el protocolo con la segunda máquina después de haber realizado lo de las claves `SSH`. Ahora si hacemos `pwd`, nos muestra la ruta de la segunda máquina.
- `put file.txt` sube el fichero al servidor remoto. Dentro de este modo, `!echo "file text" >> file.txt`, crearía un fichero. `help` te muestra la ayuda.
- `get file.txt getted.file.txt` descargaría el fichero de la segunda máquina.
- `bye` abandona SFTP.

### WGET

Se utiliza para descargar algo de internet. Hacer `cp` en internet. No se conecta a los _pipes_, con lo cual no puedes derivar el contenido de lo que descargas a otros programas. `wget` también puede hacer POST, PUT _requests_, al igual que CURL. WGET es capaz de descargar directorios recursivamente. Por ejemplo, en una web en la que se conecten ficheros CSS con rutas relativas, el programa encontraría esas URL y descargaría los contenidos. CURL no hace esto.

- `wget https://raw.githubusercontent.com/mydzor/bash2048/master/bash2048.sh` descarga el juego de internet.
- `bash bash2048.sh` ejecutaría el fichero.
- `chmod +x` le da permisos de ejecución a todos los usuarios y ahora el fichero es ejecutable de lam siguiente manera `. bash.sh`.

### CURL

`curl` funciona igual que `wget`, solo que es capaz de conectarse a los `pipes`. `curl` se usa mucho para probar una API por ejemplo.

- Es decir se podría hacer: `curl https://raw.githubusercontent.com/mydzor/bash2048/master/bash2048.sh >> game.sh` 
- `python3 -m http.server 8000 --bind 0.0.0.0`, dispara un servidor web.
- `curl http://192.168.1.46:8000/` hace una petición sin descargar el contenido. Solo imprimiéndolo en _standard out_.
- `curl -o result.html http://192.168.1.46:8000/` se lo llevaría a ese fichero sin usar _pipes_.
- `curl -X POST http://192.168.1.46:8000/` o `POST` o `PUT`... Cualquier verbo [`HTTP`](https://es.wikipedia.org/wiki/Protocolo_de_transferencia_de_hipertexto).
- `curl -d "post body" http://192.168.1.46:8000` envía datos junto con la petición `POST`. `curl -X PUT -d "post body" http://192.168.1.46:8000`, haría lo mismo pero con `PUT`.
- `curl -b "name=anerodata" -X PATCH http://192.168.1.46:8000` enviaría una petición copn _cookie_.
- `curl -L https://bit.ly/linux-cli`: petición con redirección.
- `curl -H "accept-language: en-US" -H "Authorization: xx" http://192.168.1.46:8000` para enviar _headers_ con la petición.
- A través del navegador se puede copiar una petición como `curl`.
- Hacer un pipe de `curl` a bash, es decir, descargar un programa y ejecutarlo puede ser peligroso. La confianza la otorga el dominio de donde descargas (github). En caso de que sea un sitió extraño. Descargamos el contenido en un fichero y comprobamos que se ha descargado. Ya que hay sitios que pueden cambiar el contenido por debajo de nosotros.

### Gestores de paquetes

Advance Tool Package (APT) Es el gestor de paquetes de Ubuntu. DPKG es el de Debian por ejemplo.

- `sudo apt install aptitude` Proporciona una interfaz gráfica de esto. `sudo apt install` es la versión nueva de `sudo apt get install`.
- `apt search node`: todos los paquetes disponibles de node. 
- `apt show nodejs`: muestra la información de `node`.
- `sudo apt autoremove`: borra paquetes que no se necesitan por que no son referenciados por ningún programa.
- `sudo apt update`: no actualiza ni instala nada, solo actualiza la lista de paquetes disponibles y sus versiones
- `sudo apt list upgradeable`: lista los paquetes que deben ser actualizados segun la actualización anterior.
- `sudo apt upgrade`: actualiza los programas después de haber actualizado la lista con `sudo apt update`
- `sudo apt full-upgrade`: fusión de `autoremove`, `update` y `upgrade`.

[apt-browse](https://www.apt-browse.org/) es un repositorio con todo lo que tiene `apt`.

`apt` por debajo está usando `apt-get`, `apt-cache` y muchos programás más. Es una especie de envoltorio que corre en una capa superior respecto a las anteriores.

### Snaps

Es otro programa para gestionar paquetes como `apt`. Es más seguro que este último porque usa _sandboxing_, una manera de encapsular paquetes, de manera que cuando los instalas, si tienen codigo malicioso son incapaz de dañar el sistema operativo o de robarte información. Funcionan con independencia del sistema operativo, a diferencia de `apt`, por eso funciona en cualquier distribución de Linux.

Además, las actualizaciones son más rápidas, no borra del todo la última versión apra instalar de 0 la nueva.

`sudo snap install lolcat` instalaría el mismo programa, pero mejor empaquetado. `ls -lash lolcat` saca al _standard out_ el listado coloreado.

`snap` funciona con _autoupdate_, es decir, el programa se actualiza solo como un navegador. Por eso se usa mucho para aplicaciones de escritorio. Al incluir todas las dependencias en un solo paquete, los prgramas suelen ocupar más que con `apt`.

`snap` usa un _daemon_, un programa que corre en el _background_ sin que lo ejecutemos. Hay que instalarlo si no lo está.

`snap info node` te da toda la información de `node`: versiones... etc Más actualizadas que `apt`. Cuando usamos `snap` nos conectamos a un canal que si no se explicita, es el de por defecto. `sudo snap install --channel=14/stable --classic node` `--classic` hace que no sea exactamente _sandbox_, lo que significas que tienes que confiar.

### _Scripts_

Se ejecutan con `source` delante o con `. script.sh`. También con `bash` delante. Así se crearía un subproceso y no se producirían cambios de directorio. Con `source` todo sucede en el mismo proceso

#### _Shebang or Hashbang_

`#! /bin/bash`. En lo alto de el script, le dice `bash` que ejecute esto en la _shell_ `bash`. Después de poner esto en nuestro _script_. y cambiar los permisos del `script.sh` así `chmod +x script.sh` podemos ejecutar el fichero así `./script`, incluso quitando la extensión `.sh`. No usas ningún comando, sino que simplemente corres el fichero y a través de _shebanh_, `bash` averigua dónde ejecutarlo.

`which python3` nos daría la ruta de `python3` para configurar un _shebang_ de un fichero _python_.

_shebang_ posibilita compartir _scripts_ con usuarios de interpretes de comandos UNIX que no son LINUX (`zsh`, `PowerShell`).

#### _Path_

`echo $PATH` muestra los _paths_, las rutas donde todos los programas están. Entonces cada vez que corres `python` por ejemplo, `bash` recorre cada `path` en su búsqueda. En los ejemplos de _shebang_ ejeutabamos los prgramas así `./`, para ejecutar un programa que no está en PATH. 

Ahora hemos metido el `script` de `bash` en una carpeta (my_bin) y le hemos pasado esta ruta absoluta al PATH de la siguiente manera. En `.bashrc` hemos colocado la variabla así `export PATH=/mnt/c/Users/anton/Desktop/anerodata/github/anerodata/formacion/otros/linux-command-line/bash-scripts:$PATH` con `:$PATH` para que no sobreescriba a PATH. `source ~/.bashrc` para refrescarlo. Al hacer `echo $PATH` vemos que la ruta está ahí. Ahora podemos ejecutar `gen-files` desde cualquier parte del ordenador


#### Argumentos

Podemos dar un argumento a la variable así `$DESTINATION=$1`. Para pasarle un destino en la ejeución del fichero. De manera que ahora diriamos `gen_files dir/my-dir`.

```
#Prefix by user
read -p "enter a file prefix: " FILE_PREFIX
```
Con estas lineas parametrizamos `FILE_PREFIX` para que el usuario le de el prefijo que quiera al fichero. No lleva `$` precediendo porque si lo llevara le estaríamos pasando a `read` el valor de `FILE_PREFIX`. Queremos asignar un valor con `read` para la variable, no pasarle al programa el valor que ya tenga. 

#### Condicionales

```
if [ -z $DESTINATION ]; then
        echo "no path provided, defaulting to ~/temp"
        DESTINATION=temp
fi
```

Si el usuario no incluye nada en el _input_ la ruta por defecto sera `~/temp`. `-z $VAR` es igual `true` si está vacía. Los corchetes evaluan como `test`, es como ejectuar `test -z "aa" && echo $?` en la línea. Será 1 `false` porque el _string_ no está vacio. `man test` para más información.

Brian lo llama _sintax sugar for testing_.

- `test 15 -eq 15` Devuelve `0`. o `test 15 -eq 15 && echo is true`. Dueleve `is true`.
- `test 15 -ne 15`: _not equal than_.
- `test 15 -gt 10 && echo is true`: _greater than_.
- `test 15 -lt 10 && echo is true`: _less than_.
- `test 15 -ge 10 && echo is true`: _greater or equal than_.
- `test 15 -le 10 && echo is true`: _less or equal than_.
- `test -e gen_files && echo is true`: ¿Existe el archivo?
- `test -w gen_files && echo is true`: ¿Existe el archivo y lo puedo escribir con mi usuario `anerodata` actual?

#### Loops

En los scripts de `bash`. En uno de ellos se utiliza `NUM_TO_GUESS=$(( $RANDOM % 10 + 1 ))` para sacar un número random entre 1 y 10. Los dobles parenteis con el dolar convierten a `let`, justo como los corchetes hacían con `test`. `let` es para hacer operaciones aritméticas.


### _Cron jobs_

Cualquier _script_ aquí correrá periódicamente:

- `/etc/cron.daily`
- `/etc/cron.hourly`
- `/etc/cron.monthly`
- `/etc/cron.weekly`

`crontab -e` abre el gestor de _cronjobs_. `* * * * * /mnt/c/Users/anton/Desktop/anerodata/github/anerodata/formacion/otros/linux-command-line/bash-scripts/make-file`. Los asteristos son minutos, horas, día del mes (21st), mes, día de la semana (lunes.). En el ejemplo, el _script_ correrá cada minuto siempre que tenga permisos de ejecución habilitados. [Esta](https://crontab.guru/) es una gran herramienta.

`crontab -u root -e` instalaría un `cron` con `root`. Lo normal es hacerlo con un usario que no sea `root`. En WSL, ponemos esto `service cron start` en `~/.bashrc` para iniciar un proceso con cron. [Más info](https://scottiestech.info/2018/08/07/run-cron-jobs-in-windows-subsystem-for-linux/)

### Customizar el _prompt_

Se puede ver así `echo $PS1` y cambiar de nombre así `PS1='$'`. `curl https://raw.githubusercontent.com/riobard/bash-powerline/master/bash-powerline.sh > ~/.bash-powerline.sh`. Descarga un customizador de consola de comandos. _gitbash_ o _spaceship_ para `zsh` son otros tipos de _prompt_.

Para pintar de verde, por ejemplo `echo -e "\e[32mverde`. Es muy útil para destacar resultados en _bash scripts_ por ejemplo. Si no modificamos `echo` con `-e`, sacaríamos por consola exactamente esa notación porque no buscaría caracteres escapados. En [awesomebash](https://github.com/awesome-lists/awesome-bash) podemos ver un conjunto de programas muy curiosos.

### Final

A partir de aquí, algunos [recursos extra](https://btholt.github.io/complete-intro-to-linux-and-the-cli/conclusion). Sobre [symlinks](https://linuxize.com/post/how-to-create-symbolic-links-in-linux-using-the-ln-command/).

### Instalando un antivirus

De entre todos los antivirus (en este artículo de [Genbeta](https://www.genbeta.com/linux/mejores-soluciones-anti-malware-para-linux) y en este otro de [Tecmint](https://www.tecmint.com/best-antivirus-programs-for-linux/) al final me decanto por [ `clamav`](https://www.clamav.net/documents/installing-clamav).

Es uno de los más recomendados, soporta casi todos los formatos de _mail_, trabaja desde la línea de comandos, fácil de instalar y de usar, proporciona una base de datos de virus actualizable, escanea ficheros y zips. Es un estándar en entornos UNIX.

- Para instalar `sudo apt install clamav clamav-daemon`
- `sudo systemctl stop clamav-freshclam` detiene el servicio que corre permanentemente y `sudo freshclam` actualiza y guarda los nuevos datos de virus.
- `sudo systemctl start clamav-freshclam` activa de nuevo el servicio.
- Para escanear un fichero o directorio `clamscan file.txt`.

Más info [aquí](https://linuxhint.com/install_clamav_ubuntu/) y [aquí](https://computernewage.com/2014/10/07/como-detectar-virus-en-linux-con-clamav/) y en la documentación del programa y haciendo `man clamscan`.
