import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {Presentation,PresentationFile} from '@oai/artifact-tool';
const root=process.cwd(),build=path.join(root,'.build_slides/v3'),out=path.join(root,'entregables/v3');
const skill='/Users/i.e.cavicchioli/.codex/plugins/cache/openai-primary-runtime/presentations/26.1013.11914/skills/presentations';
const {makeNativeBulletParagraphs,finalizePresentation}=await import(pathToFileURL(skill+'/container_tools/artifact_tool_utils.mjs'));
const data=JSON.parse(await fs.readFile(build+'/contenido.json','utf8'));
const cat=JSON.parse(await fs.readFile(root+'/citas/catalogo.json','utf8'));
const assets=JSON.parse(await fs.readFile(root+'/citas/presentacion_v3/catalogo.json','utf8'));
const C={ink:'#172B3A',blue:'#126FA1',muted:'#51616D',white:'#FFFFFF'};
const P=Presentation.create({slideSize:{width:1280,height:720}});
function text(s,t,x,y,w,h=55,size=36,color=C.ink,bold=false){
 const a=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 a.text=t;a.text.style={typeface:'Arial',fontSize:size,color,bold,wrap:'none',autoFit:'none'};a.text.insets=0;return a;
}
function bullets(s,items,x,y,w,h=260){
 if(!items.length)return;
 const a=text(s,'',x,y,w,h,32);
 a.text=makeNativeBulletParagraphs(items,{marginLeftPoints:20,hangingPoints:12,spaceAfterPoints:20});
 a.text.style={typeface:'Arial',fontSize:32,color:C.ink,autoFit:'none',wrap:'none'};
}
async function picture(s,file,x,y,w,h){
 const b=await fs.readFile(root+'/'+file);s.images.add({blob:b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),contentType:file.endsWith('.jpg')?'image/jpeg':'image/png',alt:file,fit:'contain',position:{left:x,top:y,width:w,height:h}});
}
function refs(d){return d.refs.map(id=>{let r=cat.find(x=>x.id===id);return `${id}. ${r.titulo}. ${r.fecha}\n${r.url}\nArchivo local: citas/${r.archivo}`;}).join('\n\n');}
function imageRefs(i){const keys={1:['portada'],3:['solar'],4:['jupiter'],6:['integracion'],11:['H01']};return (keys[i]||[]).map(k=>{let r=assets.find(x=>x.id===k);return r?`${k}: ${r.url}\nArchivo local: citas/presentacion_v3/${r.archivo}`:'';}).join('\n');}
const notes=[];
for(let i=0;i<data.length;i++){
 const d=data[i],s=P.slides.add();s.background.fill=C.white;
 text(s,String(i+1).padStart(2,'0'),1165,656,66,44,32,C.blue);
 if(d.layout==='cover'){
  text(s,d.title,64,56,1130,130,54,C.ink,true);
  text(s,'Ignacio Cavicchioli',64,268,520,55,36,C.blue);
  text(s,'Qué altera la radiación',64,390,545,55,36);
  text(s,'y cómo se afrontó.',64,442,545,55,36);
  await picture(s,d.image,660,250,555,330);
 }else{
  text(s,d.title,64,48,1150,70,46,C.ink,true);
  if(d.layout==='figure'){
   text(s,d.intro[0],64,142,1150,60,34);
   await picture(s,d.image,360,207,720,395);
   if(i===19){text(s,'Δ(1/hFE)',64,325,260,48,32,C.blue);text(s,'IC en mA',64,395,260,48,32,C.blue);}
   if(i===20){text(s,'ID en µA',64,325,260,48,32,C.blue);text(s,'VG en V',64,395,260,48,32,C.blue);text(s,'Antes / 150 krad',930,325,300,48,32,C.blue);}
   if(i===21){text(s,'Salida en V',64,325,270,48,32,C.blue);text(s,'Tiempo en s',64,395,270,48,32,C.blue);}
   text(s,d.caption,64,608,1100,45,32,C.muted);
  }else{
   d.intro.forEach((t,j)=>text(s,t,64,155+j*53,1150,52,36));
   if(d.image){
    bullets(s,d.bullets,64,330,552,260);
    await picture(s,d.image,658,300,557,280);
    const capLines={3:['SOHO, julio de 1996'],4:['Cinturones observados por Cassini'],5:['Ilustración NASA de la heliosfera'],6:['Voyager 2 en pruebas','Marzo de 1977'],7:['Hardware FDS, fotografía JPL'],11:['Fotodiodo: ejemplo equivalente'],12:['Sección de BJT NPN, JPL'],13:['Sección NMOS, ejemplo JPL']}[i+1]||[d.caption];
    capLines.forEach((t,j)=>text(s,t,658,587+j*38,557,40,32,C.muted));
   }else bullets(s,d.bullets,64,340,1140,260);
  }
 }
 const duration=d.time?`${Math.floor(d.time/60)}:${String(d.time%60).padStart(2,'0')}`:'fuera del recorrido';
 const note=`TIEMPO: ${duration}\n\nGUION ORAL\n${d.oral}\n\nLECTURA DE LA IMAGEN Y ALCANCE\n${d.visual}\n\nLOCALIZADORES\n${d.loc}\n\nFUENTES\n${refs(d)}\n${imageRefs(i+1)}`;
 s.speakerNotes.text=note;
 notes.push(`## ${i+1}. ${d.title.replace('\n',' ')}\n\nTiempo: ${duration}\n\n### Texto en pantalla\n\n${d.intro.join('\n\n')}\n\n${d.bullets.map(t=>'- '+t).join('\n')}\n\n### Guion oral\n\n${d.oral}\n\n### Figura y alcance\n\n${d.visual}\n\n### Fuentes\n\n${d.loc}\n\n${refs(d)}\n${imageRefs(i+1)}`);
 await fs.writeFile(build+'/renders/'+String(i+1).padStart(2,'0')+'.png',new Uint8Array(await (await P.export({slide:s,format:'png',scale:1.5})).arrayBuffer()));
 console.log('Render',i+1);
}
await fs.writeFile(out+'/notas_orales.md','# Radiación y electrónica de Voyager\n\nIgnacio Cavicchioli. Fecha de corte: 14/10/2026.\n\n18 diapositivas principales, 18 minutos previstos y 2 de margen. Bibliografía y cuatro respaldos fuera del recorrido. La duración debe comprobarse con ensayo oral.\n\n'+notes.join('\n\n'));
await(await PresentationFile.exportPptx(P)).save(build+'/candidate.pptx');
console.log(await finalizePresentation({workspaceDir:root,candidatePath:build+'/candidate.pptx',finalPath:out+'/Voyager_radiacion_final.pptx',pythonExecutable:'/Users/i.e.cavicchioli/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',integrityValidatorPath:skill+'/container_tools/inspect_presentation_package_integrity.py',layoutValidatorPath:skill+'/container_tools/inspect_presentation_layout_geometry.py',layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit'],explicitTotalSlideCount:23,requiredNativeTableOwnerSlides:[],fontPolicy:{basis:'user_request',families:['Arial']},verifyArtifactToolImport:true,receiptPath:build+'/validacion_final.json'}));
