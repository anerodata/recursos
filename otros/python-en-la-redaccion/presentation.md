---
theme: gaia
\_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
---

# Buceando en las cloacas con Python

---
<style type="text/css" rel="stylesheet">
img {
   width:700px;
}
</style>

### Sobre mi _background

- Graduado en periodismo y especialización en análisis de datos
- Después, un intruso en desarrollo web
- Desarrollador web en
  - Unidad de datos de [El Confidencial](https://elconfidencial.com)
  - [Fundación Ciudadana Civio](https://civio.es/)

---

### Python  en un medio de comunicación

_Scripts_ sencillos normalmente basados en programación funcional

- Rascar data de HTML y PDF ([requests](https://docs.python-requests.org/en/latest/), [bs4](https://pypi.org/project/bs4/), [selenium](https://www.selenium.dev/)).
- Análisis de grandes _datasets_ ([pandas](https://pandas.pydata.org/))

Habitualmente, en **investigaciones elaboradas con tiempo** 🔎 , aunque también en artículos del día a día o piezas de **servicio público** 📈 y **aplicaciones internas** de apoyo a periodistas 🤓

---

## Investigaciones 🔎

---

### [Metro inaccesible](https://www.elconfidencial.com/espana/madrid/2019-09-06/metro-accesible-paradas-ascensor-escaleras_2209007/)

Datos obtenidos gracias a un rascado diario de la web de [incidencias del metro](https://www.metromadrid.es/es/linea/) 

---

### [Más público que Netflix y miles de reseñas de puteros: así es el gran barrio rojo 'online'](https://www.elconfidencial.com/tecnologia/2018-09-25/prostitucion-anuncios-portales-pasion-mileroticos_1620413/)

Datos obtenidos gracias a un rascado de los portales de []() y []()

---

### [Así abusa de los microcontratos a dedo la Comunidad de Madrid: 1 millón en dos años](https://www.elconfidencial.com/espana/madrid/2018-06-04/comunidad-de-madrid-contratos-menores_1572865/)

Datos obtenidos gracias a un rascado del [buscador avanzado de contratos de la CAM](http://www.madrid.org/cs/Satellite?cid=1224915242285&language=es&pagename=PortalContratacion%2FPage%2FPCON_buscadorAvanzado)

---

### [El 80% de las ofertas de trabajo oculta el salario: "Es otra forma de explotación"](https://www.elconfidencial.com/empresas/2018-09-24/salario-sueldo-ofertas-de-trabajo-empleo-paro_1618954/)

Datos obtenidos gracias a un rascado del [portal público de empleo](https://www.empleate.gob.es/empleo/#/trabajo?search=programador&pag=0)

---

## Servicio público 📈

---

### [De qué año es tu casa](https://www.elconfidencial.com/vivienda/2019-11-26/mapa-espana-urbanismo-edificios-historia_2348415/)

Uso de `geopandas.py` para generar la capa de polígonos con la
información para cada parcela.

---

### Temas de posicionamiento SEO

- [Estos son los candidatos de los partidos políticos a las elecciones generales del 10N](https://www.elconfidencial.com/espana/2019-11-10/candidaturas-elecciones-generales-0_2275855/)

- [Candidaturas a las elecciones municipales de 2019: estas son todas las listas locales](https://www.elconfidencial.com/elecciones-municipales-y-autonomicas/2019-05-26/candidaturas-listas-eleciones-municipales-2019_1991950/)

---
