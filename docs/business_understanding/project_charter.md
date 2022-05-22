# Project Charter

## Business background

* Who is the client, what business domain the client is in.

El cliente es la empresa CNT móvil, CNT móvil es una empresa dedicada a la prestación del servicio de telefonía móvil en Ecuador.
 

* What business problems are we trying to address?

<<<<<<< HEAD
CNT móvil en los últimos años ha presentado tasas importantes el retiro del servicio, ya sea por falta de pago (deudores morosos) o por abandono del servicio (deserción) (más de 11000 líneas retiradas entre 2017 y 2019, solo en las ciudades de Ambato y Cuenca), causando inestabilidad financiera a la empresa y posiblemente una futura quiebra si no se toman acciones oportunas.

 
=======
>>>>>>> d064697f5e2c3c423cb7ba39633fb7b5edb19dc9
## Scope
* What data science solutions are we trying to build?

El objetivo del proyecto es mejorar mediante herramientas de aprendizaje no supervisado la caracterización de los clientes que se retiran del servicio de telefonía móvil, ya sea por falta de pago (deudores morosos) o por abandono del servicio (deserción), con el fin de que CNT móvil pueda tomar decisiones oportunas y más enfocadas en ciertas poblaciones para disminuir el índice de retiros de cliente del servicio.

* How is it going to be consumed by the customer?

Se creará una API para que el cliente, a medida que ingresa nuevos datos, el modelo  retorna una clasificación/segmentación de los datos 

## Personnel
* Who are on this project:
	* Microsoft:
		* Nicolás Amado
		* Cristhian Córdoba
		* Cesar Gamba
	* Client:
		* Data administrator: CNT 
		* Business contact: CNT representante
	
## Metrics
* What are the qualitative objectives? (e.g. reduce user churn)
Reducir del índice mensual de retiros tanto por falta de pago como por deserciones.


## Plan
* Phases (milestones), timeline, short description of what we'll do in each phase.

Se escoge la TDSP como la metodología a seguir para el desarrollo de este proyecto,
La primera parte consiste en el entendimiento del negocio, que se traduce en un entendimiento macro del mercado, es decir se determinará las características relevantes, el tipo de información que se tiene, donde están cuantos registros se pueden tener, cuantas columnas de datos se pueden recolectar, el número de registros, el lugar en el cual se puede obtener la información, la importancia de cada una de estas características y la relación general entre estas características.
A continuación se adquirirán los datos y se explorarán de manera más profunda, se deberá saber en qué formato se encuentran estos archivos, donde se pueden encontrar y en qué estado están, además se deberá hacer un estudio más detallado de estos datos, se deberá buscar que valores atípicos o errores se pueden tener, determinar la calidad de los mismos y proceder a realizarle el respectivo pre procesamiento, de qué forma se pueden implementar en el modelo de tal manera que sea optimo al momento de usarlos, además se deberá saber cada cuanto estos datos son actualizados
En la parte de modelamiento se realizará el entrenamiento del modelo con un optimizador lbfgs para una red neuronal de k número de neuronas (dicho número es variable y deberá obtenerse), con funciones de activación, relu, logistic, y tanh y su respectiva validación mediante un GridSearchCV con 5 pliegues, en esta parte se determinará los mejores parámetros para el problema, es decir el número de neuronas más eficiente y la función de activación más adecuada.
Finalmente, se realizaría el despliegue.


## Architecture
* Data
  * What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)

  Archivos en on-prem files en el servidor del cliente, con extensión CSV. 

* Data movement from on-prem to Azure using ADF or other data movement tools (Azcopy, EventHub etc.) to move either
  * GCP para el almacenado los datos raw, para luego enviarlo a DVC y en allí con el pypeline de preprocesamiento se entregarán los datos al modelo y una vez hecho esto se enviara el resultado de dicho entrenamiento, junto con el dataset preprocesado al repositorio de github, el versionado del codigo se hara por medio de Git.

* What tools and data storage/analytics resources will be used in the solution e.g.,
  * DVC, weights and biases , GCP, MLflow 


## Communication
* How will we keep in touch? Weekly meetings?
Se plantea reuniones semanales para el desarrollo de este proyecto     
* Who are the contact persons on both sides?
Las personas en contacto será el customer o cliente y el equipo e desarrollo

