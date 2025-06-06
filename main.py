from os import path
from data.data_saver import DataSaver
from domain.dataset_csv import DatasetCSV
from domain.dataset_json import DatasetJSON


# Ruta de los datasets
csv_path = path.join(path.dirname(__file__), "files/precios-de-gas-natural-.csv")
json_path = path.join(path.dirname(__file__), "files/world-population-by-country-2020.json")

# Cargar los datasets y transformar los datos
csv = DatasetCSV(csv_path)
csv.cargar_datos()
csv.mostrar_resumen()

json = DatasetJSON(json_path)
json.cargar_datos()
json.mostrar_resumen()

# Guardar en la base de datos
db = DataSaver()
db.guardar_dataframe(csv.datos, "precios-de-gas-natural-.csv")
db.guardar_dataframe(json.datos, "world-population-by-country-2020.json")