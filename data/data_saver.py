import pandas as pd
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import create_engine
from decouple import config


class DataSaver:

    def __init__(self):
         user = config('DB_USER')
         password = config('DB_PASSWORD')
         host = config('DB_HOST')
         port = config('DB_PORT')
         database = config('DB_NAME')

         url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
         self.engine = create_engine(url)


    def guardar_dataframe(self, df, nombre_tabla):
        if df is None:
            print(f"No se pudo guardar, no se encontraron datos para {nombre_tabla}")
            return

        if not isinstance(df, pd.DataFrame):
            print(f"Tipo no válido: Se recibió un {type(df)} cuando se esperaba un DataFrame.")
            return

        try:

            df.to_sql(nombre_tabla, con=self.engine, if_exists='replace', index=False)

            print(f"Los datos se guardaron en la tabla: {nombre_tabla}")

        except SQLAlchemyError as er:
            print(f"Error al guardar los datos: {er}")