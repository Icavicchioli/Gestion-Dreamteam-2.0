import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
import {Presentation,PresentationFile} from '@oai/artifact-tool';
const root=process.cwd();
const build=path.join(root,'.build_slides/revisada2');
const out=path.join(root,'versión 2 revisada');
const skill='/Users/i.e.cavicchioli/.codex/plugins/cache/openai-primary-runtime/presentations/26.1013.11914/skills/presentations';
const data=JSON.parse(await fs.readFile(build+'/layout.json','utf8'));
const sources=JSON.parse(await fs.readFile(build+'/fuentes.json','utf8'));
const images=JSON.parse(await fs.readFile(build+'/imagenes.json','utf8'));
const p=Presentation.create({slideSize:{width:1280,height:720}});
for(const d of data){
 const s=p.slides.add();s.background.fill='#FFFFFF';
 for(const op of d.ops){
  if(op.kind==='text'){
   const shape=s.shapes.add({geometry:'textbox',position:{left:op.x,top:op.y,width:op.w,height:op.h},fill:'none',line:{fill:'none',width:0}});
   shape.text=op.text;
   shape.text.style={typeface:'Arial',fontSize:op.size,bold:op.bold,color:op.color,autoFit:'none',wrap:'none'};
   shape.text.insets=0;
  }else if(op.kind==='image'){
   const b=await fs.readFile(out+'/imagenes/'+op.file);
   s.images.add({blob:b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),contentType:op.file.endsWith('.jpg')?'image/jpeg':'image/png',alt:d.visual,fit:'contain',position:{left:op.x,top:op.y,width:op.w,height:op.h}});
  }else if(op.kind==='table'){
   const t=s.tables.add({rows:op.rows.length,columns:op.rows[0].length,left:op.x,top:op.y,width:op.w,height:op.h,columnWidths:op.widths,values:op.rows});
   t.borders.assign({fill:'#D7E2E6',width:0.6,style:'solid'});
   for(let r=0;r<op.rows.length;r++){
    t.rows[r].height=op.h/op.rows.length;
    for(let c=0;c<op.rows[0].length;c++){
     const cell=t.getCell(r,c);cell.fill=r===0?'#172B3A':'#FFFFFF';
     cell.text.style={typeface:'Arial',fontSize:op.size,color:r===0?'#FFFFFF':'#172B3A',bold:r===0,autoFit:'none'};
    }
   }
  }
 }
 const ref=d.refs.map(k=>{const r=sources.find(x=>x.id===k);return `${k}: ${r.titulo}\n${r.url}`}).join('\n\n');
 const asset=images.find(x=>x.name===d.image);
 s.speakerNotes.text=`TIEMPO PREVISTO: ${Math.floor(d.seconds/60)}:${String(d.seconds%60).padStart(2,'0')}\n\nAPOYO ORAL\n${d.oral}\n\nFIGURA Y ALCANCE\n${d.visual}\n${d.caption}\n${asset?asset.credit+'\n'+asset.url:''}\n\nFUENTES Y LOCALIZADORES\n${d.loc}\n\n${ref}`;
 const png=await p.export({slide:s,format:'png',scale:1.5});
 await fs.writeFile(build+'/renders/'+String(d.n).padStart(2,'0')+'.png',new Uint8Array(await png.arrayBuffer()));
 console.log('Render',d.n);
}
await(await PresentationFile.exportPptx(p)).save(build+'/candidate.pptx');
const {finalizePresentation}=await import(pathToFileURL(skill+'/container_tools/artifact_tool_utils.mjs'));
const result=await finalizePresentation({
 workspaceDir:root,candidatePath:build+'/candidate.pptx',finalPath:out+'/03_Presentacion.pptx',
 pythonExecutable:'/Users/i.e.cavicchioli/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',
 integrityValidatorPath:skill+'/container_tools/inspect_presentation_package_integrity.py',
 layoutValidatorPath:skill+'/container_tools/inspect_presentation_layout_geometry.py',
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit',...[4,5,6,10].flatMap(n=>['--require-native-table-slide',String(n)])],
 explicitTotalSlideCount:18,requiredNativeTableOwnerSlides:[4,5,6,10],
 fontPolicy:{basis:'design',families:['Arial']},verifyArtifactToolImport:true,
 receiptPath:build+'/validacion_final.json'
});
console.log(JSON.stringify(result));
