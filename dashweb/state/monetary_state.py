import reflex as rx
import datetime
from pyBCRAdata import monetary

# Preparar listas y diccionario
variables = monetary.variables()
list_id = variables['idVariable'].to_list()
list_label = variables['descripcion'].to_list()
variable_dict = dict(zip(list_label, list_id))

class MonetaryState(rx.State):
    selected_desc: str = list_label[0]
    series_data: list[dict] = []
    # Add start_date and end_date, initialize with defaults
    start_date: str = datetime.date(datetime.date.today().year, 1, 1).strftime('%Y-%m-%d')
    end_date: str = datetime.date.today().strftime('%Y-%m-%d')

    def _fetch_data(self):
        """Helper method to fetch data based on current state."""
        try:
            id_variable = variable_dict[self.selected_desc]
            # Use start_date and end_date in the API call
            df = monetary.series(
                id_variable=id_variable,
                desde=self.start_date,
                hasta=self.end_date
            )[['fecha', 'valor']]
            df['fecha'] = df['fecha'].dt.strftime('%Y-%m-%d')
            df = df.sort_values(by='fecha', ascending=True)
            self.series_data = df.to_dict(orient='records')
        except Exception as e:
            # Handle potential errors during data fetching
            print(f"Error fetching data: {e}")
            self.series_data = []  # Clear data on error

    @rx.event
    def set_series(self, value: str):
        self.selected_desc = value
        self._fetch_data()  # Use helper method

    @rx.event
    def set_start_date(self, date: str):
        self.start_date = date
        self._fetch_data()  # Refetch data

    @rx.event
    def set_end_date(self, date: str):
        self.end_date = date
        self._fetch_data()  # Refetch data

    @rx.event
    def on_load(self):
        self._fetch_data()  # Fetch initial data