import numpy as np
from numpy import ndarray as Array
from pandas import DataFrame
from abc import ABC, abstractmethod
#from mlds6sentiment.types.feature_extraction import FeatureExtractionFields
from typing import Tuple
from pydantic import BaseModel
from typing import Optional, List
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler

class FeatureExtractionFields(BaseModel):
    label: str
    categorical: List[str]
    ordinal: List[str]
    numeric: List[str]

class AbstractFeatureExtractor(ABC):
    data: DataFrame
    fields: FeatureExtractionFields
    x: Array
    y: Array

    def add_data(self, data: DataFrame) -> "AbstractFeatureExtractor":
        self.data = data
        return self

    def add_fields(self, fields: FeatureExtractionFields) -> "AbstractFeatureExtractor":
        self.fields = fields
        return self

    def save(self, path: str):
        np.save(f"{path}_x.npy", self.x)
        np.save(f"{path}_y.npy", self.y)

    @abstractmethod
    def extract(self) -> Tuple[Array, Array]:
        ...

class LinesFeatureExtractor(AbstractFeatureExtractor):

    def __init__(self):
        self.transformer = ColumnTransformer(transformers=[])

    def extract(self) -> Tuple[Array, Array]:
        features = self.data[self.fields.categorical + self.fields.ordinal + self.fields.numeric]
        self.y = self.data[self.fields.label].to_numpy()

        self.transformer = ColumnTransformer(
                transformers=[
                    ("categorical", OneHotEncoder(), self.fields.categorical),
                    ("ordinal", MinMaxScaler(), self.fields.ordinal),
                    ("numeric", StandardScaler(), self.fields.numeric),
                    ]
                )
        self.x = self.transformer.fit_transform(features)

        return self.x, self.y