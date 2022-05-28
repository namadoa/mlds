# Data Dictionary

El data set consiste en archivos con extensión .csv con la información de los usuarios retirados y no retirados de los diferentes planes de línea móvil de la empresa, además de otras variables asociadas al cliente. Dichos datos son estructurados. 

# Database Name 1

## Table 1

Consiste en dos archivos .csv, uno con la información de las líneas activas hasta el año 2019 y otro con la información de las líneas retiradas entre los años 2017 y 2019. Estos archivos contienen los siguientes datos:

| column | type | description | values |
| --- | --- | --- | -- |
| Código del producto | INT | Identificador de la línea ||
| Código del cliente  | INT | Identificador usuario dueño de la línea||
| Fecha de instalación| DATE| Fecha de instalación del servicio||
| Fecha de retiro     | DATE| Fecha de desinstalación del servicio|| 
| Plan                | STRING | Plan de la oferta comercial suscrito por la línea||
| Tipo de plan        | STRING | Tipo de plan | P: prepago, S: postpago, C: control |
| Valor plan          | INT | Valor mensual que se debe pagar por el plan ||
| Código estado       | INT | Identificador del estado de conexión de la línea para líneas retiradas | 92 (retirado), 94 (retirado), 95 (retiro atención al cliente), 110 (retirado sin instalación) |
| Estado              | STRING | Descripción del estado de la línea |conexion, suspension parcial, suspension total, inactivo, orden de conexion, orden de suspension parcial, retirado, retiro atencion cliente,retiro sin instalación  |
| Ciclo               | STRING | División administrativa de las líneas ||
| Estado financiero   | STRING | Estado de la deuda del servicio |  paz y salvo, mora |
| Saldo pendiente     | INT    | Valor total adeudado a la fecha ||
| Valor en reclamo    | INT    | Valor total reclamos facturación a la fecha |

## Table 2

Consiste en dos archivos .csv, uno con la información de los clientes dueños de las líneas activas y otro con la información de los clientes dueños de las líneas retiradas. Estos archivos contienen los siguientes datos:

| column | type | description | values |
| --- | --- | --- | -- |
| Código del cliente | INT | Identificador usuario dueño de la línea ||
| Tipo de cliente | STRING | Tipo de cliente | normal, prueba plan, vip, masivo, corporativo
| Tipo de identificación | STRING | Tipo de identificación del cliente| Cédula, R.U.C, Pasaporte, Cédula de Extranjería, Otro |
| Fecha de nacimiento | DATE | Fecha de nacimiento del cliente | |
| Género | STRING | Género del cliente | M (Masculino), F (Femenino) ||
| Estado civil | STRING | Estado civil del cliente | Soltero, Casado ||
|Profesión | STRING |Profesión del cliente||
|Grado de escolaridad | STRING | Grado de escolaridad  del cliente | Educación básica, Secundaria, Universidad 
| Nivel de ingresos | STRING | Nivel de ingresos del cliente | 300 - 500, 500 - 800, 800 – 1000, 1000 - 1500, 1500 - > |
| Ciudad | STRING | Ciudad de residencia del cliente | Ambato, Cuenca

## Table 3

Consiste en un archivo .csv con la información de las quejas sobre las líneas activas y retiradas. Este archivo contiene los siguientes datos:

| column | type | description | values |
| --- | --- | --- | -- |
| Número de solicitud | INT | Identificador de la solicitud de queja ||
| Fecha de registro | DATE | Fecha de registro de la solicitud ||
| Producto | INT | Identificador de la línea ||
| Tipo | STRING | Tipo de la solicitud | Registro de Quejas ||
| Estado | STRING | Estado de la solicitud | Registrado, Anulado, Atendido |
| Fecha de atención | DATE | Fecha en que se atendió la solicitud ||
| Tipo de observación | STRING | Tipo de observación de la solicitud | De Atención al Cliente a Ordenes|
| Observación | STRING | Observación con información adicional de la solicitud en formato libre ||


## Table 4

Consiste en un archivo .csv con la información de los reclamos de facturación sobre las líneas activas y retiradas Este archivo contiene los siguientes datos:

| column | type | description | values |
| --- | --- | --- | -- |
| número de solicitud | INT | Identificador de la solicitud de reclamo |
| fecha de registro | DATE | Fecha de registro de la solicitud |
| producto | INT | Identificador de la línea ||
| tipo | STRING | Tipo de la solicitud | Reclamos |
| estado | STRING | Estado de la solicitud | Anulado, Atendido
| fecha de atención | DATE | Fecha en que se atendió la solicitud || 
| valor reclamado | INT | Valor reclamado por el cliente sobre su factura ||
| tipo de observación | STRING | Tipo de observación de atención de la solicitud | Accede, No Accede, Anulado |
| observación | STRING | Observación con información adicional de la solicitud en formato libre ||









