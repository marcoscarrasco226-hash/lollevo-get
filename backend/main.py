"""
Backend para Lollevo Get
========================

Este módulo implementa un servidor REST utilizando FastAPI. Exponemos un
endpoint principal (`/scan`) que acepta la subida de una imagen y devuelve
información simulada del producto analizado. La lógica actual es un marcador
de posición que debería sustituirse por integraciones reales con servicios
de visión artificial y scraping de marketplaces.

Estructura del endpoint `/scan`:

- **Método**: POST
- **Parámetro**: `file` (archivo de imagen)
- **Respuesta**: objeto JSON con el nombre detectado, categoría, material,
  uso, coincidencias en tiendas y precio recomendado en pesos dominicanos.

Nota: se agrega CORS abierto para permitir solicitudes desde cualquier
origen; en un despliegue real, configura los orígenes permitidos según tu
frontend.
"""

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI(title="Lollevo Get Backend",
              description="API de escaneo de productos para Lollevo Get",
              version="0.1.0")

# Permitir CORS para cualquier origen por simplicidad. Ajusta en despliegues reales.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class StoreMatch(BaseModel):
    """Representa una coincidencia de producto en una tienda en línea."""

    store: str
    price_usd: float
    price_dop: float
    url: str = ""  # URL de la página del producto, si se conoce


class ScanResponse(BaseModel):
    """Modelo de respuesta para el endpoint de escaneo."""

    detected_name: str
    category: str
    material: str
    use_case: str
    matches: List[StoreMatch]
    price_suggested_dop: float


@app.post("/scan", response_model=ScanResponse)
async def scan_product(file: UploadFile = File(...)):
    """
    Procesar una imagen subida y devolver datos simulados del producto.

    En una implementación real, aquí se integraría la lógica de visión por
    computador para identificar el producto y servicios de búsqueda para
    obtener coincidencias y precios reales.
    """
    # Validar tipo de archivo
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="El archivo debe ser una imagen")

    # Leer archivo (no se usa en esta implementación)
    await file.read()

    # Lógica simulada para la demostración
    detected_name = "Producto de ejemplo"
    category = "Categoría de ejemplo"
    material = "Material desconocido"
    use_case = "Uso sugerido del producto"
    matches = [
        StoreMatch(store="Tienda A", price_usd=20.50, price_dop=1200.0, url="https://ejemplo.com/producto-a"),
        StoreMatch(store="Tienda B", price_usd=19.99, price_dop=1150.0, url="https://ejemplo.com/producto-b"),
    ]
    # Supongamos que calculamos un precio sugerido
    price_suggested_dop = 1500.0

    return ScanResponse(
        detected_name=detected_name,
        category=category,
        material=material,
        use_case=use_case,
        matches=matches,
        price_suggested_dop=price_suggested_dop,
    )
