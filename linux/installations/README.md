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

## Instalando otros programas

### Spotify

Con `snap install spotify`.

### Chrome

Descargarlo de la [web](https://www.google.com/intl/es/chrome/) y `clamscan file.deb` para ver si está infectado, después `sudo dpkg -i file.deb`.