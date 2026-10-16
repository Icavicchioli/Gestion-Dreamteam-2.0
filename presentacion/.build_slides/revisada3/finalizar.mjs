import path from 'node:path';
import {pathToFileURL} from 'node:url';
const root=process.cwd();const build=path.join(root,'.build_slides/revisada3');const skill='/Users/i.e.cavicchioli/.codex/plugins/cache/openai-primary-runtime/presentations/26.1013.11914/skills/presentations';
const {finalizePresentation}=await import(pathToFileURL(skill+'/container_tools/artifact_tool_utils.mjs'));
const result=await finalizePresentation({
 workspaceDir:root,candidatePath:build+'/candidate.pptx',finalPath:build+'/export/entrega_verificada.pptx',
 pythonExecutable:'/Users/i.e.cavicchioli/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',
 integrityValidatorPath:skill+'/container_tools/inspect_presentation_package_integrity.py',
 layoutValidatorPath:skill+'/container_tools/inspect_presentation_layout_geometry.py',
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-heading-fit',...[4,6,8,11].flatMap(n=>['--require-native-table-slide',String(n)])],
 explicitTotalSlideCount:18,requiredNativeTableOwnerSlides:[4,6,8,11],
 fontPolicy:{basis:'design',families:['Arial']},verifyArtifactToolImport:true,
 receiptPath:build+'/validacion_revision.json'
});
console.log(JSON.stringify(result));
