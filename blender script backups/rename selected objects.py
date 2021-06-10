import bpy

for obj in bpy.context.selected_objects:
    obj.name = "GEO_sphere"
    obj.data.name = "GEO_sphere"