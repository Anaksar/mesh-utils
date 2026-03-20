import bpy

class Overlap(bpy.types.Panel):
    '''Панель с операторами пересечений'''
    bl_label = 'Overlap'
    bl_idname = 'OBJECT_PT_mesh_utils'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mesh-Utils'

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.operator('mesh.select_overlapping')
        col.operator('mesh.delaunay_triangulation')
        col.operator('mesh.mesh_from_uv')
        col.operator('mesh.select_interior_faces_bake')

        col = layout.column(align = True)
        col.operator('mesh.select_all_by_trait', text="Bevel").select_type = 'BEVEL'
        col.operator('mesh.select_all_by_trait', text="Crease").select_type = 'CREASE'
        col.operator('mesh.select_all_by_trait', text="Seam").select_type = 'SEAM'
        col.operator('mesh.select_all_by_trait', text="Sharp").select_type = 'SHARP'
        col.operator('mesh.select_all_by_trait', text="Freestyle").select_type = 'FREESTYLE'
       
        
