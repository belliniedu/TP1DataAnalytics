from domain.dataset import Dataset
import pandas as pd


class DatasetCSV(Dataset):
    def __init__(self, fuente):
        super().__init__(fuente)


    def cargar_datos(self):
        try:
            df = pd.read_csv(self.fuente)
            print("Se cargó el CSV.")
            self.datos = df
            if self.validar_datos():
               self.transformar_datos()
        except Exception as error:
            print(f"Error cargando CSV: {error}")