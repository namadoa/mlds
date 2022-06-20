import pandas as pd
from abc import ABC, abstractmethod
from pandas import DataFrame
from enum import Enum, auto


class DataSheetsEnum(Enum):
    LINEAS_ACTIVAS = auto()
    CLIENTES_ACTIVAS = auto()
    LINEAS_RETIRADAS = auto()
    CLIENTES_RETIRADAS = auto()
    QUEJAS = auto()
    RECLAMOS = auto()

class AbstractDataLoader(ABC):
    data: DataFrame
    path: str
    name: str

    def add_path(self, path: str) -> "AbstractDataLoader":
        self.path = path
        return self

    def get_data(self) -> DataFrame:
        return self.data

    @abstractmethod
    def export(self, path: str) -> "AbstractDataLoader":
        ...

    @abstractmethod
    def load(self) -> "AbstractDataLoader":
        ...

    def __repr__(self) -> str:
        return f"{self.name}(\npath={self.path}\ndata={str(self.data)})"

    def __str__(self) -> str:
        return self.__repr__()

class LinesDataLoader(AbstractDataLoader):
    name = "LinesDataLoader"
    data_lineas_activas: DataFrame
    data_clientes_activas: DataFrame
    data_lineas_retiradas: DataFrame
    data_clientes_retiradas: DataFrame
    dataquejas: DataFrame
    datareclamos: DataFrame

    def __init__(self):
        self.data = DataFrame([])
        self.data_lineas_activas = DataFrame([])
        self.data_clientes_activas = DataFrame([])
        self.data_lineas_retiradas = DataFrame([])
        self.data_clientes_retiradas = DataFrame([])
        self.dataquejas = DataFrame([])
        self.datareclamos = DataFrame([])        
        self.path = ""

    def export(self, path: str) -> "LinesDataLoader":
        self.data.to_parquet(path)
        return self

    def load(self, sheets=dict) -> "LinesDataLoader":
        self.data_lineas_activas = DataFrame(pd.read_excel(self.path, 
                                                      sheet_name = sheets[DataSheetsEnum.LINEAS_ACTIVAS]))

        self.data_clientes_activas = DataFrame(pd.read_excel(self.path, 
                                                      sheet_name = sheets[DataSheetsEnum.CLIENTES_ACTIVAS]))

        self.data_lineas_retiradas = DataFrame(pd.read_excel(self.path, 
                                                      sheet_name = sheets[DataSheetsEnum.LINEAS_RETIRADAS]))

        self.data_clientes_retiradas = DataFrame(pd.read_excel(self.path, 
                                                      sheet_name = sheets[DataSheetsEnum.CLIENTES_RETIRADAS])) 

        self.dataquejas = DataFrame(pd.read_excel(self.path, 
                                                      sheet_name = sheets[DataSheetsEnum.QUEJAS]))

        self.datareclamos = DataFrame(pd.read_excel(self.path, 
                                                      sheet_name = sheets[DataSheetsEnum.RECLAMOS]))                                                        
        return self

    
    def MergeLinesData(self, code_field:str) -> "LinesDataLoader":
        
        self.data = pd.concat([self.data_lineas_activas.join(self.data_clientes_activas.set_index(code_field), 
                                                       on=code_field, how='inner'),                       
                               self.data_lineas_retiradas.join(self.data_clientes_retiradas.set_index(code_field), 
                                                       on=code_field, how='inner')])

        return self

    def get_data_claims(self) -> DataFrame:
        return self.dataquejas  

    def get_data_complaints(self) -> DataFrame:
        return self.datareclamos