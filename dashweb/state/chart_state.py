import reflex as rx
from pyBCRAdata import monetary, currency
import pandas as pd
from typing import List, Dict, Any, Optional

# Importar constantes
from dashweb.constants import (
    MONETARY_DICT,
    MONETARY_LABELS,
    CURRENCY_DICT,
    CURRENCY_NAMES,
    DEFAULT_MONETARY_ITEM,
    DEFAULT_CURRENCY_ITEM,
    DEFAULT_START_DATE,
    DEFAULT_END_DATE
)

class MonetaryState(rx.State):
    """Estado para gráficos monetarios."""
    selected_item: str = DEFAULT_MONETARY_ITEM
    data: List[Dict[str, Any]] = []
    
    # Valores actuales mostrados en la UI
    start_date: str = DEFAULT_START_DATE
    end_date: str = DEFAULT_END_DATE
    
    # Valores temporales (para almacenar los cambios antes de aplicarlos)
    temp_selected_item: str = DEFAULT_MONETARY_ITEM
    temp_start_date: str = DEFAULT_START_DATE
    temp_end_date: str = DEFAULT_END_DATE
    
    def _fetch_data(self) -> None:
        """Fetch monetary data based on current state."""
        try:
            # Verificar que la clave seleccionada existe en el diccionario
            if self.selected_item in MONETARY_DICT:
                id_variable = MONETARY_DICT[self.selected_item]
                
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
    def on_load(self) -> None:
        """Fetch data on component load."""
        # Al cargar, inicializamos los valores temporales con los valores actuales
        self.temp_selected_item = self.selected_item
        self.temp_start_date = self.start_date
        self.temp_end_date = self.end_date
        self._fetch_data()
    
    @rx.event
    def set_selected_item(self, value: str) -> None:
        """Actualiza el valor temporal del ítem seleccionado."""
        self.temp_selected_item = value
    
    @rx.event
    def set_start_date(self, date: str) -> None:
        """Actualiza el valor temporal de la fecha de inicio."""
        self.temp_start_date = date
    
    @rx.event
    def set_end_date(self, date: str) -> None:
        """Actualiza el valor temporal de la fecha de fin."""
        self.temp_end_date = date
    
    @rx.event
    def apply_changes(self):
        # Verificar que las fechas no sean iguales
        if self.temp_start_date == self.temp_end_date:
            return rx.toast.error(
                "Error: Las fechas no pueden ser iguales",
                position="top-center",
                close_button=True,
                )
        
        # Verificar que la fecha de inicio sea anterior a la fecha de fin
        if self.temp_start_date > self.temp_end_date:
            return rx.toast.error(
                "Error: 'Desde' debe ser anterior a 'Hasta'",
                position="top-center",
                close_button=True,
                )
        
        # Si pasó las validaciones, actualizar los datos
        self.selected_item = self.temp_selected_item
        self.start_date = self.temp_start_date
        self.end_date = self.temp_end_date
        self._fetch_data()
        
        return rx.toast.success(
            "Datos actualizados correctamente",
            position="top-center",
            close_button=True,
            )
        
    @rx.event
    def download_csv(self):
        """Descarga los datos actuales como un archivo CSV."""
        try:
            # Verificar que la clave seleccionada existe en el diccionario
            if self.selected_item in MONETARY_DICT:
                id_variable = MONETARY_DICT[self.selected_item]
                
                # Obtener datos
                df = monetary.series(
                    id_variable=id_variable,
                    desde=self.start_date,
                    hasta=self.end_date
                )
                
                # Preparar para descarga
                if isinstance(df, pd.DataFrame):
                    csv_data = df.to_csv(index=False)
                    return rx.download(
                        data=csv_data,
                        filename="data_query.csv"
                    )
                else:
                    print("No data available for download")
            else:
                print(f"Selected item '{self.selected_item}' not found in variable dictionary")
        except Exception as e:
            print(f"Error downloading CSV: {e}")
            return None

class CurrencyState(rx.State):
    """Estado para gráficos de monedas."""
    selected_item: str = DEFAULT_CURRENCY_ITEM
    data: List[Dict[str, Any]] = []
    
    # Valores actuales mostrados en la UI
    start_date: str = DEFAULT_START_DATE
    end_date: str = DEFAULT_END_DATE
    
    # Valores temporales (para almacenar los cambios antes de aplicarlos)
    temp_selected_item: str = DEFAULT_CURRENCY_ITEM
    temp_start_date: str = DEFAULT_START_DATE
    temp_end_date: str = DEFAULT_END_DATE

    def _fetch_data(self) -> None:
        """Fetch currency data based on current state."""
        try:
            # Verificar que la clave seleccionada existe en el diccionario
            if self.selected_item in CURRENCY_DICT:
                moneda = CURRENCY_DICT[self.selected_item]
                
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
    def on_load(self) -> None:
        """Fetch data on component load."""
        # Al cargar, inicializamos los valores temporales con los valores actuales
        self.temp_selected_item = self.selected_item
        self.temp_start_date = self.start_date
        self.temp_end_date = self.end_date
        self._fetch_data()
    
    @rx.event
    def set_selected_item(self, value: str) -> None:
        """Actualiza el valor temporal del ítem seleccionado."""
        self.temp_selected_item = value
    
    @rx.event
    def set_start_date(self, date: str) -> None:
        """Actualiza el valor temporal de la fecha de inicio."""
        self.temp_start_date = date
    
    @rx.event
    def set_end_date(self, date: str) -> None:
        """Actualiza el valor temporal de la fecha de fin."""
        self.temp_end_date = date
    
    @rx.event
    def apply_changes(self):
        # Verificar que las fechas no sean iguales
        if self.temp_start_date == self.temp_end_date:
            return rx.toast.error(
                "Error: Las fechas no pueden ser iguales",
                position="top-center",
                close_button=True,
                )
        
        # Verificar que la fecha de inicio sea anterior a la fecha de fin
        if self.temp_start_date > self.temp_end_date:
            return rx.toast.error(
                "Error: 'Desde' debe ser anterior a 'Hasta'",
                position="top-center",
                close_button=True,
                )
        
        # Si pasó las validaciones, actualizar los datos
        self.selected_item = self.temp_selected_item
        self.start_date = self.temp_start_date
        self.end_date = self.temp_end_date
        self._fetch_data()
        
        return rx.toast.success(
            "Datos actualizados correctamente",
            position="top-center",
            close_button=True,
            )
        
    @rx.event
    def download_csv(self):
        """Descarga los datos actuales como un archivo CSV."""
        try:
            # Verificar que la clave seleccionada existe en el diccionario
            if self.selected_item in CURRENCY_DICT:
                moneda = CURRENCY_DICT[self.selected_item]
                
                # Obtener datos
                df = currency.series(
                    moneda=moneda,
                    fechadesde=self.start_date,
                    fechahasta=self.end_date
                )
                
                # Preparar para descarga
                if isinstance(df, pd.DataFrame):
                    csv_data = df.to_csv(index=False)
                    return rx.download(
                        data=csv_data,
                        filename="data_query.csv"
                    )
                else:
                    print("No data available for download")
            else:
                print(f"Selected item '{self.selected_item}' not found in currency dictionary")
        except Exception as e:
            print(f"Error downloading CSV: {e}")
            return None