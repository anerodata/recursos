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

## 11 - File System Tree

1. Does the file /bin/cat exist ? What about /bin/dd and /bin/echo. What is the type of these
files ?

Yes, these files are the binaries. Programs executables in the command line

```
ls /bin/cat ; file /bin/cat
ls /bin/dd ; file /bin/dd
ls /bin/echo ; file /bin/echo
```

2. What is the size of the Linux kernel file(s) (vmlinu\*) in /boot ?

```
ls -h /boot/vm*
```

9.8MB

3. Create a directory ~/test. Then issue the following commands:

```
cd ~/test
dd if=/dev/zero of=zeroes.txt count=1 bs=100
od zeroes.txt
```

dd will copy one times (count=1) a block of size 100 bytes (bs=100) from the file /dev/zero
to ~/test/zeroes.txt. Can you describe the functionality of /dev/zero ?

Is a programm that offers as many zeros as request. [More information](https://es.wikipedia.org/wiki//dev/zero).

> /dev/zero is a Linux special device. It can be considered a source of zeroes. You cannot send something to /dev/zero, but you can read zeroes from it.

4. Now issue the following command:
```
dd if=/dev/random of=random.txt count=1 bs=100 ; od random.txt
```

dd will copy one times (count=1) a block of size 100 bytes (bs=100) from the file /dev/ random to ~/test/random.txt. Can you describe the functionality of /dev/random ?

Generate a random number of bytes

5. Issue the following two commands, and look at the first character of each output line.
```
ls -l /dev/sd* /dev/hd*
ls -l /dev/tty* /dev/input/mou*
```
The first ls will show block(b) devices, the second ls shows character(c) devices. Can you
tell the difference between block and character devices ?

The first ones represent hardware devices, the second one, consoles or command line interface

> Block devices are always written to (or read from) in blocks. For hard disks, blocks of 512 bytes are common. Character devices act as a stream of characters (or bytes). Mouse and keyboard are typical character devices.

6. Use cat to display /etc/hosts and /etc/resolv.conf. What is your idea about the purpose
of these files ?

```
/etc/hosts contains hostnames with their ip address
```

```
/etc/resolv.conf should contain the ip address of a DNS name server.
```

7. Are there any files in /etc/skel/ ? Check also for hidden files.

There are `.bash_logout`, `.bashrc` and `.profile`

8. Display /proc/cpuinfo. On what architecture is your Linux running ?

```
Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz
```

9. Display /proc/interrupts. What is the size of this file ? Where is this file stored ?

The size is 0

> The size is zero, yet the file contains data. It is not stored anywhere because /proc is a
virtual file system that allows you to talk with the kernel. (If you answered "stored in RAM-
memory, that is also correct...).

10. Can you enter the /root directory ? Are there (hidden) files ?

No, you need sudo credentials

With sudo you have these hidden files:


```
.bash_history  .bashrc  .cache  .config	.dbus  .fnmt  .local  .profile snap  .viminfo
```

11. Are ifconfig, fdisk, parted, shutdown and grub-install present in /sbin ? Why are these
binaries in /sbin and not in /bin ?

Because they are system binaries.
> Because those files are only meant for system administrators.

12. Is /var/log a file or a directory ? What about /var/spool ?

Both are directories

`/var/log` contains the different logs of the system

`/var/spool/` contains the cronjobs

13. Open two command prompts (Ctrl-Shift-T in gnome-terminal) or terminals (Ctrl-Alt-F1,
Ctrl-Alt-F2, ...) and issue the who am i in both. Then try to echo a word from one terminal
to the other.

14. Read the man page of random and explain the difference between /dev/random and /
dev/urandom.

```
echo Hello from the first > /dev/pts2
echo Hello from the second > /dev/pts1
```

Both provides an interface to the kernel's random number generator. `/dev/random` has major device number 1 and minor device number 8.
`/dev/urandom` has major device number 1 and minor device number 9

`/dev/urandom` is slower
