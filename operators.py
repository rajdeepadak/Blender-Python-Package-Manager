from bpy.types import Operator
import bpy

class BPPM_OT_close_gui(Operator):
    """Disable BlenderpyPM. 
    A confirmation prompt will appear before disabling the addon."""
    
    bl_label = "Exit" 
    bl_idname = "bppm.close_bppm"
    bl_description = __doc__
     
    def draw(self, context):
        scn = context.scene
        
        layout = self.layout
        row = layout.row()
        row.alignment = "CENTER"
        row.label(text="       Click OK to confirm Exit.")
        row = layout.row()
        row.alignment = "CENTER"
        row.label(text="       To re-enable BlenderpyPM:")
        row = layout.row()
        row.alignment = "CENTER"
        row.label(text="Go to Edit-> Preferences-> Add-ons -> Search 'BlenderpyPM' -> Tick Checkbox.")
        
    def execute(self, context):   
        bpy.ops.preferences.addon_disable(module="BlenderpyPM")  
        return {'FINISHED'}
        
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self, width=410)
    

class BPPM_OT_help_user_guide(Operator):
    """Open User Guide"""
    bl_label = "User Guide" 
    bl_idname = "bppm.userguide"
    bl_description = __doc__ 

    def execute(self, context):
        
        return {'FINISHED'}
    
class BPPM_OT_feature_request(Operator):
    """Request a Feature"""
    bl_label = "Feature Request" 
    bl_idname = "bppm.feature_request"
    bl_description = __doc__ 

    def execute(self, context):
        
        return {'FINISHED'}
    
class BPPM_OT_report_bugs(Operator):
    """Report Bugs"""
    bl_label = "Report Bugs" 
    bl_idname = "bppm.report_bugs"
    bl_description = __doc__ 

    def execute(self, context):
        
        return {'FINISHED'}

class BPPM_OT_release_notes(Operator):
    """Read release notes"""
    bl_label = "Read Release Notes" 
    bl_idname = "bppm.release_notes"
    bl_description = __doc__ 

    def execute(self, context):
        
        return {'FINISHED'}