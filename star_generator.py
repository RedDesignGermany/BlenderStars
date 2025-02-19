bl_info = {
    "name": "Star Generator",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import random

def create_star(location):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=random.uniform(0.1, 0.3), location=location)
    star = bpy.context.object
    star.name = "Star"
    mat = bpy.data.materials.new(name="StarMaterial")
    mat.diffuse_color = (1, 1, 1, 1)
    star.data.materials.append(mat)

class OBJECT_OT_generate_stars(bpy.types.Operator):
    """Generate Stars"""
    bl_idname = "object.generate_stars"
    bl_label = "Generate Stars"
    bl_options = {'REGISTER', 'UNDO'}

    star_count: bpy.props.IntProperty(name="Star Count", default=100, min=1, max=1000)
    x_range: bpy.props.FloatProperty(name="X Range", default=10.0)
    y_range: bpy.props.FloatProperty(name="Y Range", default=10.0)
    z_range: bpy.props.FloatProperty(name="Z Range", default=10.0)

    def execute(self, context):
        for _ in range(self.star_count):
            location = (
                random.uniform(-self.x_range, self.x_range),
                random.uniform(-self.y_range, self.y_range),
                random.uniform(-self.z_range, self.z_range)
            )
            create_star(location)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(OBJECT_OT_generate_stars.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_generate_stars)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_generate_stars)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()
