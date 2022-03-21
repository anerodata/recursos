Para convertir el fichero MD a PDF. Es necesario:

1. Habiendo instalado `npm`, iniciamos `npm`:

```
npm init
```

2. Instalar la herramienta de línea de comandos [Marp](https://marp.app/):

```
npm install --save-dev @marp-team/marp-cli
```

3. Y ejecutar este comando:

```
npx @marp-team/marp-cli --allow-local-files presentation.md -o presentation.pdf
```
