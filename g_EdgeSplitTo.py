# Generate edge-split patching python from the current scene's mesh modifiers
# (convenient for cycles-prepping extracted areas with merged edges)
# Results are available in 'Split Script' Text object

import bpy

scene = bpy.context.scene
if 'Split Script' in bpy.data.texts:
    text = bpy.data.texts['Split Script']
else:
    text = bpy.data.texts.new('Split Script')

script = '''
import bpy
scene = bpy.context.scene
objs = (
'''
for o in scene.objects:
    if o.type == 'MESH' and 'EdgeSplit' in o.modifiers:
        script += "(scene.objects['%s'], %f),\n" % (o.name, o.modifiers['EdgeSplit'].split_angle)
script += ''')
for o in objs:
    scene.objects.active = o[0]
    bpy.ops.object.modifier_add(type='EDGE_SPLIT')
    o[0].modifiers['EdgeSplit'].split_angle = o[1]
'''
text.from_string(script)
