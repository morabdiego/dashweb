# pyBCRAdata-dashboard

Este sitio web es una demostración de cómo utilizar **[pyBCRAdata](https://pypi.org/project/pyBCRAdata/)**, una librería de Python diseñada para facilitar el acceso a las APIs públicas del Banco Central de la República Argentina (BCRA). Desarrollado íntegramente en Python con [Reflex](https://reflex.dev/), este dashboard interactivo permite obtener y visualizar datos económicos de manera eficiente y reproducible.

## ¿Qué es pyBCRAdata?

`pyBCRAdata` proporciona una interfaz sencilla para interactuar con las APIs oficiales del BCRA, que forman parte de su estrategia de Open Finance. Estas APIs ofrecen acceso a información clave como:

- **Principales Variables**: series estadísticas del Informe Monetario Diario, incluyendo datos sobre base monetaria, reservas internacionales, tasas de interés, entre otros.
- **Estadísticas Cambiarias**: cotizaciones de divisas y su evolución histórica.
- **Cheques Denunciados**: información sobre cheques denunciados como extraviados, sustraídos o adulterados.
- **Central de Deudores**: datos consolidados sobre financiaciones otorgadas y cheques rechazados por CUIT/CUIL/CDI.

Estas interfaces están diseñadas para integrarse fácilmente en diversas plataformas y sistemas, permitiendo automatizar análisis frecuentes y mejorar la accesibilidad a la información financiera ([bcra.gob.ar](https://www.bcra.gob.ar/BCRAyVos/catalogo-de-APIs-banco-central.asp?)).

## Objetivo del sitio

Este dashboard interactivo tiene como finalidad ilustrar cómo se pueden descargar y visualizar datos económicos en un entorno 100% Python. A través de `pyBCRAdata` y Reflex, es posible:

- Acceder a datos económicos de forma sencilla.
- Crear visualizaciones personalizadas.
- Si desea querys personalizados acceder directamente a `pyBCRAdata` en local

A continuación, se muestra un ejemplo básico del código utilizado para obtener y visualizar una serie de las Reservas Internacionales del BCRA:

```python
import reflex as rx
from pyBCRAdata import monetary

from web.components.area_chart import chart_generator

# Obtener datos de la API
df = monetary.series(
    # Reservas internacionales en millones de dólares
    id_variable="1",
    desde="2025-01-01",
    hasta="2025-04-01"
)[["fecha", "valor"]]  # Filtrar columnas relevantes

# Adaptar datos para el módulo de gráficos de Reflex
data_to_chart = df.to_dict(orient="records")

# Con un estilo predefinido anteriormente, creamos el gráfico
def reservas_internacionales_viz() -> rx.Component:
    return chart_generator(
        data=data_to_chart,
        color="#8884d8"
    )
```

Este ejemplo muestra cómo, con unas pocas líneas de código, se puede construir una visualización interactiva directamente desde Python, sin necesidad de herramientas web como HTML, CSS o JavaScript.
