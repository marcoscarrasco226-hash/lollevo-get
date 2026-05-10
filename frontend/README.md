# Frontend de Lollevo Get

Este directorio contiene una interfaz web simple que actúa como la cara de
Lollevo Get. Se trata de un prototipo de aplicación web progresiva (PWA)
capaz de funcionar en navegadores móviles y de escritorio. Permite al
usuario seleccionar o capturar una imagen, enviarla al backend y visualizar
la información de producto devuelta.

## Archivos

- `index.html`: página principal con la interfaz de usuario, estilos básicos y
  lógica JavaScript. El formulario carga una imagen y realiza una solicitud
  a la API del backend (`/scan`).
- `manifest.json`: manifiesto PWA que especifica cómo se instala la
  aplicación (nombre, colores, etc.).

En un proyecto más elaborado añadirías service workers y manejo offline,
estilos avanzados y componentes de UI reutilizables.
