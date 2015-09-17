# Cycles Fork
# MREA_2398E906 (MP1 / Artifact Temple)
#
# Performs destructive scene modification (removing coplanar geometry)
# saving the results to a separate .blend 

import bpy
import bmesh
import os.path
scene = bpy.context.scene

# Outward Window
outward_window = bmesh.new()
outward_window.from_mesh(scene.objects['MREA_2398E906_005'].data)
outward_window.faces.ensure_lookup_table()

to_remove = set()
for face in outward_window.faces:
    if face.material_index == 1:
        to_remove.add(face)

for face in to_remove:
    outward_window.faces.remove(face)
    
outward_window.to_mesh(scene.objects['MREA_2398E906_005'].data)
scene.objects['MREA_2398E906_005'].data.update()

# Inward Window
inward_window = bmesh.new()
inward_window.from_mesh(scene.objects['MREA_2398E906_045'].data)
inward_window.faces.ensure_lookup_table()

to_remove = set()
for face in inward_window.faces:
    if face.material_index == 0:
        to_remove.add(face)

for face in to_remove:
    inward_window.faces.remove(face)
    
inward_window.to_mesh(scene.objects['MREA_2398E906_045'].data)
scene.objects['MREA_2398E906_045'].data.update()

# Remove non-rendered lights
bpy.data.objects['LAMP_0_016'].hide_render = True
bpy.data.objects['LAMP_0_017'].hide_render = True
bpy.data.objects['LAMP_0_018'].hide_render = True
bpy.data.objects['LAMP_0_019'].hide_render = True
bpy.data.objects['LAMP_0_020'].hide_render = True
bpy.data.objects['LAMP_0_021'].hide_render = True
bpy.data.objects['LAMP_0_022'].hide_render = True
bpy.data.objects['LAMP_0_023'].hide_render = True
bpy.data.objects['LAMP_0_024'].hide_render = True
bpy.data.objects['LAMP_0_025'].hide_render = True

# Edge split modifiers
objs = (
(scene.objects['MREA_2398E906_136'], 0.523599),
(scene.objects['MREA_2398E906_135'], 0.523599),
(scene.objects['MREA_2398E906_134'], 0.523599),
(scene.objects['MREA_2398E906_133'], 0.523599),
(scene.objects['MREA_2398E906_132'], 0.523599),
(scene.objects['MREA_2398E906_131'], 0.532674),
(scene.objects['MREA_2398E906_130'], 0.674046),
(scene.objects['MREA_2398E906_129'], 0.523599),
(scene.objects['MREA_2398E906_128'], 0.523599),
(scene.objects['MREA_2398E906_127'], 0.523599),
(scene.objects['MREA_2398E906_126'], 0.523599),
(scene.objects['MREA_2398E906_125'], 0.523599),
(scene.objects['MREA_2398E906_124'], 0.523599),
(scene.objects['MREA_2398E906_123'], 0.569676),
(scene.objects['MREA_2398E906_122'], 0.568279),
(scene.objects['MREA_2398E906_118'], 0.629017),
(scene.objects['MREA_2398E906_117'], 0.523599),
(scene.objects['MREA_2398E906_116'], 0.523599),
(scene.objects['MREA_2398E906_115'], 0.523599),
(scene.objects['MREA_2398E906_114'], 0.523599),
(scene.objects['MREA_2398E906_085'], 0.577355),
(scene.objects['MREA_2398E906_084'], 0.770214),
(scene.objects['MREA_2398E906_083'], 0.796394),
(scene.objects['MREA_2398E906_082'], 0.523599),
(scene.objects['MREA_2398E906_081'], 0.816640),
(scene.objects['MREA_2398E906_080'], 0.859400),
(scene.objects['MREA_2398E906_079'], 0.812800),
(scene.objects['MREA_2398E906_078'], 0.814894),
(scene.objects['MREA_2398E906_077'], 0.837758),
(scene.objects['MREA_2398E906_064'], 0.523599),
(scene.objects['MREA_2398E906_063'], 0.798488),
(scene.objects['MREA_2398E906_062'], 0.291121),
(scene.objects['MREA_2398E906_060'], 0.523599),
(scene.objects['MREA_2398E906_037'], 0.646470),
(scene.objects['MREA_2398E906_013'], 0.523599),
(scene.objects['MREA_2398E906_009'], 0.558505),
(scene.objects['MREA_2398E906_008'], 0.558505),
(scene.objects['MREA_2398E906_004'], 0.523599),
(scene.objects['MREA_2398E906_001'], 0.648041),
(scene.objects['MREA_2398E906_000'], 0.523599),
)
for o in objs:
    scene.objects.active = o[0]
    bpy.ops.object.modifier_add(type='EDGE_SPLIT')
    o[0].modifiers['EdgeSplit'].split_angle = o[1]

# Save Forked File
out_path = os.path.split(bpy.data.filepath)
out_path = os.path.join(out_path[0], 'MREA_2398E906_cycles.blend')
bpy.ops.wm.save_as_mainfile(filepath=out_path)
