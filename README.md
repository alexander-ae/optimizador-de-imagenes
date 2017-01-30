# optimizador-de-imagenes
Script en python que optimiza las imágenes en un directorio mediante otras herramientas especializadas.

## Dependencias

* Python 2 o Python 3
* pngquant: https://pngquant.org/
* mozjpeg: https://github.com/mozilla/mozjpeg
* ImageMagic: https://www.imagemagick.org/script/convert.php

## Uso

Descargar el script y ejecutarlo directamente:

```
odi.py [-h] [-v] input [output]

positional arguments:
  input       Directorio que contiene los archivos de entrada
  output      Directorio destino de las imágenes optimizadas, por defecto
              genera la salida en el directorio "output"

optional arguments:
  -h, --help  show this help message and exit
  -v          ejemplo: -v o -vv
```

## Imágenes de Prueba

### PNG

* Música Placa Giratoria Nostalgia - Pixabay : https://pixabay.com/es/m%C3%BAsica-placa-giratoria-nostalgia-1727912/
* Calophyllum antillanum - Wikimedia : https://es.m.wikipedia.org/wiki/Archivo:Calophyllum_antillanum_(Palo_Mar%C3%ADa)_picture_1.png
* Ninja - Pixabay : https://pixabay.com/es/negro-ninja-espadas-m%C3%A1scaras-307983/#

### JPG

* Vendimia Retro Istambul - Pixabay : https://pixabay.com/es/vendimia-retro-istanbul-viejo-amor-1872683/
* Mevagissey Firework Display - StockSandwich : https://stocksandwich.com/media/mevagissey-firework-display
* Biblioteca - Freejpg : http://www.freejpg.com.ar/free/info/100007727/biblioteca
* Silhouette Male Man - Avopix : https://avopix.com/photo/12358-silhouette-male-man
* Sea - Cupcake : http://cupcake.nilssonlee.se/


## Resultados

Para las imágenes de prueba indicadas anteriormente:

|     | Entrada | Salida |
|-----|---------|--------|
| JPG | 11.8 MB | 2.0 MB |
| PNG | 3.3 MB  | 1.0 MB |

**Nota:** Los resultados finales pueden variar según el tipo de imágenes utilizadas.
