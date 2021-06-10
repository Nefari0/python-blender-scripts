import bpy

object_list = "Cyl","Cub"

bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(8.7426, 6.58306, -0.746959))
for obj in bpy.context.selected_objects:
    obj.name = object_list[1]
    obj.data.name = object_list[1]

bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=2, enter_editmode=False, location=(5.26588, 1.33245, -7.28225))
for obj in bpy.context.selected_objects:
    obj.name = object_list[0]
    obj.data.name = object_list[0]

print(object_list)

bpy.data.objects[object_list[1]].select_set(True)
#bpy.ops.object.select_all(action='SELECT')


#bpy.ops.object.parent_set(type='OBJECT', xmirror=False, keep_transform=False)

#bpy.ops.outliner.item_activate[cub](extend=False, deselect_all=True)
