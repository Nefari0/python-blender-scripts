import bpy

#---------------------------------------------------------------------------
#   this section adds in the plane
#---------------------------------------------------------------------------

# construct a filled planar mesh with 4 vertices
bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, location=(0, 0, 0))

# for loop will rename selected objects with given name
for obj in bpy.context.selected_objects:
    obj.name = "theBackground"
    obj.data.name = "theBackground"

# sets specified object interaction mode    
bpy.ops.object.mode_set(mode='EDIT')

# subdevide selected mesh
bpy.ops.mesh.subdivide(number_cuts=3, quadcorner='INNERVERT')

# set the objects interaction mode
bpy.ops.object.mode_set(mode='OBJECT')

# creates a list of vertex numbers to be moved
vertexList = [1,10,11,12,3]

# for loop that references the list of vertex numbers moved in objext
for num in vertexList:
    bpy.data.objects["theBackground"].data.vertices[num].co.z=+8

# set a devision surface level of 2 on mesh
bpy.ops.object.subdivision_set(level=2, relative=False)

# render and display shaded faces smooth
bpy.ops.object.shade_smooth

#---------------------------------------------------------------------------
#   this section adds camera
#---------------------------------------------------------------------------

bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(-10.7447, 0.163963, 4.48385), rotation=(1.44513, 0.0, 4.69843))

#---------------------------------------------------------------------------
#   this section adds monkey
#---------------------------------------------------------------------------

bpy.ops.mesh.primitive_monkey_add(size=2.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0.0, 0.0, 2.96913), rotation=(0.0, 0.0, 4.71239))

# set a devision surface level of 2 on mesh
bpy.ops.object.subdivision_set(level=2, relative=False)

# render and display shaded faces smooth
bpy.ops.object.shade_smooth

#---------------------------------------------------------------------------
#   this section adds light
#---------------------------------------------------------------------------

bpy.ops.object.light_add(type='AREA', radius=1.0, align='WORLD', location=(-4.14292, 0.0, 6.99893), rotation=(0.0, -0.216462, 0.0))
bpy.context.object.data.energy = 200

# for loop will rename selected objects with given name
for obj in bpy.context.selected_objects:
    obj.name = "keyLight"
    obj.data.name = "Keylight"