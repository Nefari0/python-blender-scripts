import bpy
import math

# center curser
for i in range(0,3):
    bpy.context.scene.cursor.location[i] = 0

# aperture variables 
#aperture_Radius = 0.5
yplacement = 65
zorbit = 0
zplacement = -16.5

# scanner variables
scan_radius = 65
scan_depth = 100
scan_Zlocale = 0.0

# renaming function: renames selected objects
object_name = [object_name] #rename variable stores new name data
def rename_obj():
    for obj in bpy.context.selected_objects:
        obj.name = object_name
        obj.data.name = object_name
        object_name = tuple()

#------------------------------------------------------------------------------------
# add cylindrical apertures and positioning transformations 
#------------------------------------------------------------------------------------


for aper in range(32):
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=.5, depth=10.0, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, yplacement, zplacement ), rotation=(math.radians(90), 0.0, 0.0))
    # set object origin to world origin
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
    # iterate rotation increment
    bpy.context.object.rotation_euler[2] = zorbit
#    # names and joins apertures into same object
    for obj in bpy.context.selected_objects:
        obj.name = "apr"
        obj.data.name = "apr"
        bpy.ops.object.select_by_type(extend=False, type='MESH')
        bpy.ops.object.join()
        bpy.ops.object.select_all(action='DESELECT')

    zorbit  = zorbit + 0.19635
    zplacement = zplacement + 1
#------------------------------------------------------------------------------------
# add external cylindrical scanner
#------------------------------------------------------------------------------------

bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=scan_radius, depth=scan_depth, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, scan_Zlocale ), rotation=(0.0, 0.0, 0.0))
object_name = "scanner"
rename_obj()


#------------------------------------------------------------------------------------
# add smaller cylinder use boolean to hollow out scanner
#------------------------------------------------------------------------------------

bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=scan_radius - 1.5, depth=scan_depth - 2.9, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, scan_Zlocale ), rotation=(0.0, 0.0, 0.0))

bpy.data.objects[scanner].select_set(True)

# remove unnecessary geometry from scanner
# use boolean modifier to add apertures to scanner