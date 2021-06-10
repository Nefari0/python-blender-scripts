import bpy

#------------------------------------------------
#       this adds and manipulates circle
#------------------------------------------------

# add circle
bpy.ops.mesh.primitive_circle_add(vertices=32, radius=1, fill_type='NOTHING', calc_uvs=True, enter_editmode=False, align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0))

# for loop will rename selected objects with given name
for obj in bpy.context.selected_objects:
    obj.name = "circ"
    obj.data.name = "circ"
    
#bpy.data.objects["circ"].data.vertices[6].co.y=+8

#------------------------------------------------
#     this helps determine vert location
#------------------------------------------------

# creates a list of vertex numbers to be moved
#vertexList = [1,0,31]

# for loop that references the list of vertex numbers moved in objext
#for num in vertexList:
#   bpy.data.objects["circ"].data.vertices[num].co.y=+8


