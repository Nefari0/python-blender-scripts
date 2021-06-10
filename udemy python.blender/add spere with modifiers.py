import bpy
from math import radians
my_cursor_location = bpy.context.scene.cursor.location

x_cursor = my_cursor_location.x
y_cursor = my_cursor_location.y
z_cursor = my_cursor_location.z

x_rotation = radians(90)

for obj in range(10):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(x_cursor, y_cursor, z_cursor), rotation=(x_rotation, 0.0, 0.0))

    bpy.ops.object.modifier_add(type='SUBSURF')
    bpy.context.object.modifiers["Subdivision"].levels = 2
    bpy.ops.object.shade_smooth()

    x_cursor += 5
    y_cursor += 5
    z_cursor += 5