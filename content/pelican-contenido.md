Title: Crear contenido con Pelican
Summary: Agrega contenido a tu página en Pelican.
Category: Pelican
Tags: Pelican, CMS

## Agrégale contenido a tu página en Pelican

Después de la [introducción a Pelican]({filename}/pelican-inicio-rapido.md) podemos empezar a ver como agregar mas contenido y darle un poco mas de forma al sitio.

## Páginas y artículos

Pelican considera que los "artículos" son contenido cronológico, como entradas en un blog y por ende están asociados con una fecha.

La idea detrás de las "páginas" es que usualmente no tienen una naturaleza temporal y son utilizadas para contenido que no cambia con frecuencia., por ejemplo las páginas "Quienes somos" o "Contactanos".

## Estructura de la página

Generalmente los proyectos hechos con Pelican llevan la siguiente estructura de archivos

```
sitio/
├── content
│   ├── category/
│   │   └── articulo1.rst
│   ├── articulo2.md
│   └── pages
│       └── acerca.md
└── pelican.conf.py
```

Note que los artículos y las páginas van dentro de la carpeta `content`, los artículos peuden ir dentro de esa carpeta sueltos y laspáginas necesitan otra carpeta llamada `pages`.

Asegúrate de agregar los metadatos tanto en artículos como páginas para que Pelican pueda convertirlos.

## Metadatos

 Los metadatos típicos son los siguientes:

 ```
Title: Mi súper título
Date: 2010-12-03 10:20
Modified: 2010-12-05 19:30
Category: Python
Tags: pelican, publishing
Slug: my-super-post
Authors: Alexis Metaireau, Conan Doyle
Summary: Versión corta para el index y feeds

Este es el contenido de mi artículo

 ```
Nota que además del título, todos los metadatos son opcionales, por ejemlo, si no hay `date` y la configuración `DEFAULT_DATE` es igual a `'fs'`, la fecha de creación del archivo es utilizada para generar la fecha del artículo.

## Utlizar borradores

Es posible crear artículos y páginas que no son publicados inmediatamente, por ejemplo para que algún colega los revise antes, para esto lo que hay que hacer es agrear un metadato `Status: draft` y el artículo se agegará a el folder `drafts`.

Si quieres que todos los artículos se creen como borrador inmediatamente puedes agregarlo ne la configuración así:

```
DEFAULT_METADATA = {
    'status': 'draft',
}
```
