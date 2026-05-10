# Backend de Lollevo Get

Este directorio contiene el servidor backend construido con
[FastAPI](https://fastapi.tiangolo.com/). Su función es recibir imágenes, analizarlas
(en este ejemplo de forma simulada) y devolver información estructurada sobre el
producto, coincidencias en tiendas en línea y un precio sugerido.

## Estructura

- `main.py`: punto de entrada del servicio. Define la API REST con un endpoint `/scan`
  que acepta una imagen y devuelve un objeto JSON con la detección simulada.
- `requirements.txt`: dependencias necesarias para ejecutar el servidor.

## Ejecución

Para iniciar el servidor localmente:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Luego de iniciar, el endpoint principal estará disponible en
`http://localhost:8000/scan`. Puedes probarlo con [HTTPie](https://httpie.io/) o
[curl](https://curl.se/):

```bash
curl -X POST -F "file=@ruta/de/la/imagen.jpg" http://localhost:8000/scan
```

## Cómo extender

Para integrar capacidades reales de reconocimiento de productos, podrías:

1. Conectar la carga de imágenes con un servicio de visión por computador que
   devuelva etiquetas, descripciones, códigos de barra o textos extraídos.
2. Implementar una búsqueda inversa en la web utilizando API de terceros para
   obtener páginas donde se vende el producto y extraer precios.
3. Aplicar reglas de negocio para calcular el precio de venta en pesos dominicanos
   tomando en cuenta costos de importación, comisiones, impuestos y márgenes.
