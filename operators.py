from bpy.types import Operator
import bpy

class BPPM_OT_close_gui(Operator):
    """Disable Blender Python Package Manager. 
    A confirmation prompt will appear before disabling the addon."""
    
    bl_label = "Exit" 
    bl_idname = "bppm.closebppm"
    bl_description = __doc__
     
    def draw(self, context):
        scn = context.scene
        
        layout = self.layout
        row = layout.row()
        row.alignment = "CENTER"
        row.label(text="       Click OK to confirm Exit.")
        row = layout.row()
        row.alignment = "CENTER"
        row.label(text="       To re-enable BPPM:")
        row = layout.row()
        row.alignment = "CENTER"
        row.label(text="Go to Edit-> Preferences-> Add-ons -> Search 'Blender PPM' -> Tick Checkbox.")
        
    def execute(self, context):   
        bpy.ops.preferences.addon_disable(module="bppm")  
        return {'FINISHED'}
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=410)