import pandas as pd
import numpy as np
from datetime import datetime
from abc import ABC, abstractmethod
from pandas import DataFrame
from typing import List

class AbstractPreprocesser(ABC):
    data: DataFrame

    def add_data(self) -> DataFrame:
        return self.data

    def dropDuplicates(self, subset_: List[str]) -> "AbstractPreprocesser":
        self.data.drop_duplicates(subset=subset_, keep='last', inplace=True)
        return self

    def imputeData(self, field: str, value: float) -> "AbstractPreprocesser":
        self.data[field].fillna(value, inplace=True)
        return self

    def cleanOutliers(self, field: str, threshold: float, newvalue: float) -> "AbstractPreprocesser":
        self.data.loc[self.data[field] > threshold, field] = newvalue        
        return self

    @abstractmethod
    def CleanData(self) -> "AbstractPreprocesser":
        ...

    @abstractmethod
    def AddFeatures(self) -> "AbstractPreprocesser":
        ...

    @abstractmethod
    def DropFeatures(self) -> "AbstractPreprocesser":
        ...

class LinesDataPreprocesser(AbstractPreprocesser):

    def __init__(self, data : DataFrame, dfquejas_: DataFrame, dfreclamos_: DataFrame):
        self.data = data
        self.dfquejas = dfquejas_
        self.dfreclamos = dfreclamos_

    """Formateo y limpieza"""

    def AdjustColumnsNames(self) -> "LinesDataPreprocesser":
        
        self.data.columns = self.data.columns.str.replace(' ','_')
        return self

    def SetIndex(self) -> "LinesDataPreprocesser":
        
        self.data.set_index("codigo_del_producto", inplace=True)
        return self        

    def CleanData(self, impute_fields: List[str], outliers_fields: List[str] ) -> "LinesDataPreprocesser":
        
        self.dropDuplicates(['codigo_del_producto'])
             
        for field in impute_fields:    
            self.imputeData(field, self.data[field].mean())

        for field in outliers_fields: 
            self.cleanOutliers(field, 
                               self.data[field].quantile(.9999), 
                               self.data[field].quantile(.9999))
        return self


    def FormatDates(self) -> "LinesDataPreprocesser":
        self.data = self.data.assign(
            fecha_de_retiro = (lambda df: pd.to_datetime(df['fecha_de_retiro'], 
                                                        format='%Y/%m/%d %H:%M:%S', errors = 'coerce')
                                                        .fillna(datetime.strptime('31/12/2019 23:59:59', '%d/%m/%Y %H:%M:%S'))),
            fecha_de_nacimiento = pd.to_datetime(self.data ['fecha_de_nacimiento'], 
                                                 format='%Y/%m/%d %H:%M:%S', errors = 'coerce'),
            fecha_de_instalacion = pd.to_datetime(self.data ['fecha_de_instalacion'], 
                                                  format='%Y/%m/%d %H:%M:%S', errors = 'coerce')
        )
        return self

    """Creación de características"""

    def getAgeandAntiquity(self) -> "LinesDataPreprocesser":
        self.data = self.data.assign(
            edad_temp = lambda df: np.floor(df['fecha_de_retiro'].sub(df['fecha_de_nacimiento']) 
                                                                      / np.timedelta64(1, 'Y')), 
            edad = lambda df: df['edad_temp'].fillna(df['edad_temp'].mean()),
            antiguedad = lambda df: np.floor(df['fecha_de_retiro'].sub(df['fecha_de_instalacion'])
                                                                      / np.timedelta64(1, 'Y'))
        )

        self.data.drop(columns=['edad_temp'], axis=1, inplace=True)        
        return self
    
    # Obtiene nro. promedio de quejas anual
    def getComplaintsInfo(self) -> "LinesDataPreprocesser":
    
        self.dfquejas = (self.dfquejas.assign(
                                ano = self.dfquejas['fecha de registro'].apply(lambda fecha: str(fecha).split("-")[0])
                            ).groupby(['producto','ano']).count()['numero de solicitud']
                             .groupby('producto').mean())
        
        self.data = (self.data.join(self.dfquejas, on='codigo_del_producto', how='left')
                                .rename({'numero de solicitud' : 'nro_promedio_quejas_anual'}
                                        ,axis=1, inplace = False))
        
        self.data['nro_promedio_quejas_anual'].fillna(0, inplace = True)
        return self

    # Obtiene nro. promedio reclamos anual y valor promedio reclamos anual
    def getClaimsInfo(self) -> "LinesDataPreprocesser":

        def apply_func(df):

            return pd.Series({
                'count_reclamos': df['numero de solicitud'].count(),
                'val_reclamos': df['valor reclamado'].sum()
            })

        self.dfreclamos  = (self.dfreclamos.assign(
                            ano = self.dfreclamos['fecha de registro'].apply(lambda fecha: str(fecha).split("-")[0])
                            ).groupby(['producto','ano']).apply(apply_func)
                            .groupby('producto').mean()
                            .rename({'count_reclamos' : 'nro_promedio_reclamos_anual', 
                                    'val_reclamos' : 'valor_promedio_reclamos_anual'}
                                    ,axis=1, inplace = False))

        self.data = self.data.join(self.dfreclamos, on='codigo_del_producto', how='left')
        self.data.loc[self.data['nro_promedio_reclamos_anual'].isna(), ['nro_promedio_reclamos_anual','valor_promedio_reclamos_anual']] = 0
        return self

    # Obtiene Etiqueta del dataset
    def getClass(self) -> "LinesDataPreprocesser":

        self.data = self.data.assign(
                        clase = self.data['codigo_estado'].apply(lambda x: 1 if (x == 95 or x == 94) else 0)
                    )
        return self

    # Adiciona características a un dataset
    def AddFeatures(self) -> "LinesDataPreprocesser":
        (self.FormatDates()
             .getAgeandAntiquity()
             .getComplaintsInfo()
             .getClaimsInfo()
             .getClass())
        return self

    """Eliminación características"""

    # Eliminación características del dataset
    def DropFeatures(self, fields: List[str]) -> "LinesDataPreprocesser":
    
        self.data.drop(columns=fields, axis=1, inplace=True)
        self.data.dropna(inplace=True, axis = 1)

        return self
