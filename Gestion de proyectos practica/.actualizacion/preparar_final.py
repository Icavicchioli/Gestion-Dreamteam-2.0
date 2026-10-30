from pathlib import Path
import json
p=Path('.actualizacion/completar.mjs');s=p.read_text();s=s.replace("['Precio kit',400,'Libro original']","['Precio kit',800,'Decisión del usuario: 29/10/2026; receptividad por validar']")
idx=s.index('wb.recalculate();')
s=s[:idx]+'''a.getRange('B15').values=[[800]];
for(const n of ['Flujo de caja','Plan 12 meses','Cambios realizados'])wb.worksheets.getItem(n).getRange('A1').values=[['ANTECEDENTE — consultar Resumen nuevo, Flujo mensual nuevo y Plan 18 meses']];
sum.getRange('A20:C27').values=[['Conciliación previa','USD','Causa'],['Prototipos',1200,'12000 previstos; 10800 distribuidos'],['Bioquímica',12000,'Sin distribución'],['Consultas',-14000,'10000 previstos; 24000 distribuidos'],['QA',8000,'Sin distribución'],['Reserva',4800,'Sin distribución'],['Preserie',17103.06,'Omitida de egresos'],['Total diferencia',29103.06,'228303.06 menos 199200']];
for(const [r,c] of [[34,'C24'],[35,'D24'],[36,'E24'],[37,'C62'],[38,'D62'],[39,'E62'],[40,'C65'],[41,'D65'],[42,'E65']])a.getRange('B'+r).formulas=[["='Plan comercial'!"+c]];
plan.getRange('G1:L1').values=[['Mes','Ing. software','Ing. embebidos','Técnico QA','Técnico laboratorio','Capacidad por persona']];
for(let mm=1;mm<=18;mm++){plan.getRange(`G${mm+1}:L${mm+1}`).values=[[mm,null,null,null,null,160]];for(let z=0;z<4;z++){const c=String.fromCharCode(72+z);plan.getRange(`${c}${mm+1}`).formulas=[[`=SUMIF('Tareas y sprints'!$D$2:$D$196,G${mm+1},'Tareas y sprints'!$${c}$2:$${c}$196)`]];}}
plan.getRange('A17:E19').values=[['Dedicación','80% producto; 20% transversal',null,null,null],['Espera externa','Espera no equivale a esfuerzo. Se revisan hitos según autorizaciones.',null,null,null],['Previsión de unidades','Ventas y demos: equivalentes mensuales; producción y compras redondeadas.',null,null,null]];
''' +s[idx:]
s=s.replace("await fs.writeFile('.actualizacion/resultados.json'","await fs.writeFile('.actualizacion/mensual.json',JSON.stringify(m.getRange('A1:V49').values));await fs.writeFile('.actualizacion/resultados.json'")
s+='''\nconsole.log((await wb.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NUM!|#NAME\\\\?',options:{useRegex:true,maxResults:20},maxChars:1800})).ndjson);\n'''
Path('.actualizacion/ajuste-final.mjs').write_text(s)
rows=json.loads(Path('.actualizacion/tareas.json').read_text());out=[]
fronts=['Parche descartable','Lector reutilizable','Pulsera','Aplicación'];roles=['Ing. software','Ing. embebidos','Técnico QA','Técnico laboratorio']
months=[['Requisitos y rangos','Materiales, reactivos y electrodos','Canales y adhesivo','Muestras y microfluídica','Selectividad e interferencias','Calibración y estabilidad','Acoplamiento e integración','Repetibilidad por lote','Sudor, adhesión y recambio','Corrección de formulación','Documentación de fabricación','Aceptación MVP','Referencias clínicas','Desvíos de desempeño','Repetición de controles','Preparación de producción','Recepción de lotes','Liberación'],['Interfaces ópticas y eléctricas','Componentes y batería','Esquema y PCB','Compra, montaje y alimentación','Firmware de adquisición','Buffer y BLE simultáneo','Integración de cuatro productos','Carga, consumo y memoria','IP68 y alternancia','Correcciones PCB/firmware','Candidata y trazabilidad','MVP documentado','Versión clínica','Análisis de registros','Control de cambios','Fixtures','Recepción y programación','Liberación de lectores'],['Requisitos de sensores y LED','PPG, IMU y batería','Esquema y carcasa','Montaje y sensores','Firmware y gesto','BLE directo y semáforo','Integración de enlaces','LED, consumo y caducidad','IP68 y sudor','Correcciones','Guía de carga','Aceptación MVP','Versión clínica','Observaciones de uso','Regresión','Control de fabricación','Recepción de unidades','Liberación'],['Historias y datos','Contrato BLE y navegación','Simulación y almacenamiento','Vinculación BLE','Historial y lector activo','Recuperación sin duplicados','Integración completa','Evaluación de modelos','Avisos actuales y predictivos','Usabilidad y fallas','Candidata y ayuda','MVP documentado','Datos clínicos','Exactitud y alertas','Validación independiente','Soporte y distribución','Onboarding','Liberación']]
counts={m:len({x[4] for x in rows if x[3]==m}) for m in range(1,19)}
for x in rows:
 f=fronts.index(x[1]);m,sprint=x[3:5];lead=[3,1,2,0][f];k=sorted({y[4] for y in rows if y[3]==m}).index(sprint);x[2]=months[f][m-1]+': '+['preparación/ejecución','verificación/corrección','repetición/cierre'][k];x[5]=roles[lead];x[7:11]=[160/counts[m]*(.56 if z==lead else .08) for z in range(4)];x[11]=['Muestras y protocolo por lote','Versión de PCB/firmware y mediciones','Versión de pulsera y reporte','Aplicación instalable y reporte'][f];x[12]='Evidencia contra requisito del ciclo; revisión cruzada y desvíos críticos documentados'
 if sprint==14:x[6]=','.join('T13'+str(z) for z in range(1,5))
 out.append(x)
for sprint in range(1,40):
 m=next(x[3] for x in rows if x[4]==sprint);out.append([f'X{sprint:02d}','Transversal','Coordinación, compras, QA, documentación'+('; evidencia clínica/regulatoria' if m>=7 else '')+('; captación de aliados' if m>=9 else ''),m,sprint,'Equipo; técnico laboratorio coordina',f'X{sprint-1:02d}' if sprint>1 else 'Inicio',*[160/counts[m]*.2]*4,'Órdenes, actas, dossier y contactos','Recepción trazable; revisión de riesgos; ensayos autorizados; siguiente acción con responsable'])
out.sort(key=lambda x:(x[4],x[0]));Path('.actualizacion/tareas.json').write_text(json.dumps(out,ensure_ascii=False))
for m in range(1,19):
 for c in range(7,11):assert abs(sum(x[c] for x in out if x[3]==m)-160)<1e-6
print('Preparadas 195 tareas; capacidad de cuatro recursos comprobada; script final guardado.')
