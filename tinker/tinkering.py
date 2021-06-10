import bpy

bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, location=(0, 0, 0))

for obj in bpy.context.selected_objects:
    obj.name = "theBackground"
    obj.data.name = "theBackground"
    
bpy.ops.object.mode_set(mode='EDIT')

# set the objects interaction mode
bpy.ops.object.mode_set(mode='OBJECT')

#list of vertex numbers to be moved
#vertexList = [1,10,11,12,3]

#for loop that references the list of vertex numbers moved in objext
#for num in vertexList:
    #bpy.data.objects["theBackground"].data.vertices[num].co.z=+10

bpy.data.objects["theBackground"].data.vertices[2].co.yxz=+10
#bpy.data.objects["theBackground"].data.vertices[10].co.z=+10
#bpy.data.objects["theBackground"].data.vertices[11].co.z=+10
#bpy.data.objects["theBackground"].data.vertices[12].co.z=+10
#bpy.data.objects["theBackground"].data.vertices[3].co.z=+10

#
#bpy.ops.object.subdivision_set(level=3, relative=False)

