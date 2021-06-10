import bpy

#-----------------------------------------------------------------------
#creat list to store values
#-----------------------------------------------------------------------

point_coordinates = [[-1.5,0,0],[-1,1,0],[1,1,0],[3.5,0,0],[5.5,0,0]]

curveList = []

#-----------------------------------------------------------------------
#creat the curve object
#-----------------------------------------------------------------------

# add new curve to main database
theCurveObject = bpy.data.curves.new('CurveObject', 'CURVE')

theCurveObject.dimensions = '3D'

# add new slpine to the curve
splineObject = theCurveObject.splines.new(type = 'NURBS')

# add a number of points to this spline
splineObject.points.add(len(point_coordinates)-1)

for vert in range(len(point_coordinates)):
    x,y,z = point_coordinates[vert]
    splineObject.points[vert].co = (x,y,z, 1)
    
# make new object with curve
curve_object = bpy.data.objects.new('CurveLine', theCurveObject)

# link curve object to scene collection
bpy.context.scene.collection.objects.link(curve_object)

# make object active
bpy.context.view_layer.objects.active = curve_object

# I want to append any curve I make so I can iterate over them at any time
curveList.append(curve_object)

#iterate throught the CurveList and moves each new curve .05 relative to it's x position
for obj in curveList:
    obj.location.x +=.5