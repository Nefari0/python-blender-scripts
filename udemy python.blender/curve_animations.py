import bpy


#-----------------------------------------------------------------------
#       create list to store values
#-----------------------------------------------------------------------

coords_list = [[12,2,5],[9,6,4],[8,1,3],[0,4,2],[-7,-16,1]]

curveList = []

color_list_1 = [0.8, 0.0, 0.004, 1.0]
color_list_2 = [0.004, 0.0, 0.8, 1.0]
color_list_3 = [0.076, 0.883, 0.906, 1.0]
color_list_4 = [0.017, 0.8, 0.0, 1.0]

cam_location_list = [[12,2,5],[11,2,4],[8,0,3],[0.7,6,2],[-7,-16,1]]

cam_rotation_list = [[1.570800, 0, -0.561918], [1.570800, 0, -0.450954], [1.570800, 0, 0.481517], [1.434536, 0.086752,  0.829282], [1.293639, 0.085921, 0.676657]]

#-----------------------------------------------------------------------
#       create the curve object
#-----------------------------------------------------------------------

# for loop creates 4 of these curves
for eachObj in range(0, 4):
    
    # add new curve to main database
    theCurveObject = bpy.data.curves.new('CurveObject', 'CURVE')

    theCurveObject.dimensions = '3D'

    # adds new spline to the curve
    splineObject = theCurveObject.splines.new(type="NURBS")

    # add a number of points to this spline # Step back as there is one by default
    splineObject.points.add(len(coords_list)-1)

    for vert in range(len(coords_list)):
        x,y,z = coords_list[vert]
        splineObject.points[vert].co = (x,y,z, 1)
        
    # make new object with curve
    curve_obj = bpy.data.objects.new('curve_line', theCurveObject)

    # link curve object to scene collection
    bpy.context.scene.collection.objects.link(curve_obj)

    # makes it active
    bpy.context.view_layer.objects.active = curve_obj

    # append any curve created so it can be iterated over
    curveList.append(curve_obj)

    # iterates through the curveList and moves each new curve .05 relative to it's x position
    for obj in curveList:
        obj.location.x +=.05

        
    bpy.context.object.data.bevel_depth = 0.02

    # set the timeline to 1
    bpy.context.scene.frame_set(1)

    # set factor to 1
    bpy.context.object.data.bevel_factor_start = 1

    # access the object data of active object and place a keyframe at it's bevel start value
    bpy.context.object.data.keyframe_insert(data_path='bevel_factor_start')

    # set timeline to 1
    bpy.context.scene.frame_set(50)

    # set factor to 0
    bpy.context.object.data.bevel_factor_start = 0

    # access the object data of active object and place a keyframe at it's bevel start value
    bpy.context.object.data.keyframe_insert(data_path='bevel_factor_start')

    # sets the frame range on the timeline
    bpy.context.scene.frame_end = 50
    
    
#-----------------------------------------------------------------------
#       create material for the curves
#-----------------------------------------------------------------------

curveMaterial = bpy.data.materials.get("M_curve_line")
if curveMaterial is None:
    #create a new variable and assign it to the new material
    curveMaterial = bpy.data.materials.new(name="M_curve_line")
    
# set the use nodes arguement to true
curveMaterial.use_nodes = True

# for loop to check for any nodes and delete them
curveNodes = curveMaterial.node_tree.nodes
for node in curveNodes:
    curveNodes.remove(node)
    
# adds back a material output node
mat_output = curveNodes.new(type="ShaderNodeOutputMaterial")

# create a new variable and assign it too the newmaterail node
emissionType = curveMaterial.node_tree.nodes.new('ShaderNodeEmission')

# sets color of the new material
emissionType.inputs[0].default_value = color_list_4

# sets emission strength to a specified value
emissionType.inputs[1].default_value = 20

# link emission shader to the material
curveMaterial.node_tree.links.new(mat_output.inputs[0], emissionType.outputs[0])

#create a variable and assign it to a copy of the curve material
mat_01 = curveMaterial.copy()
mat_01.name = "M_curve_line.001"
emissionType.inputs[0].default_value = (color_list_1)
bpy.data.objects["curve_line.001"].active_material = mat_01

mat_02 = curveMaterial.copy()
mat_02.name = "M_curve_line.002"
emissionType.inputs[0].default_value = (color_list_2)
bpy.data.objects["curve_line.002"].active_material = mat_02

mat_03 = curveMaterial.copy()
mat_03.name = "M_curve_line.003"
emissionType.inputs[0].default_value = (color_list_3)
bpy.data.objects["curve_line.003"].active_material = mat_03

mat_04 = curveMaterial.copy()
mat_04.name = "M_curve_line"
emissionType.inputs[0].default_value = (color_list_4)
bpy.data.objects["curve_line"].active_material = mat_04

# changes backround color
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0, 0, 0, 1)

#-----------------------------------------------------------------------
#       adding a camera to the scene
#-----------------------------------------------------------------------

bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(0, 0, 0))

camObj = bpy.context.object

# sets the location of the cam from the list
camObj.location = cam_location_list[4]
camObj.rotation_euler = cam_rotation_list[0]
# set keyframe for location at frame 1
camObj.keyframe_insert(data_path="location", frame=1)
# set keyframe for rotation at frame 1
camObj.keyframe_insert(data_path="rotation_euler", frame=1)

# sets the location of the cam from the list
camObj.location = cam_location_list[3]
camObj.rotation_euler = cam_rotation_list[1]
# set keyframe for location at frame 15
camObj.keyframe_insert(data_path="location", frame=15)
# set keyframe for rotation at frame 15
camObj.keyframe_insert(data_path="rotation_euler", frame=15)

# sets the location of the cam from the list
camObj.location = cam_location_list[2]
camObj.rotation_euler = cam_rotation_list[2]
# set keyframe for location at frame 25
camObj.keyframe_insert(data_path="location", frame=25)
# set keyframe for rotation at frame 25
camObj.keyframe_insert(data_path="rotation_euler", frame=25)

# sets the location of the cam from the list
camObj.location = cam_location_list[1]
camObj.rotation_euler = cam_rotation_list[3]
# set keyframe for location at frame 37
camObj.keyframe_insert(data_path="location", frame=37)
# set keyframe for rotation at frame 37
camObj.keyframe_insert(data_path="rotation_euler", frame=37)

# sets the location of the cam from the list
camObj.location = cam_location_list[0]
camObj.rotation_euler = cam_rotation_list[4]
# set keyframe for location at frame 50
camObj.keyframe_insert(data_path="location", frame=50)
# set keyframe for rotation at frame 50
camObj.keyframe_insert(data_path="rotation_euler", frame=50)