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

# Save Forked File
out_path = os.path.split(bpy.data.filepath)
out_path = os.path.join(out_path[0], 'MREA_2398E906_cycles.blend')
bpy.ops.wm.save_as_mainfile(filepath=out_path)
