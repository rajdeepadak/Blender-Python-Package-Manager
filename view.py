from bpy.types import Panel
import bpy
from operators import BPPM_OT_close_gui

class MainPanel(Panel):
    bl_idname = "BPPM_PT_main_panel"
    bl_label = ""
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "BlenderpyPM"
    
    def draw_header(self, context):
        layout =self.layout
        logo_img = main_logo["main"]
        logo_icon = logo_img["logo_icon"]
        
        row1 = layout.row()
        row1.enabled = not context.scene.dev_mode    
        row1.prop(context.scene, "steps", expand=True, emboss = True)
        
        row = layout.row()
            
        layout.menu(header_menus.HR_MT_meshing.bl_idname, text="Help")
        layout.menu(header_menus.HR_MT_dev.bl_idname, text="Dev")
        layout.menu(header_menus.HR_MT_aboutus.bl_idname, text="About Us")
        
        layout.operator(BPPM_OT_settings.bl_idname, text="", icon="PREFERENCES")
        layout.alert = True
        layout.operator(BPPM_OT_close_gui.bl_idname, text="", icon="PANEL_CLOSE")
        layout.alert = False
        
    def draw(self, context):
        layout = self.layout
        
        