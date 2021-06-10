import bpy
from math import radians
my_cursor_location = bpy.context.scene.cursor.location


#------------------------------------------------------------------------
#       adds and modifies circle
#------------------------------------------------------------------------

# For loop adds x number of circles

xyradius = 1
Ytranslate = 2
zrotation = 0

for circles in range(10):
    bpy.ops.mesh.primitive_circle_add(vertices=32, radius=xyradius, fill_type='NOTHING', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0, 0, 0), rotation=(0.0, 0.0, 0.0))
    
    # For loop names cirlces
    for obj in bpy.context.selected_objects:
        obj.name = "circ"
        obj.data.name = "circ"
        
    # moves vertice in Y relative to radius
    bpy.data.objects["circ"].data.vertices[0].co.y=+Ytranslate
    
    #rotates each object
    bpy.context.object.rotation_euler[2] = zrotation
    
    zrotation = zrotation + 0.523599
    Ytranslate = Ytranslate + 1
    xyradius = xyradius + 1
    