from domain.dataset import Dataset
import pandas as pd


class DatasetJSON(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)


    def cargar_datos(self):
        try:
            df = pd.read_json(self.fuente)
            print("Se cargó el JSON")
            self.datos = df
            if self.validar_datos():
                self.transformar_datos()
        except Exception as error:
            print(f"Error cargando CSV: {error}")