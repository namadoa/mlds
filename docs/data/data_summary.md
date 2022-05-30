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


## Data quality summary

## Target variable

## Individual variables

## Variable ranking

## Relationship between explanatory variables and target variable




Se observa más de un 89% de datos faltantes para las columnas Género, Estado 
civil, Profesión, Grado de escolaridad, Nivel de ingresos y de egresos. Esto se debe a que en el sistema transaccional no es requerido ingresar esta información al momento de registrar nuevos usuarios. Otras columnas con valores faltantes pero en una medida mucho menor que las antes mecionadas son las columnas Tipo de identificación y Fecha de nacimiento.

Este dataset no contiene datos numéricos a parte del código del cliente por lo que el método describe() no arroja información de importancia.