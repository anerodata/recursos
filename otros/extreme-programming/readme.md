Para convertir el fichero MD a PDF. Es necesario:

1. Instalar el gestor de paquetes de Node NPM y la herramienta de línea de comandos Marp:

```
npm install --save-dev @marp-team/marp-cli
```

2. Y ejecutar este comando:

```
npx @marp-team/marp-cli --allow-local-files presentation.md -o presentation.pdf
```