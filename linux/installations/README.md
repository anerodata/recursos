# Instalaciones

## Ubuntu

Para instalar Ubuntu y eliminar Windows hay que crear un _bootable usb_ con Ubuntu instalado. Iniciarlo y seguir los pasos. Está explicado en [la web](https://ubuntu.com/tutorials/install-ubuntu-desktop#1-overview).

## Instalando un antivirus

De entre todos los antivirus (en este artículo de [Genbeta](https://www.genbeta.com/linux/mejores-soluciones-anti-malware-para-linux) y en este otro de [Tecmint](https://www.tecmint.com/best-antivirus-programs-for-linux/) al final me decanto por [ `clamav`](https://www.clamav.net/documents/installing-clamav).

Es uno de los más recomendados, soporta casi todos los formatos de _mail_, trabaja desde la línea de comandos, fácil de instalar y de usar, proporciona una base de datos de virus actualizable, escanea ficheros y zips. Es un estándar en entornos UNIX.

- Para instalar `sudo apt install clamav clamav-daemon`
- `sudo systemctl stop clamav-freshclam` detiene el servicio que corre permanentemente y `sudo freshclam` actualiza y guarda los nuevos datos de virus.
- `sudo systemctl start clamav-freshclam` activa de nuevo el servicio.
- Para escanear un fichero o directorio `clamscan file.txt`.

Más info [aquí](https://linuxhint.com/install_clamav_ubuntu/) y [aquí](https://computernewage.com/2014/10/07/como-detectar-virus-en-linux-con-clamav/) y en la documentación del programa y haciendo `man clamscan`.

## Autofirma

Es un programa para firmar PDF con un certificado digital o firma electrónica. En la [descarga](https://firmaelectronica.gob.es/Home/Descargas.html) hay información sobre como instalarlo y [aquí](https://www.pcrednet.com/blog/10008-tutoriales/90-instalar-autofirma-en-ubuntu-18-04-y-linux-mint-19) también. En resumidas cuentas:

- `sudo apt install libnss3-tools`, tal y como afirman [aquí](https://packages.debian.org/jessie/libnss3-tools): _a set of tools on top of the Network Security Service libraries_.
- `sudo apt install openjdk-11-jre-headless` instala Java. `java --version`
- `sudo dpkg -i AutoFirma_1_6_5.deb` instala el programa. `AutoFirma` en la terminal lo abre.

## Entorno de desarrollo

### [RVM](https://rvm.io/) y Ruby

Es un gestor de paquetes de Ruby. Para instalarlo hay que instalar previamente `gpg2`. GnuPG es la versión libre de PGP (_Pretty Good Privacy_). Sirve para cifrar un archivo que se podrá mandar con la seguridad de que nadie lo podrá leer excepto el que tenga la clave pública.

Después instalamos Ruby 2.6.5 con `rvm install 2.6`. Con `rvm list` listamos los paquetes instalados y con `ruby --version` chequeamos la versión actual de Ruby. Estos programas se han instalado coyunturalmente: `gawk, g++, gcc, autoconf, automake, bison, libc6-dev, libffi-dev, libgdbm-dev, libncurses5-dev, libsqlite3-dev, libtool, libyaml-dev, make, sqlite3, zlib1g-dev, libgmp-dev, libreadline-dev, libssl-dev`.

Cada vez que entremos en Terminal habrá que ejecutar `source /home/anerodata/.rvm/scripts/rvm` para usar Ruby.

### [NVM](https://github.com/nvm-sh/nvm) y Node

Tal y como lo tenemos en [Civio](https://github.com/civio/infra-management/wiki/Development-environment#python):

```
$ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.2/install.sh | bash
```

Si en `.bashrc` no tenemos ya esto escrito, debemos escribirlo:

```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
```

Ahora, en la terminal:

```
$ source ~/.bashrc
$ nvm install 14.15
```

Instalamos la 14.15 porque tiene _Long Term Support_. Si todo está instalado correctamente, cerramos la terminal y en una nueva veríamos:

```
$ node --version
v14.15.3
```

### [pyenv](https://github.com/pyenv/pyenv-installer#installation--update--uninstallation)

Uso `pyenv` como gestor de paquetes de Python. Para instalar ejecutamos en la terminal:

```
$ curl https://pyenv.run | bash
```

Después añadimos a `~/.bashrc`

```
# Load pyenv
export PATH="/home/anerodata/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Instalo la versión de Python 3.7.5:

```
$ pyenv install 3.7.5
```

Para poder verla instalada:

```
$ pyenv versions
3.7.5
```

Para hacerla global:

```
$ pyenv global 3.7.5
```

`$ pyenv help global` para más información sobre esto.

Ya podemos usar esa versión de python ejecutando en la terminal `python`.

Conviene actualizar `pip` ejecutando:

```
$ pip install --upgrade pip
```


## Editores de texto

### Vim

`sudo apt install vim`

Versión renovada de Vi:

- Está instalado en casi todas las distribuciones de tipo Unix. Por lo tanto se puede utilizar para editar ficheros en un servidor remoto mediante SSH.
- No necesita un _desktop environment_.
- Tiene características chulas y permite rápidamente editar un fichero.

### Sublime

`sudo snap install sublime-text`

## Instalando otros programas

### Spotify

Con `snap install spotify`.

### Chrome

Descargarlo de la [web](https://www.google.com/intl/es/chrome/) y `clamscan file.deb` para ver si está infectado, después `sudo dpkg -i file.deb`.

## Otros

- Sincronizar Ubuntu con Google Drive es [bastante sencillo](https://cambiatealinux.com/instalar-google-drive-en-ubuntu).
