# Lollevo Get

Lollevo Get es una herramienta de escaneo de productos orientada a emprendedores que desean
identificar artículos, comparar precios en línea y obtener una sugerencia de precio de venta en
pesos dominicanos. Este proyecto proporciona una estructura básica para un sistema modular
compuesto por un backend y un frontend. El backend expone una API que acepta imágenes
subidas por el usuario y devuelve información detectada del producto, coincidencias de
marketplaces y un precio de venta sugerido. El frontend ofrece una interfaz web móvil (PWA)
que permite tomar o subir una foto, enviar la imagen al servidor y mostrar los resultados.

> **Advertencia**: La lógica de reconocimiento de imágenes, extracción de datos de páginas
> web y cálculo de precios se implementa como marcadores de posición. Esta versión no
> consulta servicios externos reales ni realiza scraping; solo demuestra cómo integrar
> componentes y sirve de base para desarrollos futuros.

## Estructura del proyecto

```
lollevo-get/
├── backend/           # Implementación de la API con FastAPI
│   ├── main.py        # Punto de entrada del servidor
│   ├── requirements.txt
│   └── README.md
├── frontend/          # Aplicación web progresiva (PWA)
│   ├── index.html
│   ├── manifest.json
│   └── README.md
└── README.md          # Este documento
```

## Configuración rápida

1. **Clonar el repositorio** (o descargar los archivos) y cambiar al directorio del proyecto.
2. Levantar el backend:
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
3. Abrir el archivo `frontend/index.html` en el navegador o servirlo con cualquier
   servidor web estático. Asegúrate de que el navegador pueda acceder a
   `http://localhost:8000/scan` (o al puerto configurado) desde el frontend.

## Cómo funciona

1. **Carga/escaneo de imagen**: el usuario selecciona o captura una foto del producto en la
   interfaz web.
2. **Envío al backend**: la imagen se envía al endpoint `/scan` del servidor FastAPI.
3. **Análisis y coincidencias**: en esta versión el servidor devuelve datos simulados
   (nombre detectado, categoría, material, uso, lista de tiendas donde se vende y precio
   sugerido). En una implementación real, aquí se integrarían servicios de visión por
   computador, APIs de búsqueda, scraping de precios y lógicas de costos.
4. **Presentación de resultados**: el frontend muestra la información del producto, las
   coincidencias y el precio sugerido al usuario.

## Próximos pasos

Este proyecto es un punto de partida. Para una solución completa considera:

- Integrar un servicio de reconocimiento de imágenes (por ejemplo, Google Vision,
  Azure Cognitive Services u OpenAI Vision API) que devuelva descripciones, etiquetas y
  marcas.
- Implementar un motor de búsqueda inversa para localizar el producto en diferentes
  marketplaces. SerpApi, Google Lens (a través de proxies) o APIs de marketplaces como
  eBay Browse pueden ser opciones.
- Realizar scraping de precios con técnicas de extracción permitidas y respetando los
  términos de uso de cada sitio web.
- Calcular costos de importación (envíos, aduanas, comisiones) y márgenes de beneficio
  para obtener precios sugeridos más realistas.
- Añadir una base de datos para almacenar productos escaneados, historiales de precios
  y catálogos internos.
- Convertir el frontend en un paquete instalable (PWA) y añadir funciones offline
  mediante Service Workers.

## Licencia

MIT License. Consulta el archivo `LICENSE.md` para más detalles.
