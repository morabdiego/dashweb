import reflex as rx
from pyBCRAdata import monetary, currency
import datetime
import pandas as pd

# Preparar listas y diccionario
variables = monetary.variables()
list_id = variables['idVariable'].to_list()
list_label = variables['descripcion'].to_list()
variable_dict = {}
# Crear el diccionario de forma segura (asegurándose de que las claves sean hashables)
for label, id_var in zip(list_label, list_id):
    if isinstance(label, (str, int, float, bool, tuple)):
        variable_dict[label] = id_var

# Preparar listas y diccionario para monedas
currencies = currency.currencies()
currency_codes = currencies['codigo'].to_list()
currency_names = currencies['denominacion'].to_list()
currency_dict = {}
# Crear el diccionario de forma segura para monedas
for name, code in zip(currency_names, currency_codes):
    if isinstance(name, (str, int, float, bool, tuple)):
        currency_dict[name] = code

# Valor por defecto en caso de que no haya opciones válidas en la lista
DEFAULT_MONETARY_ITEM = list_label[0] if list_label and isinstance(list_label[0], (str, int, float, bool, tuple)) else "Base Monetaria"
DEFAULT_CURRENCY_ITEM = currency_names[36] if len(currency_names) > 36 and isinstance(currency_names[36], (str, int, float, bool, tuple)) else "Dólar estadounidense"

# Fechas predeterminadas
DEFAULT_START_DATE = datetime.date(datetime.date.today().year, 1, 1).strftime('%Y-%m-%d')
DEFAULT_END_DATE = datetime.date.today().strftime('%Y-%m-%d')

class MonetaryState(rx.State):
    """Estado para gráficos monetarios."""
    selected_item: str = DEFAULT_MONETARY_ITEM
    data: list[dict] = []
    
    # Valores actuales mostrados en la UI
    start_date: str = DEFAULT_START_DATE
    end_date: str = DEFAULT_END_DATE
    
    # Valores temporales (para almacenar los cambios antes de aplicarlos)
    temp_selected_item: str = DEFAULT_MONETARY_ITEM
    temp_start_date: str = DEFAULT_START_DATE
    temp_end_date: str = DEFAULT_END_DATE
    
    def _fetch_data(self):
        """Fetch monetary data based on current state."""
        try:
            # Verificar que la clave seleccionada existe en el diccionario
            if self.selected_item in variable_dict:
                id_variable = variable_dict[self.selected_item]
                
                # Obtener datos y procesarlos de manera segura
                df = monetary.series(
                    id_variable=id_variable,
                    desde=self.start_date,
                    hasta=self.end_date
                )
                
                # Asegurarse de que df es un DataFrame y contiene las columnas esperadas
                if isinstance(df, pd.DataFrame) and 'fecha' in df.columns and 'valor' in df.columns:
                    df_processed = df[['fecha', 'valor']].copy()
                    df_processed['fecha'] = df_processed['fecha'].dt.strftime('%Y-%m-%d')
                    df_processed = df_processed.sort_values(by='fecha', ascending=True)
                    
                    # Convertir a lista de diccionarios de manera segura
                    self.data = df_processed.to_dict(orient='records')
                else:
                    print(f"DataFrame does not have expected columns: {df.columns}")
                    self.data = []
            else:
                print(f"Selected item '{self.selected_item}' not found in variable dictionary")
                self.data = []
        except Exception as e:
            print(f"Error fetching monetary data: {e}")
            self.data = []
    
    @rx.event
    def on_load(self):
        """Fetch data on component load."""
        # Al cargar, inicializamos los valores temporales con los valores actuales
        self.temp_selected_item = self.selected_item
        self.temp_start_date = self.start_date
        self.temp_end_date = self.end_date
        self._fetch_data()
    
    @rx.event
    def set_selected_item(self, value: str):
        """Actualiza el valor temporal del ítem seleccionado."""
        self.temp_selected_item = value
    
    @rx.event
    def set_start_date(self, date: str):
        """Actualiza el valor temporal de la fecha de inicio."""
        self.temp_start_date = date
    
    @rx.event
    def set_end_date(self, date: str):
        """Actualiza el valor temporal de la fecha de fin."""
        self.temp_end_date = date
    
    @rx.event
    def apply_changes(self):
        """Aplica los cambios temporales y actualiza los datos."""
        # Actualizar los valores reales
        self.selected_item = self.temp_selected_item
        self.start_date = self.temp_start_date
        self.end_date = self.temp_end_date
        
        # Actualizar los datos
        self._fetch_data()

class CurrencyState(rx.State):
    """Estado para gráficos de monedas."""
    selected_item: str = DEFAULT_CURRENCY_ITEM
    data: list[dict] = []
    
    # Valores actuales mostrados en la UI
    start_date: str = DEFAULT_START_DATE
    end_date: str = DEFAULT_END_DATE
    
    # Valores temporales (para almacenar los cambios antes de aplicarlos)
    temp_selected_item: str = DEFAULT_CURRENCY_ITEM
    temp_start_date: str = DEFAULT_START_DATE
    temp_end_date: str = DEFAULT_END_DATE
   
    def _fetch_data(self):
        """Fetch currency data based on current state."""
        try:
            # Verificar que la clave seleccionada existe en el diccionario
            if self.selected_item in currency_dict:
                moneda = currency_dict[self.selected_item]
                
                # Obtener datos y procesarlos de manera segura
                df = currency.series(
                    moneda=moneda,
                    fechadesde=self.start_date,
                    fechahasta=self.end_date
                )
                
                # Asegurarse de que df es un DataFrame y contiene las columnas esperadas
                if isinstance(df, pd.DataFrame) and 'fecha' in df.columns and 'detalle_tipoCotizacion' in df.columns:
                    df_processed = df[['fecha', 'detalle_tipoCotizacion']].copy()
                    df_processed['fecha'] = df_processed['fecha'].dt.strftime('%Y-%m-%d')
                    df_processed = df_processed.sort_values(by='fecha', ascending=True)
                    
                    # Convertir a lista de diccionarios de manera segura
                    self.data = df_processed.to_dict(orient='records')
                else:
                    print(f"DataFrame does not have expected columns: {df.columns}")
                    self.data = []
            else:
                print(f"Selected item '{self.selected_item}' not found in currency dictionary")
                self.data = []
        except Exception as e:
            print(f"Error fetching currency data: {e}")
            self.data = []
    
    @rx.event
    def on_load(self):
        """Fetch data on component load."""
        # Al cargar, inicializamos los valores temporales con los valores actuales
        self.temp_selected_item = self.selected_item
        self.temp_start_date = self.start_date
        self.temp_end_date = self.end_date
        self._fetch_data()
    
    @rx.event
    def set_selected_item(self, value: str):
        """Actualiza el valor temporal del ítem seleccionado."""
        self.temp_selected_item = value
    
    @rx.event
    def set_start_date(self, date: str):
        """Actualiza el valor temporal de la fecha de inicio."""
        self.temp_start_date = date
       
    @rx.event
    def set_end_date(self, date: str):
        """Actualiza el valor temporal de la fecha de fin."""
        self.temp_end_date = date
    
    @rx.event
    def apply_changes(self):
        """Aplica los cambios temporales y actualiza los datos."""
        # Actualizar los valores reales
        self.selected_item = self.temp_selected_item
        self.start_date = self.temp_start_date
        self.end_date = self.temp_end_date
        
        # Actualizar los datos
        self._fetch_data()