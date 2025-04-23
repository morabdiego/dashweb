import reflex as rx
from pyBCRAdata import monetary, currency
import datetime

# Preparar listas y diccionario
variables = monetary.variables()
list_id = variables['idVariable'].to_list()
list_label = variables['descripcion'].to_list()
variable_dict = dict(zip(list_label, list_id))

# Preparar listas y diccionario para monedas
currencies = currency.currencies()
currency_codes = currencies['codigo'].to_list()
currency_names = currencies['denominacion'].to_list()
currency_dict = dict(zip(currency_names, currency_codes))

class BaseChartState(rx.State):
    """Base class for chart states with common functionality."""
    # Removed common data attribute to avoid shadowing
    start_date: str = datetime.date(datetime.date.today().year, 1, 1).strftime('%Y-%m-%d')
    end_date: str = datetime.date.today().strftime('%Y-%m-%d')
    
    def _fetch_data(self):
        """Abstract method to be implemented by subclasses."""
        pass
    
    @rx.event
    def set_start_date(self, date: str, prefix: str = ""):
        setattr(self, f"{prefix}start_date", date)
        self._fetch_data()
    
    @rx.event
    def set_end_date(self, date: str, prefix: str = ""):
        setattr(self, f"{prefix}end_date", date)
        self._fetch_data()
    
    @rx.event
    def on_load(self):
        self._fetch_data()


class MonetaryState(BaseChartState):
    selected_desc: str = list_label[0]
    series_data: list[dict] = []  # Renamed from 'data' to avoid shadowing

    def _fetch_data(self):
        """Fetch monetary data based on current state."""
        try:
            id_variable = variable_dict[self.selected_desc]
            df = monetary.series(
                id_variable=id_variable,
                desde=self.start_date,
                hasta=self.end_date
            )[['fecha', 'valor']]
            df['fecha'] = df['fecha'].dt.strftime('%Y-%m-%d')
            df = df.sort_values(by='fecha', ascending=True)
            self.series_data = df.to_dict(orient='records')
        except Exception as e:
            print(f"Error fetching monetary data: {e}")
            self.series_data = []

    @rx.event
    def on_load(self):
        """Override parent method to ensure proper initialization of monetary data."""
        self._fetch_data()

    @rx.event
    def set_series(self, value: str):
        self.selected_desc = value
        self._fetch_data()


class CurrencyState(BaseChartState):
    selected_currency: str = currency_codes[36]
    currency_data: list[dict] = []  # Renamed from 'data' to avoid shadowing

    def _fetch_data(self):
        """Fetch currency data based on current state."""
        try:
            moneda = currency_dict[self.selected_currency]
            df = currency.series(
                moneda=moneda,
                fechadesde=self.start_date,
                fechahasta=self.end_date
            )[['fecha', 'detalle_tipoCotizacion']]
            df['fecha'] = df['fecha'].dt.strftime('%Y-%m-%d')
            df = df.rename(columns={'detalle_tipoCotizacion': 'valor'})
            df = df.sort_values(by='fecha', ascending=True)
            self.currency_data = df.to_dict(orient='records')
        except Exception as e:
            print(f"Error fetching currency data: {e}")
            self.currency_data = []

    @rx.event
    def on_load(self):
        """Override parent method to ensure proper initialization of currency data."""
        self._fetch_data()

    @rx.event
    def set_currency(self, value: str):
        self.selected_currency = value
        self._fetch_data()

    @rx.event
    def set_currency_start_date(self, date: str):
        self.set_start_date(date, "currency_")
        
    @rx.event
    def set_currency_end_date(self, date: str):
        self.set_end_date(date, "currency_")
