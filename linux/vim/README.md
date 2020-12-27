# Vim	
Se sigue [este tutorial de DistroTube](https://www.youtube.com/watch?v=ER5JYFKkYDg&ab_channel=DistroTube)
Un sistema operativo instalado en casi todas las distribuciones de tipo UNIX. A veces viene Vi, su versión antigua.
Un recurso chulo para aprender Vim es https://vim-adventures.com.
En el Terminal introduciendo `vimtutor` vamos al tutorial de vim.

Las teclas para mover el cursor tradicionalmente son h(izquierda)j(abajo)k(arriba)l(derecha). Estas teclas mueven el cursor a través de las líneas lógicas que existen, que a veces ocupan más de dos renglones. Si quisieramos desplazarnos a través de las líneas visuales tendríamos que hacer `g + j` (para abajo), y así sucesivamente.

Para salir pulsamos `:` para llevarnos al modo comando e introducimos `quit` o `q` para salir. Si hemos hecho cambios `:wq` para salir y guardar o `:q!` para salir sin guardar. Una manera chula de hacer un `:wq` es el atajo `ZZ`

Vim es un editor de texto modal. Tiene modos:

1. **Modo normal**: puedes navegar con las teclas de cursor, copiar, pegar, marcar comandos como el `ZZ`, el `gg` que te lleva a lo alto del fichero, el `SHIFT+g` que te lleva a la última línea. Otros atajos:

- `$` te lleva al final de una línea
- `0` te lleva al principio de una línea.
- `2 + SHIFT G` te lleva a la segunda línea.
- `u` es _undo_. `3 + u` hace 3 undos seguidos.
- `CTRL + r`, _redo_.
- `d + w` borra la palabra
- `d + $` borra desde el cursor hasta el final. Es como hacer `SHIFT +d`
- `x` es como `ins`. Borra el caracter detrás del cursor.
- `2 + x` borra 2s caracteres.
- `d + d` borra la línea entera. `3 + d` borra las tres siguientes lineas
- `w` nos deplazamos rápidamente, palabra por palabra hacia el primer caracter
- `e` nos desplazamos palabra por palabra hacia el último caracter
- `3 + w` nos desplazamos tres palabras más allá
- `b` es el contrario, nos desplaza al primer caracter de la palabra anterior. `3 + b`, igual pero con tres palabras
- Este incremento también funciona con las teclas `hjkl`.
- `p` o _put_. Coloca lo que hayamos `borrado` con `d` en donde estemos. Esto es como hacer _copy/paste_. Es igual que `C`.
- `r + caracter` reemplaza el caracter en el que estemos con el cursor por otro.
- `c` es _change_. `c + e` borra todos los caracteres desde el cursor hasta el final de la palabra y nos mete en el modo insertar para reemplazar la palabra
- `c + $` para cambiar toda la línea. Es como hacer `SHIFT + c`
- `c + w` borra la palabra y te introude en el modo insertar es igual que `c + e`.


Tanto la `b` como la `w`, o la `e` tienen su versión `SHIFT + b/w` para no tomar caracteres como , o paréntesis como si fueran palabras

- la `f` es como _for to..._: avanza hasta el caracter introducido después de la `f` en una misma línea. `SHIFT + f` hace lo mismo, pero para atrás.
- `t` y `SHIFT + T` se parecen mucho, solo que en vez se situarte sobre el próximo caracter, te situan en el caracter que precede
- `SHIFT + i` te lleva al principio de la línea y te mete en el modo insertar.
- `SHIFT + a` te lleva al final de la línea y te mete en el modo insertar.
- `a` te situa en el modo insertar en el caracter posterior al cursor
- `s` borra el caracter del cursor y te mete en el modo insertar.
- `SHIFT + s` borra toda la línea y te mete en el modo insertar.
- `o` crea una línea nueva siguiente a la que estamos y te introduce en insertar. `SHIFT + o` hace lo mismo, solo que en una línea anterior

El comando _yank_ es igual a hacer un _copy_:

- `y + w` copia la palabra y la pegamos con `p`.
- `y + y` copia una línea entera. Es como hacer `SHIFT + y`.
- `y + $` copia desde el cursor hasta el final de la línea.
- `%` Encuentra los parénteisis en una línea. 

Para puscar pulsamos `/` introducimos el término y pulsamos intro. Nos lleva a la primera ocurrencia. Luego pulsando `n`, vamos a las siguientes ocurrencias. `SHIFT + n` busca para atrás. Con `?` también se puede buscar, `n` y `N` funciona de manera cambiada aquí. Si quisieramos volver a la posición anterior una vez nos desplazamos con `n` podemos hacerlo con `CTRL + o` que retrocede el cursor a la posición anterior. `CTRL + i` después de haber hecho `CTRL o` nos devuelve a la posición más reciente.

Para reemplazar: 

- `:s/oldstring/newstring/g`: en el documento entero. 
- `:%s/oldstring/newstring/gc`: en el documento entero, pero con un prompt. 
- `:3,9s/oldstring/newstring/g`: en el documento entero.

Para cerrar, ejecutando `!ls` podemos listar el directorio en el que estamos desde la línea de comandos sin salirnos de Vim. Funcionaría para el resto de comandos de la Terminal.

Una pequeña documentación aparece para conocer qué comandos empiezan por una letra en cuestión cuando hacemos `:w CTRL + d`.

2. **Modo insertar**: con el atajo `i` se entra y con el atajo `esc` se sale. Mucha gente cambia este comando por la tecla `Bloq Mayus` o por `ii`.
3. **Modo visual**: con el atajo `v`.

## Instalando _plugins_

Desde la versión 8 de Vim, no es necesario instalar un gestor de _plugins_. Basta con seguir [estos pasos](https://coolaj86.com/articles/vim-8-plugins/) para activar el gestor de paquetes por defecto de Vim. El primer paso no ha sido necesario hacerlo en Ubuntu 20. Una vez hecho esto podemos instalar paquetes:

- [vim-colorscheme](https://github.com/flazz/vim-colorschemes): En el fichero `.vimrc` dentro de HOME. configuro `molokai` como el esquema de color por defecto así `colorscheme molokai`. Podría meter esta configuración en `/etc/vim/.vimrc` pero prefiero que solo este activo para mi usuario.

Sin embargo, es recomendable instalar un gestor de _plugins_. Uno de los [más recomendados](https://www.slant.co/topics/1224/~best-plugin-managers-for-vim) es [`vim-plug`](https://github.com/junegunn/vim-plug).

### Instalando el gestor de _plugins_ `vim-plug`

Instalamos `vim-plug` siguiendo [las instrucciones](https://github.com/junegunn/vim-plug#vim). Después, pegamos [estas líneas](https://github.com/junegunn/vim-plug#example) en `~/.vimrc`. Previamente hay que crear la carpeta `~/.vim/plugged` que es en donde se van a instalar los _plugins_. A continuación, pegamos el _plugin_ que queramos instalar. En mi caso [`Plug 'sickill/vim-monokai'`](https://github.com/sickill/vim-monokai). Después, introducimos en el mismo _script_ `:source%` para correrlo y `:PlugInstall` para instalar toda la lista. En el caso de que queramos instalar uno en concreto `:PlugInstall sickill/vim-monokai`.

Al final de `.vimrc` tengo inicializado el _plugin_ así `colorscheme monokai`.

El resto de comandos están en el README, pero destacan `PlugUpgrade` para actualizar el gestor y `PlugUpdate` para actualizar los _plugins_ instalados.
