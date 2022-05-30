# Data Report

This document contains the results from the exploratory data analysis.

## General summary of the data 

Cargamos la información de las líneas móviles telefónicas activas y retiradas desde el año 2017 hasta el año 2019 a partir excel MLprojectlines.xlsx:

![1](https://user-images.githubusercontent.com/66392216/171025376-1555b59f-97da-4a49-9b4c-00d1182970b9.JPG)

![2](https://user-images.githubusercontent.com/66392216/171025523-68ad5aa9-3846-419e-918f-0d68d5908bec.JPG)

Se hace la verificación de las columnas 

![3](https://user-images.githubusercontent.com/66392216/171025833-6eaba477-58c7-4946-81de-56504aa78d7b.JPG)

![4](https://user-images.githubusercontent.com/66392216/171026323-c38faba0-ea0c-4a81-95e4-c341a54953ba.JPG)

![5](https://user-images.githubusercontent.com/66392216/171026501-0c24a0bb-d976-48f0-bba2-7e76e1d977df.JPG)

Se observan valores faltantes en la columna Fecha de retiro y en la columna Edad. La primera es debido a que el dataset también contiene productos activos y la segunda si se debe a registros incompletos.

![6](https://user-images.githubusercontent.com/66392216/171026689-31bc6edb-046d-4997-8573-1e9006217384.JPG)

De acuerdo a la media, desviación estándar, valor mínimo y máximo de cada una de las columnas, no se encuentran valores por fuera de lo normal. Se observa un valor máximo de los campos valor del plan, saldo pendiente y valor promedio de reclamos anual muy alto con respecto a la media, pero esto se debe a que existen algunos clientes corporativos los cuales pueden presentar este tipo de valores.

Verificamos valores de las variables categóricas del dataset:

![7](https://user-images.githubusercontent.com/66392216/171026873-92c750f9-8a9d-4ffb-b7e9-02ace93d3294.JPG)


Hacemos recuento de los posible valores de los atributos categóricos del dataset de líneas activas:

![8](https://user-images.githubusercontent.com/66392216/171027079-9e3a2dc6-1c57-4ace-a404-b2b26ecbabd9.JPG)

![9](https://user-images.githubusercontent.com/66392216/171027183-251d9266-5e72-42d6-bada-4496afa89a80.JPG)

![image](https://user-images.githubusercontent.com/66392216/171027253-93280659-e04f-4f04-a045-a1f0a4c400c4.png)

## Data quality summary

En general los datos se encuentran sin anomalías graves ni sesgos evidentes, las inconsistencias como la diferencia entre el promedio anual de reclamos es muy diferente a la media del resto de valores, sin  embargo, esto tiene una explicación (ya se ha explicado en el capítulo anterior)

## Target variable

Añadimos la columna Retiro, que indica si una línea está retirada o no (1: retirada, 0: no retirada).

![image](https://user-images.githubusercontent.com/66392216/171029311-1930731a-61fd-4280-9972-3870564b6515.png)

Se crea la columna Deserción, donde "1" significa que el usuario desistió del servicio y "0" que no desistió del servicio, a partir de la columna Estado:

![image](https://user-images.githubusercontent.com/66392216/171030653-8aec5f0b-8fb4-42e9-81e4-552902db19c6.png)

Creamos la columna Clase con los siguientes valores:

* 0 - Activo
* 1 - Retirado por falta de pago
* 2 - Retiro voluntario (deserción)

![image](https://user-images.githubusercontent.com/66392216/171030736-4e9d02cf-f8de-40e3-8fa1-fdfb5aea705a.png)

Eliminamos la columnas Estado, Retiro y Deserción utilizadas para calcular la columna Clase, y  establecemos la columna Código del producto cómo indice del dataset:

![image](https://user-images.githubusercontent.com/66392216/171030823-b5fcf5a5-13c8-4853-9424-5d5009cae7d5.png)


## Individual variables

Este será el dataset definitivo con el que realizaremos las tareas de aprendizaje supervisado y no supervisado:

![image](https://user-images.githubusercontent.com/66392216/171030990-b3680786-610d-4510-87fb-14ce8572a6ee.png)


## Variable ranking



## Relationship between explanatory variables and target variable

