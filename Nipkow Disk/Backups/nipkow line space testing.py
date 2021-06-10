import bpy

radius = 25

for circles in range(32):
    bpy.ops.mesh.primitive_circle_add(radius=radius, enter_editmode=False, location=(0, 0, 0))
    
    radius = radius + 1
