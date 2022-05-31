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
| Lineas.csv | lineas_activas.csv, lineas_retiradas.csv, clientes_lineas_activas.csv, clientes_lineas_retiradas.csv, quejas_lineas.csv, reclamos_lineas.csv | [PreprocessScript.py](link/to/python/script/file/in/Code) | [Processed Dataset 1 Report](link/to/report1)|

**Union de datasets**

Unimos datasets de líneas retiradas y clientes retirados

![im1](https://user-images.githubusercontent.com/105468214/171090073-85390ce2-9f73-45bb-98fd-7b09b2333512.png)

Unimos datasets de líneas activas y de clientes activos:

![im2](https://user-images.githubusercontent.com/105468214/171090095-0eec91dd-81fb-4615-9748-43cbfb023d96.png)

**Limpieza de datos duplicados**

Limpieza de líneas duplicadas en el dataset de líneas activas:

![im3](https://user-images.githubusercontent.com/105468214/171090106-d61b4d5f-b17e-40c5-9e06-b4913d4eb140.png)

Limpieza de líneas duplicadas en el dataset de líneas retiradas:

![im4](https://user-images.githubusercontent.com/105468214/171090114-1ab25ade-a8f3-4009-977b-7a0b2c436fae.png)
 
**Limpieza de datos faltantes**

* Se imputa la media del valor del plan o el tipo de plan en los casos en que el valor del plan es nulo, en los dataset de líneas activas y líneas retiradas:

![im5](https://user-images.githubusercontent.com/105468214/171090124-b83985ac-3a2c-429d-8e66-dac941c54d1e.png)
 
* Se eliminan columnas Género, Estado civil, Profesión, Grado de escolaridad, Nivel de ingresos y de egresos correspondientes a la información del cliente tanto de los datasets de líneas retiradas como los de activas, debido alrededor del 90% de los registros tienen estas columnas nulas.

![im6](https://user-images.githubusercontent.com/105468214/171090129-592be3b5-07ff-46d2-b045-e7bb389ccc4e.png)

![im7](https://user-images.githubusercontent.com/105468214/171090137-ae7f01d0-c6dc-47f4-89f8-8020c6a0190e.png)

**Selección y creación de nuevas características**

* Se unen los datasets de líneas activas y líneas retiradas.
* Se añaden las características Edad y Antiguedad, la primera es la edad del cliente de la línea al momento del retiro (último día de 2019 para líneas activas) y la segunda la antigüedad del servicio hasta el momento del retiro (último día de 2019 para líneas activas).

![im8](https://user-images.githubusercontent.com/105468214/171090146-d788273e-4aa8-4b33-9347-5b44b632d88e.png)

*	Se añade la característica de "Número de promedio quejas anual", a partir de la fecha de registro y el número de quejas registradas para cada línea telefónica en el dataset de quejas.

![im9](https://user-images.githubusercontent.com/105468214/171090152-5d898744-894c-4bc2-876b-557b390734a9.png)


*	Se añaden las características "Número promedio de reclamos anual" y "Valor promedio de reclamos anual", a partir de la fecha de registro, el valor reclamado y el número de reclamos registrados para cada línea telefónica en el dataset de reclamos.

![im10](https://user-images.githubusercontent.com/105468214/171090161-d007f939-e6b6-422c-bbfd-174ad937ece1.png)

*	Se eliminan las columnas Valor en reclamo y Tipo de cliente de los datasets de líneas retiradas y líneas activas, la primera porque es cero para casi el 100% de los registros en ambos datasets y la segunda porque tiene el mismo valor para casi el 100% de los registros.

![im11](https://user-images.githubusercontent.com/105468214/171090169-07f04ab1-a7a0-4e12-ac3e-ee53395afec7.png) 

*	Se eliminan las columnas de tipo fecha usadas para calcular la edad y la antigüedad (fecha de instalación, fecha de retiro y fecha de nacimiento).
*	Se crea la característica clase a partir de la columna estado:

> * 0 - Activo
> * 1 - Retirado por no pago
> * 2 - Deserción

**Limpieza de outliers**

Se identifican outliers en la columna saldo pendiente, se reemplaza el valor de estos outliers con un valor normal dentro del rango del campo.
 
![im12](https://user-images.githubusercontent.com/105468214/171090639-7b9c92da-99e2-4bfe-81ad-7da45dbd4e8c.png)

![im13](https://user-images.githubusercontent.com/105468214/171090670-e90f7afc-9bb6-4e39-a24f-365b11be12c4.png)

**Dataset resultante:**

![im14](https://user-images.githubusercontent.com/105468214/171090675-e8b2c082-fe0c-4b32-b6d7-ea8b575a711b.png)
![im15](https://user-images.githubusercontent.com/105468214/171090680-d509c327-8486-4805-8d6a-2ff8f9ae1109.png)

Descripción de los campos del dataset:

| column | type	| description |
| ---:| ---: | ---: |
| Plan |	STRING |	Plan de la oferta comercial suscrito por la línea |
| Tipo de plan |	STRING |	P: prepago, S: postpago, C: control |
| Ciclo	| STRING |	División administrativa de las líneas |
| Tipo de identificación | STRING |	Tipo de identificación del cliente: Cédula, R.U.C, Pasaporte, Cédula de Extranjería, Otro |
| Estado financiero	| STRING |Estado de la deuda del servicio: paz y salvo, mora | 
| Ciudad | STRING | Ciudad de residencia del cliente: Ambato, Cuenca |
| Edad | INT | Edad del cliente dueño de la línea |
| Antiguedad | INT | Antiguedad del servicio |
| Valor plan | INT | Valor mensual que se debe pagar por el plan |
| Nro. promedio quejas anual | FLO | Número promedio de quejas que se registraron sobre el servicio anualmente |
| Nro. promedio reclamos anual | FLO | Número promedio de reclamos que se registraron sobre el servicio anualmente |
| Valor promedio reclamos anual	| FLO |	Valor promedio de los reclamos que se registraron sobre el servicio anualmente |
| Saldo pendiente |	INT	| Valor total adeudado a la fecha |
| Clase |	INT	| Etiqueta a predecir en el modelo: 0 - Activo, 1 - Retirado por no pago, 2 - Deserción


## Feature Sets

| Feature Set Name | Input Dataset(s)   | Feature Engineering Tools/Scripts | Link to Report |
| ---:| ---: | ---: | ---: | 
| feature_set.npy | Lineas.csv | [Features_Script.py](link/to/R/script/file/in/Code) | [Feature Set1 Report](link/to/report1)|

Con el fin de obtener el vector de características que será el insumo del modelo se transformará el dataset preprocesado, de tal manera que las variables categóricas se conviertan a vectores numéricos y las variables numéricas serán escaladas o normalizadas:

| column | type	| description |
| ---:| ---: | ---: |
| Plan |	STRING | Codificación one-hot |
| Tipo de plan |	STRING | Codificación one-hot	 |
| Ciclo	| STRING | Codificación one-hot	 |
| Tipo de identificación | STRING | Codificación one-hot |
| Estado financiero	| STRING | Codificación one-hot | 
| Ciudad | STRING | Codificación one-hot |
| Edad | INT | Escalamiento entre 0 y 1 (Min-max scaling) |
| Antiguedad | INT | Escalamiento entre 0 y 1 (Min-max scaling) |
| Valor plan | INT | Normalización con media 0 y desviación estándar de 1 (Standard scaling) |
| Nro. promedio quejas anual | FLO | Normalización con media 0 y desviación estándar de 1 (Standard scaling)  |
| Nro. promedio reclamos anual | FLO | Normalización con media 0 y desviación estándar de 1 (Standard scaling) |
| Valor promedio reclamos anual	| FLO |	Normalización con media 0 y desviación estándar de 1 (Standard scaling) |
| Saldo pendiente |	INT	| Normalización con media 0 y desviación estándar de 1 (Standard scaling)  |
| Clase |	INT	| Normalización con media 0 y desviación estándar de 1 (Standard scaling) |


Vector de características resultante:


```

['x0_BANDA ANCHA PREACTIVADO PREPAGO BIESS|0/30',
 'x0_CHIP + 2',
 'x0_CHIP + PREPAGO',
 'x0_CHIP + |3/30',
 'x0_CNT CHIP HSPA PLUS',
 'x0_CNT CHIP PREPAGO AUXCOMPSA',
 'x0_CNT CONECTADOS PREACTIVADO PREPAGO |3/30',
 'x0_DATOS Y VOZ CBM 0 CTRL 3.5G',
 'x0_DISCAPACITADO HSPA PLUS CONTROL',
 'x0_EMPRESA ABIERTO 3.5G',
 'x0_EMPRESA CONTROL',
 'x0_EMPRESA CONTROL 3.5G',
 'x0_INDIVIDUAL CONTROLADO',
 'x0_MULTIPLAN CONTROL SERV PUBLICO HSPA',
 'x0_MULTIPLAN CONTROL SERVIDOR PUBLICO 3.5G',
 'x0_MULTIPLAN CONTROL SERVIDOR PUBLICO GSM',
 'x0_MULTIPLAN CONTROLADO 3.5G',
 'x0_MULTIPLAN CONTROLADO GSM',
 'x0_MULTIPLAN EMPRESAS PRIVADAS 4G/3G CONTROLADO',
 'x0_MULTIPLAN EMPRESAS PUBLICAS 4G/3G CONTROLADO',
 'x0_MULTIPLANES EMPRESAS ABIERTO HSPA PLUS',
 'x0_MULTIPLANES EMPRESAS CONTROLADO HSPA PLUS',
 'x0_MULTIPLANES PERSONAS CONTROLADO HSPA PLUS',
 'x0_PAGO LO QUE HABLO 3.5G CONTROL TD',
 'x0_PAGO LO QUE HABLO ABIERTO GRUPAL TU',
 'x0_PAGO LO QUE HABLO ABIERTO TU',
 'x0_PAGO LO QUE HABLO CONTROL GRUPAL TD',
 'x0_PAGO LO QUE HABLO CONTROL GRUPAL TU',
 'x0_PAGO LO QUE HABLO CONTROL TD',
 'x0_PAGO LO QUE HABLO CONTROL TU',
 'x0_PLAN CNT CHIP HSPA+',
 'x0_PLAN CNT CHIP HSPA+ |3/30',
 'x0_PLAN CNT EP AUTOCONSUMO CONTROLADO PERFIL 2',
 'x0_PLAN CNT EP AUTOCONSUMO CONTROLADO PERFIL 4',
 'x0_PLAN CNT EP AUTOCONSUMO CONTROLADO PERFIL 5',
 'x0_PLAN COMERCIALIZADORES PREPAGO',
 'x0_PLAN CONTROLADO DATOS +VOZ 1',
 'x0_PLAN CONTROLADO DATOS +VOZ 2',
 'x0_PLAN CONTROLADO DATOS +VOZ 3',
 'x0_PLAN CONTROLADO DATOS +VOZ 4',
 'x0_PLAN CONTROLADO DATOS +VOZ 5',
 'x0_PLAN CONTROLADO DATOS +VOZ 6',
 'x0_PLAN CONTROLADO DATOS +VOZ 7',
 'x0_PLAN DE PRUEBAS ABIERTO LTE (VOZ)',
 'x0_PLAN GENERICO WCC GSM',
 'x0_PLAN MOVIL ESPECIAL',
 'x0_PLAN PREACTIVADO TURISTAS 1GB',
 'x0_PLAN PREACTIVADO TURISTAS 500MB',
 'x0_PLAN PREACTIVADO TURISTAS 800MB',
 'x0_PLAN PREACTIVADO TURISTAS LTE CORP 1GB',
 'x0_PLAN PREPAGO MIGRACION 4G',
 'x0_PLAN PROMO CAMPANAS',
 'x0_PLAN TARIFA UNICA $0.08 HSPA PLUS CTRL IND',
 'x0_PLAN TODOS CONECTADOS',
 'x0_PLAN VOZ CTRL IND',
 'x0_PREACTIVADO CHIP + PREPAGO',
 'x0_PREACTIVADO CHIP + |3/30',
 'x0_PREACTIVADO CNT CHIP DISTRIBUIDOR',
 'x0_PREACTIVADO CNT CHIP HSPA+ |3/30',
 'x0_PREACTIVADO CNT CHIP PREPAGO AUXCOMPSA',
 'x0_PREACTIVADO PREPAGO CNT CHIP HSPA PLUS',
 'x0_PREACTIVADO PREPAGO CNT KIT TU |3/30 GSM',
 'x0_PREACTIVADO SUPER CHIP |0/30 HSPA PLUS',
 'x0_PREACTIVADO TD |3/30',
 'x0_TARIFA DIFERENCIADA HSPA PLUS',
 'x0_TARIFA UNICA 3.5G  CONTROL CORP',
 'x0_TARIFA UNICA 3.5G  CONTROL IND',
 'x0_TARIFA UNICA GSM  ABIERTO IND',
 'x0_TARIFA UNICA GSM  CONTROL IND',
 'x0_TARIFA UNICA HSPA PLUS CTRL IND',
 'x0_VIRTUAL EMPRESA GSM',
 'x1_C',
 'x1_P',
 'x1_S',
 'x2_CLIENTES CONTRATO 1 - 7',
 'x2_CLIENTES CONTRATO 16 - 22',
 'x2_CLIENTES CONTRATO 23 - 31',
 'x2_CLIENTES CONTRATO 8 - 15',
 'x2_CLIENTES VENTA DIRECTA',
 'x2_CLIENTES VENTA DIRECTA GSM',
 'x2_MULTIAGENCIAS CNT',
 'x2_PREPAGO',
 'x2_TELECSA',
 'x3_Cédula',
 'x3_Cédula de Extranjería',
 'x3_Otro',
 'x3_Pasaporte',
 'x3_R.U.C',
 'x4_MORA',
 'x4_PAZ Y SALVO',
 'x5_AMBATO',
 'x5_CUENCA',
 'edad',
 'antiguedad',
 'valor plan',
 'nro. promedio quejas anual',
 'nro. promedio reclamos anual',
 'valor promedio reclamos anual',
 'saldo pendiente']

```

Donde:
* X0: plan
* X1: tipo de plan
* X2: ciclo
* X3: tipo de identificación
* X4: estado financiero
* X5: ciudad 

