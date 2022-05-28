# Data and Feature Definitions

This document provides a central hub for the raw data sources, the processed/transformed data, and feature sets. More details of each dataset is provided in the data summary report. 

For each data, an individual report describing the data schema, the meaning of each data field, and other information that is helpful for understanding the data is provided. If the dataset is the output of processing/transforming/feature engineering existing data set(s), the names of the input data sets, and the links to scripts that are used to conduct the operation are also provided. 

For each dataset, the links to the sample datasets in the _**Data**_ directory are also provided. 

_**For ease of modifying this report, placeholder links are included in this page, for example a link to dataset 1, but they are just placeholders pointing to a non-existent page. These should be modified to point to the actual location.**_

## Raw Data Sources

| Dataset Name | Original Location   | Destination Location  | Data Movement Tools / Scripts | Link to Report |
| ---:| ---: | ---: | ---: | -----: |
| lineas_activas.csv | Los datos se obtendrán  a partir de archivos csv almacenados en Google cloud storage (GCP) | Los datos se almacenarán de manera estructurada en el almacen de datos de Big query| [script1.py](link/to/python/script/file/in/Code) | [Dataset 1 Report](link/to/report1)|
| lineas_retiradas.csv | Los datos se obtendrán  a partir de archivos csv almacenados en Google cloud storage (GCP)  | Los datos se almacenarán de manera estructurada en el almacen de datos de Big query | [script1.py](link/to/R/script/file/in/Code) | [Dataset 2 Report](link/to/report2)|
| clientes_lineas_activas.csv | Los datos se obtendran  partir de archivos csv almacenados en Google cloud storage (GCP)  | Los datos se almacenarán de manera estructurada en el almacen de datos de Big query | [script1.py](link/to/R/script/file/in/Code) | [Dataset 3 Report](link/to/report2)|
| clientes_lineas_retiradas.csv | Los datos se obtendran  partir de archivos csv almacenados en Google cloud storage (GCP)  | Los datos se almacenarán de manera estructurada en el almacen de datos de Big query | [script1.py](link/to/R/script/file/in/Code) | [Dataset 4 Report](link/to/report2)|
| quejas_lineas.csv | Los datos se obtendran  partir de archivos csv almacenados en Google cloud storage (GCP)  | Los datos se almacenarán de manera estructurada en el almacen de datos de Big query | [script1.py](link/to/R/script/file/in/Code) | [Dataset 5 Report](link/to/report2)|
| reclamos_lineas.csv| Los datos se obtendran  partir de archivos csv almacenados en Google cloud storage (GCP)  | Los datos se almacenarán de manera estructurada en el almacen de datos de Big query | [script1.py](link/to/R/script/file/in/Code) | [Dataset 6 Report](link/to/report2)|

* Dataset1 summary. <Provide brief summary of the data, such as how to access the data. More detailed information should be in the Dataset1 Report.>

1.	lineas_activas.csv
    *	Descripción: Líneas móviles activas
    *	Contenido: Información relacionada a las líneas móviles activas hasta el año 2019
    *	Total campos: 12
    *	Total registros:  86550
    *	Formato de almacenamiento: archivo .csv
    *	Tipos de datos: estructurados

Información de los campos:

RangeIndex: 86550 entries, 0 to 86549
Data columns (total 12 columns):

| #      | Column |  Non-Null Count     | Dtype | 
| ----------- | ----------- | ----------- | ----------- |
|0   |código del producto   |86550 non-null  |int64 |        
|1   |código del cliente    |86550 non-null  |int64 |        
|2   |fecha de instalación  |86550 non-null  |datetime64|
|3   |fecha de retiro       |86550 non-null  |object|       
|4   |plan                  |86550 non-null  |object|    
|5   |tipo de plan          |86550 non-null  |object|     
|6   |valor plan            |85972 non-null  |float64|      
|7   |estado                |86550 non-null  |object|     
|8   |ciclo                 |86550 non-null  |object|      
|9   |estado financiero     |86550 non-null  |object|     
|10  |saldo pendiente       |86550 non-null  |float64|   
|11  |valor en reclamo      |86550 non-null  |float64|

Estadísticas descriptivas de los campos numéricos:

|        | valor plan    | saldo pendiente |  valor del reclamo |
| ----------- | ----------- | ----------- | ----------- |
|count|	85972.000000|  	86550.000000|	86550.000000|
|mean|	77.220173|	7.185170|	0.000129|
|std|	244.716541|	136.252221|	0.038070|
|min|	0.000000|	-2.630000|	0.000000|
|25%|	0.000000|	0.000000|	0.000000|
|50%|	0.000000|	0.000000|	0.000000|
|75%|	47.980000|	0.000000|	0.000000|
|max|	2618.000000|	36866.670000|	11.200000|

![1](https://user-images.githubusercontent.com/66392216/169719710-fe183a3a-a610-441e-97e0-da1ad4d87c93.JPG)

2.	lineas_retiradas.csv

    *	Descripción: Líneas móviles retiradas
    *	Contenido: Información relacionada a las líneas móviles retiradas entre los años 2017 y 2019
    *	Total campos: 13
    *	Total registros:  27236
    *	Formato de almacenamiento: archivo .csv
    *	Tipos de datos: estructurados

Información de los campos:

RangeIndex: 27236 entries, 0 to 27235
Data columns (total 13 columns):
| #      | Column |  Non-Null Count     | Dtype | 
| ----------- | ----------- | ----------- | ----------- |      
 0 |  código del producto|   27236 non-null|  int64 |        
 1 |  código del cliente|    27236 non-null|  int64 |        
 2 |  fecha de instalación | 27236 non-null|  datetime64[ns]|
 3 |  fecha de retiro|       27236 non-null | datetime64[ns]|
 4 |  plan  |                27236 non-null|  object        
 5 |  tipo de plan  |        27236 non-null | object|       
 6 |  valor plan  |          27175 non-null|  float64 |      
 7 |  código estado |        27236 non-null |int64 |        
 8 |  estado |               27236 non-null|  object |       
 9 |  ciclo   |              27236 non-null|  object|        
 10 | estado financiero|     27236 non-null|  object|        
 11 | saldo pendiente|      27236 non-null | float64|       
 12 | valor en reclamo |     27236 non-null | int64  |       

Estadísticas descriptivas de los campos numéricos:

|        | valor plan    | saldo pendiente |  valor del reclamo |
| ----------- | ----------- | ----------- | ----------- |
|count	|27175.000000|	27236.000000|	27236.0|
|mean	|225.730198|	37.277095|	0.0|
|std	|325.581351	|137.877364|	0.0|
|min	|0.000000|	-0.040000	|0.0|
|25%	|0.000000|	0.000000	|0.0|
|50%	|69.950000|	0.000000	|0.0|
|75%	|375.880000|	14.630000	|0.0|
|max	|2618.000000|	2295.900000	|0.0|



![4](https://user-images.githubusercontent.com/66392216/169719988-2be9dbfc-8ecd-426c-8882-963ff67d27fb.JPG)


3.	clientes_lineas_activas.csv

    *	Descripción: Clientes de las líneas móviles activas
    *	Contenido: Información relacionada a los clientes dueños de la líneas activas hasta 2019.
    *	Total campos: 11
    *	Total registros:  58052
    *	Formato de almacenamiento: archivo .csv
    *	Tipos de datos: estructurados

Información de los campos:

Data columns (total 11 columns):
| #      | Column |  Non-Null Count     | Dtype | 
| ----------- | ----------- | ----------- | ----------- |  
|0   |código del cliente |     58052 non-null | int64 |
|1   |tipo de cliente  |       58052 non-null | object |
| 2   |tipo de identificación | 58052 non-null |  object |
| 3   |fecha de nacimiento  |   56902 non-null|  object|
| 4   |género  |                6109 non-null |  object|
| 5   |estado civil |           4948 non-null |  object|
| 6   |profesión |              4819 non-null|   object|
| 7   |grado de escolaridad|    3267 non-null  | object|
| 8  | nivel de ingresos|       3300 non-null |  object|
| 9   |nivel de egresos |       3282 non-null|   object|



![6](https://user-images.githubusercontent.com/66392216/169720572-8374a0b9-7614-462e-a982-220e3f8045c9.JPG)

4.	clientes_lineas_retiradas.csv

    *	Descripción: Clientes de las líneas móviles retiradas
    *	Contenido: Información relacionada a los clientes dueños de las líneas retiradas entre 2017 y 2019.
    *	Total campos: 11
    *	Total registros:  21191
    *	Formato de almacenamiento: archivo .csv
    *	Tipos de datos: estructurados

Información de los campos:

| #      | Column |  Non-Null Count     | Dtype | 
| ----------- | ----------- | ----------- | ----------- |  
| 0  | código del cliente    |  21191 non-null | int64 |
| 1 |  tipo de cliente     |    21191 non-null | object|
 |2  | tipo de identificación|  21191 non-null | object|
 |3  | fecha de nacimiento   |  20842 non-null  |object|
 |4  | género   |               2182 non-null  | object|
 |5   |estado civil     |       1737 non-null |  object|
|6 |  profesión   |            1601 non-null  | object|
 |7   |grado de escolaridad |   1092 non-null  | object|
|9	| nivel de ingresos    |   1145 non-null  | object|
 |9  | nivel de egresos   |     1125 non-null |  object|
|10	 | ciudad   |               21191 non-null|    object|


![8](https://user-images.githubusercontent.com/66392216/169720634-907783f5-173b-43fa-948c-bc45d5b5f5ac.JPG)

5.	quejas_lineas.csv

    *	Descripción: Quejas sobre las líneas móviles
    *	Contenido: Quejas sobre las líneas móviles tanto activas como retiradas
    *	Total campos: 8
    *	Total registros:  10816
    *	Formato de almacenamiento: archivo .csv
    *	Tipos de datos: estructurados

Información de los campos:

RangeIndex: 10817 entries, 0 to 10816
Data columns (total 8 columns):
| #      | Column |  Non-Null Count     | Dtype | 
| ----------- | ----------- | ----------- | ----------- |         
| 0   |número de solicitud | 10817 non-null | int64   |      
| 1   |fecha de registro   | 10817 non-null  |datetime64[ns]|
| 2   |producto            | 10817 non-null | int64  |       
| 3   |tipo                | 10817 non-null | object  |      
| 4   |estado              | 10817 non-null | object |       
| 5   |fecha de atención   | 9818 non-null  | datetime64[ns]|
| 6   |tipo de observación | 10817 non-null | object  |      
| 7   |observación         | 10817 non-null | object |   

![10](https://user-images.githubusercontent.com/66392216/169720833-5edc0a99-ff22-456f-8fc4-95c7af1e5b46.JPG)

6.	reclamos_lineas.csv

    *	Descripción: Líneas móviles activas
    *	Contenido: Información relacionada a las líneas móviles activas hasta el año 2019
    *	Total campos: 9
    *	Total registros: 3102
    *	Formato de almacenamiento: archivo .csv
    *	Tipos de datos: estructurados

Información de los campos:

RangeIndex: 3102 entries, 0 to 3101
Data columns (total 9 columns):
| #      | Column |  Non-Null Count     | Dtype | 
| ----------- | ----------- | ----------- | ----------- |         
| 0  | número de solicitud| 3102 non-null  | int64  |       
| 1  | fecha de registro |   3102 non-null  | datetime64[ns]|
| 2  | producto    |         3102 non-null  | int64  |       
| 3  | tipo   |              3102 non-null  | object |       
| 4  | estado |              3102 non-null  | object  |      
| 5  | fecha de atención |   3102 non-null  | datetime64[ns]|
| 6  | valor reclamado |     3102 non-null  | float64  |     
| 7  | tipo de observación | 3102 non-null  | object  |      
| 8  | observación  |        3101 non-null  | object|


![12](https://user-images.githubusercontent.com/66392216/169720883-a0646177-8152-4ed0-9de1-9818ab81aa6a.JPG)

## Processed Data
| Processed Dataset Name | Input Dataset(s)   | Data Processing Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Processed Dataset 1 | [Dataset1](link/to/dataset1/report), [Dataset2](link/to/dataset2/report) | [Python_Script1.py](link/to/python/script/file/in/Code) | [Processed Dataset 1 Report](link/to/report1)|
| Processed Dataset 2 | [Dataset2](link/to/dataset2/report) |[script2.R](link/to/R/script/file/in/Code) | [Processed Dataset 2 Report](link/to/report2)|
* Processed Data1 summary. <Provide brief summary of the processed data, such as why you want to process data in this way. More detailed information about the processed data should be in the Processed Data1 Report.>
* Processed Data2 summary. <Provide brief summary of the processed data, such as why you want to process data in this way. More detailed information about the processed data should be in the Processed Data2 Report.> 

## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| Feature Set 1 | [Dataset1](link/to/dataset1/report), [Processed Dataset2](link/to/dataset2/report) | [R_Script2.R](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|
| Feature Set 2 | [Processed Dataset2](link/to/dataset2/report) |[SQL_Script2.sql](link/to/sql/script/file/in/Code) | [Feature Set2 Report](link/to/report2)|

* Feature Set1 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set1 Report.>
* Feature Set2 summary. <Provide detailed description of the feature set, such as the meaning of each feature. More detailed information about the feature set should be in the Feature Set2 Report.> 
