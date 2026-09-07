# Basadas en las especificaciones del marco normativo actual

## Sobre condiciones de vuelo y reglas de vuelo

- **ESP-NOR-01 — Requisitos previos de operación.** Antes de cada misión, el servicio deberá verificar la categoría aeronáutica aplicable, el registro del dron cuando corresponda y la autorización del titular o administrador del predio para realizar el relevamiento. Se deberá identificar al piloto responsable y, como criterio conservador del proyecto, contar con seguro de responsabilidad civil que cubra la actividad.

- **ESP-NOR-02 — Altura de vuelo.** En espacio aéreo no controlado, el sistema deberá mantener la aeronave por debajo de 400 pies sobre el terreno local —121,92 m, aproximadamente 122 m—, considerando el relieve y el error de medición. El límite deberá respetarse también durante el retorno automático y reducirse cuando exista una restricción específica de la zona.

- **ESP-NOR-03 — Área de operación y restricciones.** El sistema deberá mostrar la posición del dron y verificar que la trayectoria respeta el área de operación autorizada y las exclusiones del relevamiento. Antes de cada misión se deberá comprobar información aeronáutica oficial vigente sobre aeródromos, helipuertos, corredores y restricciones permanentes o temporales. No se deberá habilitar una trayectoria incompatible con esas condiciones o sin las autorizaciones exigibles.

- **ESP-NOR-04 — Alcance visual y control humano.** Como criterio inicial del proyecto, el vuelo deberá realizarse manteniendo contacto visual con la aeronave, con apoyo de observadores cuando corresponda. El piloto deberá poder modificar o interrumpir cualquier ruta automática y operar una sola aeronave a la vez. Si la superficie no puede cubrirse bajo estas condiciones, el relevamiento deberá dividirse en varios vuelos.

- **ESP-NOR-05 — Seguridad de personas y otras aeronaves.** La operación deberá mantener vigilancia del tránsito aéreo y ceder el paso a las aeronaves que tengan prioridad, especialmente aviones y helicópteros agrícolas. No se deberán planificar sobrevuelos de aglomeraciones ni, como criterio inicial, de personas ajenas a la operación. Ante un conflicto o ingreso de terceros al área de riesgo, el piloto deberá interrumpir el relevamiento y aplicar una maniobra segura.

- **ESP-NOR-06 — Condiciones del equipo, enlace y contingencias.** El dron deberá operar dentro de los límites ambientales y de carga del fabricante, con mantenimiento vigente y sin desactivar sensores vitales. Deberá mostrar al piloto el estado del enlace de mando y control y de la batería. Ante pérdida de enlace, energía insuficiente o falla de navegación, deberá ejecutar una contingencia previamente definida y probada, utilizando retorno automático únicamente cuando pueda realizarse con seguridad.

## Sobre datos personales

- **ESP-NOR-07 — Finalidad y minimización.** El sistema deberá limitar la captura y el tratamiento de datos personales a lo necesario para el relevamiento contratado. Deberá evitar captar personas, viviendas y actividad de predios vecinos ajenas a esa finalidad, considerando también los metadatos o asociaciones que permitan identificar a una persona. La información no deberá utilizarse para finalidades incompatibles con las informadas.

- **ESP-NOR-08 — Disociación de imágenes.** Cuando se capten incidentalmente datos personales innecesarios para el relevamiento, deberán eliminarse o disociarse de manera irreversible en el menor plazo técnicamente posible y antes de entregar los resultados. El procedimiento deberá contemplar rostros, matrículas, metadatos y copias originales que permitan identificar a las personas.

- **ESP-NOR-09 — Información y consentimiento.** Antes de recolectar datos personales, el responsable deberá informar la finalidad, los destinatarios, su identidad y los derechos de los titulares, y documentar el consentimiento o la excepción legal aplicable. Se deberán prever medios de información para trabajadores y visitantes. La autorización del productor para relevar el lote no se considerará consentimiento de todas las personas presentes.

- **ESP-NOR-10 — Seguridad, confidencialidad y proveedores.** El sistema deberá proteger imágenes y datos contra acceso, modificación, pérdida o divulgación no autorizados, limitando el acceso por función y cliente. El servicio deberá definir las obligaciones de confidencialidad de sus proveedores y verificar las condiciones legales de las transferencias internacionales de datos personales. El uso de información para entrenar modelos o compartirla con terceros requerirá los permisos contractuales y fundamentos legales correspondientes.

- **ESP-NOR-11 — Conservación y derechos sobre los datos.** El servicio deberá disponer de una política de privacidad que defina conservación, eliminación y atención de solicitudes de los titulares, e inscribir las bases alcanzadas por esa obligación. Los datos deberán eliminarse o disociarse cuando dejen de ser necesarios, salvo conservación legalmente justificada. Se deberán atender los pedidos de acceso dentro de diez días corridos desde la intimación fehaciente y los de rectificación, actualización o supresión procedente dentro de cinco días hábiles.

## Sobre comunicaciones

- **ESP-NOR-12 — Banda y parámetros de emisión.** Si se utiliza LoRa para sensores terrestres o meteorológicos bajo el régimen de banda compartida previsto, deberá configurarse dentro de 915–928 MHz y respetar los límites de potencia, emisiones y demás parámetros técnicos aplicables. Los cambios de antena, potencia o configuración que afecten la emisión deberán revisarse antes de habilitarse. Esta banda no se impone a los enlaces de mando o video del dron.

- **ESP-NOR-13 — Homologación y RAMATEL.** Antes de integrar equipos de radio, se deberá verificar y documentar su homologación, codificación, autorización o excepción aplicable y su inscripción RAMATEL cuando corresponda. La comprobación deberá considerar el modelo y su configuración final, incluidos los módulos y antenas utilizados, según el régimen vigente al momento de incorporación.

- **ESP-NOR-14 — Uso de LoRa y convivencia.** Como decisión técnica del proyecto, LoRa se utilizará para telemetría de baja tasa de sensores y no reemplazará el enlace de mando y control ni el de video del dron. El sistema deberá contemplar interferencias y pérdidas de mensajes, identificar las lecturas desactualizadas y limitar los reintentos y la ocupación innecesaria del espectro. La pérdida del enlace de sensores no deberá impedir la intervención del piloto.

## Sobre el alcance del diagnóstico y las recomendaciones

- **ESP-NOR-15 — Validación profesional y prescripciones.** Los informes deberán distinguir indicios de plaga de diagnósticos validados y expresar las limitaciones de detección. Las recomendaciones deberán ser elaboradas o validadas por un ingeniero agrónomo habilitado según la jurisdicción. Cuando los mapas incluyan producto, dosis o condiciones de aplicación, deberán respetar los usos autorizados y contar con la receta exigible; el mapa no sustituirá esa receta. La aplicación física de fitosanitarios permanecerá excluida del servicio, conforme a ESP-SRV-16.
