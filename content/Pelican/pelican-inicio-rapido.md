Title: Pelican - Inicio Rápido
Summary: Inicia con Pelican para generar tu página
Category: Pelican
Tags: Pelican, CMS

# Pelican, inicio rápido.

[Pelican](https://blog.getpelican.com/) es un generador de sitios estáticos escrito en [Python](https://www.python.org/), sus caracteísticas principales incluyen:

*   Escribe tu contenido en [reStructuredText](https://docutils.sourceforge.net/rst.html) o en [Markdown](daringfireball.net/projects/markdown/)
*   Tiene una simple herramienta CLI para (re)generar el sitios
*   Interface simple con control de versiones distribuido y web hooks
*   Salida completamente estática fácil de hospedar donde sea.

## Documentación
La documentación completa se encuentra en [https://docs.getpelican.com](https://docs.getpelican.com)

## TL;DR

Los pasos a seguir para empezar a usar Pelican son los siguientes.

### Instalación
```
pip install pelican markdown
```
Esto instalará Pelican y markdown por si piensas utilizarlo así.

### Crear un Proyecto

```
mkdir -p ~/proyectos/tuSitio
cd ~/proyectos/tuSitio
```
### Crear el esqueleto del proyecto
```
pelican-quickstart
```

esto te hará algunas preguntas sobre tu proyecto para configurarlo de la forma adecuada.

### Crear un artículo

No puedes crear tu sitio sin haber creado un artículo primero, entonces crea un archivo en `~/proyectos/tuSitio/content/` llamado `articulo1.md` con el siguiente contenido:

```
Title: My First Review
Date: 2017-11-15 12:00
Category: Categoría

Este es mi primer artículo
```
Nota que este tipo de archivos acepta Markdown y tiene ya algunos metadatos como titulo, fecha y categoría.

Estos metadatos son tomados por Pelican al generar el artículo.

Para crear mas artículos, solo hay que crear mar archivos `.md` dentro de la carpera `content/` en el proyecto.

### Generar el sitio

Desde el directorio base del proyecto, en este caso `~/proyectos/tuSitio/` ejecuta
```
pelican content
```
El sitio ha sido generado en la carpeta `output/`

### Ver tu sitio

Desde la carpeta `output/` ejecuta
```
python -m pelican.server
```

Ahora puedes ver tu sitio en [https://localhost:8000/]( https://localhost:8000/)
