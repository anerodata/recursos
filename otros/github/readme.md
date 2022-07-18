Curso básico de Git y Github
=======
Git es una herramienta de control de versiones. Se utiliza para documentar procesos de trabajo. Github es un portal para subir a la red el repositorio creado previamente con Git con el objetivo de ponerlo en común con otras personas

## 1 - Comandos básicos
1. `git init`: sirve para iniciar git dentro de un directorio

2. `git status`: sirve para conocer el estado actual de nuestro repositorio

3. `git add nombre_fichero`: añade al area de almacenamiento un fichero que se encuentra en el directorio de trabajo. Cada vez que cambiamos un fichero y guardamos, hay que usar este comando. Si usamos un punto (.) en lugar de nombre_fichero añadiremos todos los ficheros al area de almacenamiento a la vez

4. `git checkout -- nombre_fichero`: retrocede el cambio efectuado, de manera que no hará falta correr git add nombre_fichero. Sería como hacer ctrl + z

5. `git diff nombre_fichero`: ver como ha cambiado el fichero antes de hacer git add sobre el

6. `git commit`: registra los cambios y añade los ficheros en su nueva versión al repositiorio. Hace un snapshot de la última versión del proyecto con sus cambios y modificaciones. Hay que darle un nombre a cada commit

7. `git commit -m "nombre del cambio"`: Hace lo mismo que el comando anterior sin abrir el fichero de commits

8. `git log`: muestra un registro con todas las versiones del repositorio 

9. `git checkout 43ea714582cb136a75813552fb85429628d67576` la cifra se refiere al hash del commit y permite retroceder a una versión anteriormente trackeada de nuestro repositorio

10. `git checkout master`: habiendo retrocedido a otra versión, nos devuelve al ultimo commit efectuado, la versión más reciente. Estando en otra rama distinta, nos permite cambiar a master

## 2 - Subiendo el repositorio a Github
1. `git remote add origin https://github.com/anerodata/curso-github.git`: vincula el repositorio local a ese repositorio online

2. `git push -u origin master`: subimos todos los cambios al repositorio remoto https://github.com/anerodata/curso-github.git vinculado al que tenemos en local

3. `git clone https://github.com/anerodata/curso-github.git`: descarga el repositorio online y lo deja en local

4. `git pull`: sirve para traerte todos los cambios del repositorio online al repositorio local 

Este [video](https://www.youtube.com/watch?v=HiXLkL42tMUde) de youtube está bastante bien para iniciarse

5. Estando fuera de `master`, y tras comitear, `git push --set-upstream origin branch-name` crea y establece en el repositorio remoto el nombre de la rama como destino y "empuja" los cambios hacia ella.

6. Como comentan en [Freecodecamp](https://www.freecodecamp.org/news/git-checkout-remote-branch-tutorial/#3pullchangesfromaremotebranch) `git checkout -b fix-failing-tests origin/fix-failing-tests` Crea la rama `fix-failing-tests`, tira de los cambios en la rama remota `fix-failing-tests` y nos cambia a ella

## 3 - Rama gh-pages 

Como documenta [flowsta](https://github.com/flowsta/github#rama-gh-pages), si nuestro repositorio es un proyecto web, podemos mostrarlo gracias a la rama gh-pages de github:

1. `git checkout -b gh-pages` crear rama gh-pages y cambiar de master a gh-pages

2. `git merge master` poner todo el contenido de master en gh-pages

3. `git push -u origin gh-pages` empujar los cambios locales a la rama gh-pages

4. Para tener la rama master y la rama gh-pages avanzando en paralelo añadimos estas dos lineas bajo [remote "origin"] en .git/config:

`push = +refs/heads/master:refs/heads/gh-pages`

`push = +refs/heads/master:refs/heads/master`

Ahora tendríamos el proyecto web renderizando en https://nombre-de-usuario.github.io/nombre-del-repositorio/
