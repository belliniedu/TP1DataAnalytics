from abc import ABC, abstractmethod

class Dataset(ABC):
    def __init__(self, fuente):
        self.__fuente = fuente
        self.__datos = None

    @property
    def datos(self):
        # Procesar
        return self.__datos

    @datos.setter
    def datos(self, value):
        # Validaciones
        self.__datos = value

    @property
    def fuente(self):
        return self.__fuente

    @abstractmethod
    def cargar_datos(self):
        pass

    def validar_datos(self):
        if self.datos is None:
            raise ValueError("No se cargaron los datos")
        if self.datos.duplicated().sum() > 0:
            print("Se detectaron filas duplicadas.")
        if self.datos.isnull().sum().sum() > 0:
            print("Se detectaron datos faltantes.")
        return True

    def transformar_datos(self):
        if self.datos is not None:
            self.__datos.columns = self.datos.columns.str.lower().str.replace(" ", "_")
            self.__datos = self.datos.replace(to_replace=[None, "nan", "NaN", ""], value=" ")
            self.__datos = self.datos.drop_duplicates()
            for col in self.datos.select_dtypes(include="object").columns:
                self.__datos[col] = self.datos[col].astype(str).str.strip()
            print("Se aplicaron las transformaciones.")
        else:
            print("No se encontraron datos para transformar.")

    def mostrar_resumen(self):
        return print(self.datos.describe(include='all') if self.datos is not None else "No se encontraron Datos.")