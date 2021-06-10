import bpy
from math import radians

# location for added objects
my_cursor_location = bpy.context.scene.cursor.location

# object name variables: enter unique names for the objects you want to create
Axle = "axle"    
Hinge = "hinge"
Motor = "motor"
Main = "Cube"

drive_motor = True # choose false if no motor is needed
parent_objects = True # choosing True will parent the Motor and Hinge to the Axle. This allows you to move all the rig objects as one unit

# Motor rotation 
motorRotation = radians(-90)

#adds cube for testing purposes only
#bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(my_cursor_location))
#for obj in bpy.context.selected_objects:
#    obj.name = "Cube"
#    obj.data.name = "Cube"
#bpy.context.object.location[2] = 2


#----------------------------------------------------------------------------------------
#       adds axle
#----------------------------------------------------------------------------------------

# adds cylinder as Axle
bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=1, depth=2, end_fill_type='NGON', calc_uvs=True, enter_editmode=False, align='WORLD', location=(my_cursor_location), rotation=(0, 0, 0))
for obj in bpy.context.selected_objects:
    obj.name = Axle
    obj.data.name = "Axledata"
    
# moves down in z # applies transform. this is noto necessary, but keeps the objects from cluttering together
bpy.context.object.location[2] = -2
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

# gives rigidbody properties
bpy.ops.rigidbody.object_add()
bpy.context.object.rigid_body.type = 'PASSIVE'


#----------------------------------------------------------------------------------------
#       adds hinge
#----------------------------------------------------------------------------------------

# adds empty as Hinge
bpy.ops.object.empty_add(type='ARROWS', location=(my_cursor_location))
for obj in bpy.context.selected_objects:
    obj.name = Hinge

# moves down in z
bpy.context.object.location[2] = -6

# gives rigid body properties
bpy.ops.rigidbody.constraint_add()
bpy.context.object.rigid_body_constraint.type = 'HINGE'
# set first object
bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects[Main]
# set second object
bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects[Axle]


#----------------------------------------------------------------------------------------
#       adds motor
#----------------------------------------------------------------------------------------

# adds empty as Motor
if drive_motor is True:
    bpy.ops.object.empty_add(type='ARROWS', location=(my_cursor_location))
    for obj in bpy.context.selected_objects:
        obj.name = Motor
        
    # moves down in z
    bpy.context.object.location[2] = -10
    # rotates 1.5708rad/90deg
    bpy.context.object.rotation_euler[1] = motorRotation
    # add rigidbody properties/motor
    bpy.ops.rigidbody.constraint_add()
    bpy.context.object.rigid_body_constraint.type = 'MOTOR'
    bpy.context.object.rigid_body_constraint.use_motor_ang = True
    # set first object
    bpy.context.object.rigid_body_constraint.object1 = bpy.data.objects[Main]
    # set second object
    bpy.context.object.rigid_body_constraint.object2 = bpy.data.objects[Axle]


#----------------------------------------------------------------------------------------
#       parents items
#----------------------------------------------------------------------------------------

if parent_objects is True:
    # Selects objects
    bpy.data.objects[Hinge].select_set(True)
    bpy.data.objects[Axle].select_set(True)
    # makes Axle active
    obj = bpy.context.window.scene.objects[Axle]
    bpy.context.view_layer.objects.active = obj
    # parents objects to Axle
    bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)