import fs from 'node:fs/promises';
export const C={ink:'#142C40',blue:'#146BA4',muted:'#6C7F8C',light:'#E4EFF6',paper:'#FFFFFF',line:'#B9C8D2'};
export function text(s,t,x,y,w=1100,h=48,size=32,color=C.ink,bold=false,align='left'){
 const a=s.shapes.add({geometry:'textbox',position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
 a.text=t;a.text.style={typeface:'Arial',fontSize:size,color,bold,alignment:align,wrap:'none',autoFit:'none'};a.text.insets=0;return a;
}
export function shape(s,geometry,x,y,w,h,fill='none',stroke=C.ink,width=2){return s.shapes.add({geometry,position:{left:x,top:y,width:w,height:h},fill,line:{fill:stroke,width}});}
export function rect(s,x,y,w,h,fill='none',stroke=C.ink,width=2){return shape(s,'rect',x,y,w,h,fill,stroke,width);}
export function poly(s,pts,color=C.ink,width=3,fill='none',closed=false){
 let minx=Math.min(...pts.map(p=>p[0])),miny=Math.min(...pts.map(p=>p[1])),w=Math.max(...pts.map(p=>p[0]))-minx,h=Math.max(...pts.map(p=>p[1]))-miny;w=Math.max(w,1);h=Math.max(h,1);
 let commands=pts.map((p,i)=>({[i?'lineTo':'moveTo']:{x:p[0]-minx,y:p[1]-miny}}));if(closed)commands.push({close:{}});
 return s.shapes.add({geometry:'custom',position:{left:minx,top:miny,width:w,height:h},fill,line:{fill:color,width},customPaths:[{width:w,height:h,commands}]});
}
export function wire(s,x1,y1,x2,y2,col=C.ink,width=3){return poly(s,[[x1,y1],[x2,y2]],col,width);}
export function arrow(s,x1,y1,x2,y2,col=C.blue,width=3){wire(s,x1,y1,x2,y2,col,width);const a=Math.atan2(y2-y1,x2-x1),l=11;poly(s,[[x2-l*Math.cos(a-.45),y2-l*Math.sin(a-.45)],[x2,y2],[x2-l*Math.cos(a+.45),y2-l*Math.sin(a+.45)]],col,width);}
export function dot(s,x,y,r=5,color=C.ink){shape(s,'ellipse',x-r,y-r,2*r,2*r,color,'none',0);}
export function ground(s,x,y,col=C.ink){wire(s,x,y,x,y+12,col);[24,15,6].forEach((w,i)=>wire(s,x-w,y+12+i*8,x+w,y+12+i*8,col,2));}
export function resistor(s,x,y,len=90,vertical=false,col=C.ink){if(vertical){wire(s,x,y,x,y+20,col);rect(s,x-12,y+20,24,len-40,'none',col);wire(s,x,y+len-20,x,y+len,col);}else{wire(s,x,y,x+20,y,col);rect(s,x+20,y-12,len-40,24,'none',col);wire(s,x+len-20,y,x+len,y,col);}}
export function capacitor(s,x,y,len=90,col=C.ink){wire(s,x,y,x,y+len/2-7,col);wire(s,x-24,y+len/2-7,x+24,y+len/2-7,col);wire(s,x-24,y+len/2+7,x+24,y+len/2+7,col);wire(s,x,y+len/2+7,x,y+len,col);}
export function diode(s,x,y,col=C.ink){wire(s,x,y,x,y+25,col);wire(s,x-20,y+25,x+20,y+25,col);poly(s,[[x-20,y+65],[x+20,y+65],[x,y+25]],col,3,'none',true);wire(s,x,y+65,x,y+90,col);}
export function amp(s,x,y,col=C.ink,cmp=false){poly(s,[[x,y-45],[x,y+45],[x+85,y]],col,3,'none',true);text(s,cmp?'>':'＋',x+12,y-21,60,42,32,col);}
export function coil(s,x,y,len=100,col=C.ink){wire(s,x,y,x,y+10,col);for(let i=0;i<4;i++){s.shapes.add({geometry:'custom',position:{left:x-17,top:y+10+i*20,width:34,height:20},fill:'none',line:{fill:col,width:3},customPaths:[{width:34,height:20,commands:[{moveTo:{x:17,y:0}},{cubicBezTo:{x1:40,y1:0,x2:40,y2:20,x:17,y:20}}]}]});}wire(s,x,y+90,x,y+len,col);}
export function transistor(s,x,y,col=C.ink){wire(s,x,y-32,x,y+32,col);wire(s,x-30,y,x,y,col);wire(s,x,y-18,x+42,y-48,col);wire(s,x+42,y-48,x+42,y-70,col);arrow(s,x,y+18,x+42,y+48,col);wire(s,x+42,y+48,x+42,y+68,col);}
export function charge(s,x,y,sign='+',col=C.blue){shape(s,'ellipse',x-15,y-15,30,30,C.paper,col,2);text(s,sign,x-14,y-19,28,38,32,col,false,'center');}
export async function image(s,root,f,x,y,w,h){let b=await fs.readFile(root+'/'+f);s.images.add({blob:b.buffer.slice(b.byteOffset,b.byteOffset+b.byteLength),contentType:f.endsWith('.jpg')?'image/jpeg':'image/png',alt:f,fit:'contain',position:{left:x,top:y,width:w,height:h}});}
export function trace(s,pts,col=C.blue,width=4){return poly(s,pts,col,width);}
export function axes(s,x,y,w,h){arrow(s,x,y,x+w,y,C.muted,2);arrow(s,x,y,x,y-h,C.muted,2);}
// Shared functional circuit. Bias networks and detailed power connections omitted.
function txtLoad(s,x,y){text(s,'Carga',x-140,y-18,125,45,32,C.ink);}
export function circuit(s,{top=290,highlight='',labels=true,power=true}={}){
 const y=top,active=(id)=>highlight===id?C.blue:C.ink;
 diode(s,100,y,active('sensor'));ground(s,100,y+90,active('sensor'));wire(s,100,y,190,y);resistor(s,190,y,100,false,active('rc'));wire(s,290,y,445,y);dot(s,340,y);capacitor(s,340,y,92,active('rc'));ground(s,340,y+92,active('rc'));
 amp(s,445,y,active('amp'));wire(s,530,y,615,y,active('amp'));amp(s,615,y,active('cmp'),true);wire(s,700,y,785,y,active('cmp'));
 rect(s,785,y-43,125,86,'none',active('state'),3);text(s,'D   Q',801,y-20,100,45,32,active('state'),true);poly(s,[[785,y+12],[797,y+20],[785,y+28]],active('state'),2);wire(s,910,y,965,y,active('state'));resistor(s,965,y,90,false,active('drive'));wire(s,1055,y,1080,y,active('drive'));transistor(s,1110,y,active('drive'));ground(s,1152,y+68,active('drive'));
 if(power){wire(s,1152,y-70,1152,y-100);coil(s,1152,y-200,100,active('drive'));wire(s,1152,y-200,1152,y-225);wire(s,475,y-225,1152,y-225,C.muted,2);wire(s,475,y-225,475,y-45,C.muted,2);wire(s,645,y-225,645,y-45,C.muted,2);wire(s,845,y-225,845,y-43,C.muted,2);text(s,'Alimentación',475,y-275,350,48,32,C.muted);}
 if(!power){resistor(s,1152,y-145,75,true,active('drive'));wire(s,1152,y-145,1152,y-160);txtLoad(s,1152,y-145);}
 if(labels){[['Sensor',60,180],['R / C',260,160],['Amplif.',420,220],['Compar.',625,215],['Registro',790,170],['Mando',1050,180]].forEach(([t,x,w])=>text(s,t,x,y+145,w,50,32,highlight&&['amp','cmp','state','drive'].includes(highlight)?C.ink:C.ink));}
 return {sensor:[100,y],amp:[565,y],state:[850,y],drive:[1152,y]};
}
