from domain.dataset import Dataset
import pandas as pd
import requests


class DatasetAPI(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)

    def cargar_datos(self):

        try:
            response = requests.get(self.fuente)

            if response.status_code == 200:
                df = pd.json_normalize(response.json())

                # Verificar el valor es una lista
                def es_lista(v):
                    return isinstance(v, list)

                # Transformar todas las columnas de tipo list a string
                def lista_to_string(l):
                    if isinstance(l, list):
                        return ', '.join(map(str, l))

                for columna in df.columns:
                    if df[columna].apply(es_lista).any():
                        df[columna] = df[columna].apply(lista_to_string)

                self.datos = df
                print(self.datos)
                print("La API fue cargada")

                if self.validar_datos():
                    self.transformar_datos()

            else:
                print("Se produjo un error al obtener los datos de la API")

        except Exception as error:
            # Se informa el error
            print(f"Error de la API. {error}")