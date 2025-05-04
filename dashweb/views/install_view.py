import reflex as rx

def install_content() -> rx.Component:
    """Generate the installation content."""
    return rx.markdown(
        """
        # **PyBCRAdata dashboard**
        
        Esta web fue desarrollada con el framework [Reflex](https://reflex.dev/) y el paquete [pyBCRAdata](https://pypi.org/project/pyBCRAdata/) y es un ejemplo de cómo utilizar la librería para acceder a datos del Banco Central de la República Argentina (BCRA).
        
        # **Instalación de pyBCRA**
        **Con el paquete de PyPI** podrás acceder a estadísticas monetarias, datos de tipo de cambio e información de deudores publicados por el **Banco Central de la República Argentina (BCRA)** y utilizarlo en tu proyecto.

        ### 🛆 Instalación
        Para instalar la librería, ejecuta el siguiente comando en tu terminal:

        ```bash
        pip install pyBCRAdata
        ```

        **Requisitos:**
        - Python 3.7 o superior
        - Bibliotecas [pandas](https://pandas.pydata.org/) y [requests](https://docs.python-requests.org/)

        Consulta la [documentación de instalación](https://github.com/morabdiego/pyBCRA/blob/main/docs/installation/installation.md) para más detalles.

        ### 📊 Ejemplo Rápido
        ```python
        from pyBCRAdata import (
        monetary, currency, checks, debtors
        )

        # Obtener variables monetarias
        variables = monetary.variables()

        # Obtener cotización por fecha de todas las divisas
        cotizacion = currency.rates(fecha="2024-01-01")

        # Obtener entidades bancarias
        bancos = checks.banks()

        # Consultar deudores
        deudas = debtors.debtors(identificacion="12345678")
        ```

        O utilizando el cliente completo:

        ```python
        from pyBCRAdata import BCRAclient

        # Inicializar cliente
        client = BCRAclient()

        # Obtener tasa de política monetaria
        df = client.monetary.series(
            # Tasa de Política Monetaria (en % n.a.)
            id_variable="6",
            desde="2024-01-01",
            hasta="2024-03-21"
        )
        print(df.head())

        # Obtener cotización histórica del dólar
        usd = client.currency.series(
            moneda="USD",
            fechadesde="2024-01-01",
            fechahasta="2024-03-21"
        )
        print(usd.head())
        ```

        Consulta más información en el [repositorio oficial de GitHub](https://github.com/morabdiego/pyBCRA).
        """
    )