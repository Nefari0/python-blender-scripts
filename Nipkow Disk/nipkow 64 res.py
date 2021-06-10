import bpy

# iterates location and rotation of apertures
yPlacement = 15
zRotation = 0

bpy.context.scene.cursor.location[0] = 0
bpy.context.scene.cursor.location[1] = 0
bpy.context.scene.cursor.location[2] = 0

# adds apertures to scene
for circles in range(64):
    bpy.ops.mesh.primitive_cylinder_add(radius=.25, depth=10, enter_editmode=False, location=(0, yPlacement, 0))
    # set object origin to world origin
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    # iterate rotation increment
    bpy.context.object.rotation_euler[2] = zRotation
    # names and joins apertures into same object
    for obj in bpy.context.selected_objects:
        obj.name = "Cyl"
        obj.data.name = "Cyl"
        bpy.ops.object.select_by_type(extend=False, type='MESH')
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')


    zRotation = zRotation + 0.098175
    yPlacement = yPlacement + .5
    
# creates cylindrical disk
bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=50.0, depth=5.0, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 0.0), rotation=(0.0, 0.0, 0.0))

# adds boolean modifier # sets to difference."Cyl"
bpy.ops.object.modifier_add(type='BOOLEAN')

bpy.data.objects["Cylinder"].modifiers["Boolean"].object

bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cyl"]

# applies boolean modifier
bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Boolean")

# selects and deletes apertures
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects["Cyl"].select_set(True)
bpy.ops.object.delete(use_global=False, confirm=True)
