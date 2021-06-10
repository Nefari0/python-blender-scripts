import bpy

# adds plane as platform
bpy.ops.mesh.primitive_plane_add(size=144, calc_uvs=True, enter_editmode=False, align='WORLD', location=(0, 0, 0), rotation=(0, 0, 0))

# for loop will rename selected objects with given name
for obj in bpy.context.selected_objects:
    obj.name = "buildplatform"
    obj.data.name = "buildplatform"

# adjust size to x = 140
verts = [1,3]
for num in verts:
    bpy.data.objects["buildplatform"].data.vertices[num].co.x=68

# recenters geometry to origin    
bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')

# makes thickness .25 
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].thickness = 0.25

# moves platform up for brim possitioning
bpy.context.object.location[2] = 0.1
