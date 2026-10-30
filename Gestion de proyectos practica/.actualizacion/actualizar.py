from pathlib import Path
import json,re
root=Path.cwd(); tex=root/'Gestion de proyectos practica'
# Retirar marcadores pendientes ya sustituidos por especificaciones aprobadas.
for p in tex.glob('*.tex'):
 t=p.read_text(); needle=r'\textcolor{red}{'; start=0
 while (a:=t.find(needle,start))>=0:
  j=a+len(needle); depth=1
  while depth and j<len(t):
   depth+=(t[j]=='{')-(t[j]=='}');j+=1
  t=t[:a]+t[j:];start=a
 t=t.replace('La validación clínica y la certificación comercial no están incluidas.','El programa incorpora evaluación clínica y autorización de comercialización, con cierre previsto en el mes 18.').replace('El alcance no incluye validación clínica, certificación comercial ni afirmaciones diagnósticas; incorporarlas exigiría presupuesto, cronograma, protocolo y autoridades competentes específicos.','El programa incluye evaluación clínica y autorizaciones sanitarias entre el prototipo del mes 7 y el cierre previsto del mes 18; las ventas se proyectan desde el mes 19.').replace('los dispositivos se comunican únicamente con el teléfono por BLE','los dispositivos se comunican con el teléfono por BLE y el lector activo mantiene además un enlace directo con la pulsera')
 if p.name=='Evaluacion del proyecto.tex':
  t=t.replace(r'\draw[remoto] (hub.east)',r'\draw[flujo] (parche.east) -- node[etiqueta, above] {BLE directo: lectura actual} (pulsera.west);'+'\n'+r'\draw[remoto] (hub.east)')
  t=t.replace('Lector y pulsera','Dos lectores y una pulsera').replace('Parche\\\\en sobre individual','Dos parches\\\\en sobres individuales').replace('Accesorios\\\\de carga','Fuente USB-C dual\\\\y dos cables').replace('Carga, protección y regulación};','USB-C sellado, carga\\\\protección y regulación};')
  t=t.replace('Microcontrolador\\\\Adquisición\\\\y filtrado\\\\','Microcontrolador\\\\Adquisición y filtrado\\\\LED RGB y gesto\\\\')
  cut=t.index(r'\caption{Costos estimados por dispositivo')
  # Retirar desde el inicio de la tabla económica hasta el fin; reemplazo integral a continuación.
  a=t.rfind(r'\begin{table}',0,cut)
  t=t[:a]+r'\input{Economia actualizada.tex}'+'\n'
 p.write_text(t)
# Especificaciones autoritativas integradas después de requerimientos.
spec=r'''
\subsubsection{Configuración de entrega, carga y continuidad}
El kit contiene una pulsera, dos módulos lectores reutilizables de 750 mAh, dos parches descartables iniciales, una fuente USB-C con dos salidas, dos cables USB-C y documentación. Cada lector y la pulsera de 850 mAh incorporan entrada USB-C, controlador de carga, protección y supervisión térmica. El tiempo de carga es informativo y se determinará con la celda seleccionada; la pulsera se carga durante el descanso y los lectores se alternan. La potencia de la fuente no sustituye los límites de corriente de la batería.
Para cambiar el lector se sincronizan sus datos, se retira, se acopla el lector cargado y la aplicación confirma su identificación y calibración como lector activo. No se combinan como simultáneas las lecturas de los dos módulos. Durante la recarga de la pulsera se interrumpen sus señales fisiológicas y su indicador portátil; el lector continúa registrando y transmitiendo a la aplicación. El historial identifica esos intervalos sin contexto.
\paragraph{Protección ambiental}
Se adopta IP68 conforme a IEC 60529 como objetivo para las envolventes electrónicas: polvo IP6X e inmersión de referencia a 1,5 m durante 30 minutos, con el cable desconectado. Se seleccionará un receptáculo USB-C sellado en condición desconectada y se verificará su unión con la carcasa. El ensayo corresponde al conjunto terminado y se repetirá tras ciclos de conexión y recambio. Se ensayan por separado sudor artificial, corrosión y adhesión. La zona de captación del parche permanece accesible. La carga se realiza con el puerto seco.
\paragraph{Adquisición y enlaces}
El lector genera una medición procesada cada dos minutos y conserva registros de 64 bytes; la sincronización nominal al teléfono ocurre cada cinco minutos. Cada nueva lectura se envía también por BLE directo a la pulsera, sin esperar esa sincronización. El mensaje incluye lector activo, secuencia, marca temporal, unidad, valor y calidad. La pulsera ignora duplicados y lectores inactivos; después de dos períodos sin lectura válida muestra ausencia de datos. Se prueban los enlaces simultáneos y la recuperación al reconectar.
\paragraph{Indicador RGB}
La pulsera indica la última lectura: verde dentro del rango establecido; amarillo próximo al límite o que requiere atención; rojo lectura anómala que requiere consultar la aplicación y verificar con el método de referencia indicado. Los rangos se fijan y validan en la evaluación clínica. La aplicación es la interfaz principal para historial, interpretación y avisos actuales y predictivos. El verde describe una lectura, no una garantía general de salud.
El LED permanece apagado en reposo. Un gesto detectado por la IMU lo enciende tres segundos. El rojo agrega un destello de 100 ms cada diez segundos; la ausencia o caducidad de datos se representa con dos destellos amarillos al consultar. Se limita la corriente del LED a 1 mA.
\paragraph{Revisión de energía}
El presupuesto previo reserva 3,5 mA medios para el lector y 4,0 mA para la pulsera. Dentro de esos límites se asignan 0,2 mA y 0,3 mA respectivamente a BLE adicional, gesto y señalización, quedando 3,3 mA y 3,7 mA para las demás funciones. Un destello de 1 mA por 100 ms cada diez segundos consume 0,01 mA medio; 30 consultas diarias de tres segundos agregan 0,0011 mA. Con reserva del 20\%, las autonomías presupuestadas siguen siendo $750\times0,8/3,5=171$ h y $850\times0,8/4=170$ h. Estas asignaciones son límites de diseño, sujetos a medir consumo por estado y descarga completa con todos los enlaces y el LED activos.
'''
p=tex/'Evaluacion del proyecto.tex';t=p.read_text();pos=t.index(r'\subsubsection{Diseño preliminar');t=t[:pos]+spec+'\n'+t[pos:];p.write_text(t)
# Datos de planificación detallada.
fronts=['Parche descartable','Lector reutilizable','Pulsera','Aplicación']
stages=[['Requisitos y criterios de aceptación','Interfaces, componentes y proveedores','Protocolos y diseño detallado'],['Fabricación de muestras y montaje inicial','Firmware, adquisición y pruebas unitarias','Calibración y ensayos de subsistema'],['Integración extremo a extremo'],['Pruebas de autonomía, BLE y recuperación','Protección, recambio y usabilidad','Correcciones y candidato a MVP'],['Aceptación técnica y documentación','MVP técnico y expediente actualizado'],['Evidencia clínica y respuesta a observaciones','Ensayos complementarios y control de cambios','Preparación de producción y aliados','Registro y documentación de uso','Recepción del lote comercial','Autorizaciones y preparación de lanzamiento']]
monthstage=sum(stages,[]);counts=[2,2,2,2,2,3,2,2,3,2,2,2,2,2,2,2,2,3];tasks=[];s=0
for m,count in enumerate(counts,1):
 for k in range(count):
  s+=1
  for f,front in enumerate(fronts):
   hours=[round(160/count*(.7 if x==f else .1),6) for x in range(4)]
   tasks.append([f'T{s:02d}{f+1}',front,monthstage[m-1]+f' — incremento {k+1}',m,s,['Técnico laboratorio','Ing. embebidos','Técnico QA','Ing. software'][f],f'T{s-1:02d}{f+1}' if s>1 else 'Inicio',*hours,'Especificación o versión ensayable, registro de pruebas y desvíos','Revisión cruzada y evidencia contra requisitos; fallas críticas con acción y fecha'])
assert s==39
(root/'.actualizacion/tareas.json').write_text(json.dumps(tasks,ensure_ascii=False))
planning=r'''\clearpage
\section{Planificación del proyecto}
El programa combina cuatro frentes paralelos: parche descartable, lector reutilizable, pulsera y aplicación. Compras, integración, QA, clínica, regulación y captación de aliados son actividades transversales. El desarrollo dura doce meses y el cierre regulatorio se prevé en el mes 18. El prototipo integrado del mes 7 habilita la revisión de aptitud y el avance de presentaciones según la evidencia disponible.
\subsection{Equipo, capacidad y sprints}
Se mantienen dos perfiles de ingeniería y dos técnicos/administrativos hasta el mes 18, a 160 horas mensuales por persona: 7.680 horas el primer año y 3.840 horas adicionales. Las horas controlan capacidad y no se vuelven a sumar como salarios por tarea. Los cuatro recursos se comparten entre frentes y realizan revisión cruzada. Laboratorios e investigadores clínicos se contratan como servicios externos.
Se planifican 26 sprints de dos semanas el primer año y 13 durante los meses 13--18. La asignación mensual de capacidad se ajusta a los dos o tres sprints de cada mes; no se multiplica automáticamente cada sprint por 80 horas. Cada tarea incluye ID, producto, dependencia, sprint, responsable, horas por recurso, entregable y aceptación en la hoja Tareas y sprints. La compra, recepción, revisión externa y autorización conservan sus esperas independientes del esfuerzo.
\begin{center}\begin{tabular}{lll}\hline
Meses & Sprints & Resultado\\\hline
1--3 & 1--6 & Requisitos, interfaces, proveedores\\
4--6 & 7--13 & Subsistemas construidos y ensayados\\
7 & 14--15 & Prototipo integrado\\
8--10 & 16--22 & Pruebas, correcciones y avance regulatorio\\
11--12 & 23--26 & MVP técnico y documentación\\
13--18 & 27--39 & Evaluación, registro y lanzamiento preparado\\\hline
\end{tabular}\end{center}
\subsection{Secuencia por producto}
Parche: materiales y reactivos, muestras, calibración e interferencias, estabilidad y adhesión, fabricación y control de lotes. Lector: interfaces, componentes y PCB, montaje, firmware y adquisición, memoria y BLE, USB-C y carcasa, pruebas. Pulsera: sensores y PCB, montaje, firmware, BLE directo y LED, alimentación y protección, pruebas. Aplicación: interfaces y datos, BLE, historial, calidad y recuperación, avisos actuales, predicciones y ayuda. La integración exige versiones compatibles y resultados individuales disponibles. Cada sprint cierra con demostración, revisión de riesgos y evidencia.
\subsection{Evaluación clínica y autorizaciones}
La preparación de requisitos, asesoramiento y documentación comienza en los meses 1--6. Desde el prototipo del mes 7 se avanza con los ensayos y presentaciones permitidos por la evidencia de seguridad. Participan ANMAT, el comité de ética y el centro clínico para autorizar la investigación; se distingue esa autorización del registro para comercializar. Se incluye el encuadre de la aplicación, fabricación/importación y revisión de homologación BLE ante ENACOM. Los estudios con participantes se realizan después de las autorizaciones correspondientes. Se prevén evaluación de mediciones y alertas frente a referencia, resultados, observaciones, correcciones y documentación; el presente plan no desarrolla un protocolo clínico completo.
El cierre regulatorio hacia el mes 18 es una previsión ajustable. La captación de médicos y clínicas avanza desde el mes 9 con responsables técnicos/administrativos y asesoramiento externo. Las ventas comienzan desde el mes 19, sujetas a autorizaciones. Las unidades de investigación se distinguen de los 100 kits comerciales previstos para el lanzamiento.
\subsection{Control y aceptación}
La revisión mensual concilia tareas, capacidad, compras, costos y riesgos. Se comprueban adquisición, calibración, interferencias, autonomía, memoria y retención, BLE simultáneo, recuperación, recambio de lector, carga, temperatura, IP68 y sudor, LED con datos válidos o vencidos y trazabilidad de lotes. Los meses 3, 6, 7, 10, 12 y 18 tienen revisión formal. Los cambios afectan simultáneamente backlog, cronograma, presupuesto, documentación y evidencia clínica cuando corresponda.
'''
(tex/'Planificacion del proyecto.tex').write_text(planning)
inv=['USB-C y accesorios','Dos lectores y dos descartables','Protección IP68 y sudor','BLE directo y diagramas','LED y gesto','Autonomía y frecuencia','Cuatro frentes y sprints','Evaluación y autoridades','18 meses y ventas desde 19','Conciliación y flujo mensual']
(root/'Inventario de correcciones.txt').write_text('Actualización 29/10/2026\nOrigen: comentarios.txt, diez marcas rojas del LaTeX y decisiones de la conversación.\n'+ '\n'.join(f'C{i:02d}. {x}. Resolución: especificaciones, planificación y modelo actualizado. Cierre: revisar coherencia con las pruebas y cifras del libro.' for i,x in enumerate(inv,1))+'\nLas pruebas de producto son actividades planificadas, no ensayos realizados.\n')
