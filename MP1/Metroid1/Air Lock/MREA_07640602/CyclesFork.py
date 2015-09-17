# Cycles Fork
# MREA_07640602 (MP1 / Air Lock)
#
# Adds edge-split modifers for cycles rendering

import bpy
import os.path
scene = bpy.context.scene

objs = (
(scene.objects['MREA_07640602_078'], 0.523599),
(scene.objects['MREA_07640602_077'], 0.523599),
(scene.objects['MREA_07640602_060'], 0.523599),
(scene.objects['MREA_07640602_059'], 0.476824),
(scene.objects['MREA_07640602_058'], 0.523599),
(scene.objects['MREA_07640602_055'], 0.523599),
(scene.objects['MREA_07640602_019'], 0.523599),
(scene.objects['MREA_07640602_018'], 0.455531),
(scene.objects['MREA_07640602_017'], 0.523599),
(scene.objects['MREA_07640602_016'], 0.523599),
(scene.objects['MREA_07640602_014'], 0.523599),
(scene.objects['MREA_07640602_011'], 0.284838),
(scene.objects['MREA_07640602_009'], 0.523599),
(scene.objects['MREA_07640602_008'], 0.446630),
(scene.objects['MREA_07640602_007'], 0.523599),
(scene.objects['MREA_07640602_006'], 0.523599),
(scene.objects['MREA_07640602_005'], 0.523599),
(scene.objects['MREA_07640602_003'], 0.434238),
(scene.objects['MREA_07640602_001'], 0.523599),
)
for o in objs:
    scene.objects.active = o[0]
    bpy.ops.object.modifier_add(type='EDGE_SPLIT')
    o[0].modifiers['EdgeSplit'].split_angle = o[1]

# Save Forked File
out_path = os.path.split(bpy.data.filepath)
out_path = os.path.join(out_path[0], 'MREA_07640602_cycles.blend')
bpy.ops.wm.save_as_mainfile(filepath=out_path)
