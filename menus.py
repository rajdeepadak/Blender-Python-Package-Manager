from operators import BPPM_OT_help_user_guide
from operators import BPPM_OT_feature_request
from operators import BPPM_OT_report_bugs
from operators import BPPM_OT_release_notes

class BPPM_MT_aboutus(Menu):
    """Learn about us"""
    bl_idname = "BPPM_MT_aboutus"
    bl_label = ""
    bl_description = __doc__
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text="About Us Section")
        
class BPPM_MT_help(Menu):
    """View Help Options"""
    bl_idname = "BPPM_MT_help"
    bl_label = ""
    bl_description = __doc__
    
    def draw(self, context):
        layout = self.layout

        layout.operator(BPPM_OT_help_user_guide.bl_idname, text = "User Guide", icon="USER")
        layout.separator()
        layout.operator(BPPM_OT_feature_request.bl_idname, text = "Feature Request", icon = "FILE_CACHE")
        layout.operator(BPPM_OT_report_bugs.bl_idname, text = "Report Bugs", icon="GHOST_DISABLED")
        layout.separator()
        layout.operator(BPPM_OT_release_notes.bl_idname, text = "Release Notes", icon="help_menu")