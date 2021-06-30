bl_info = {
    "name": "Viewport QuickTheme",
    "author": "Spectral Vectors",
    "version": (0, 3),
    "blender": (2, 90, 0),
    "location": "View 3D",
    "description": "Shortcuts and presets for the Viewport theme",
    "warning": "",
    "doc_url": "",
    "category": "View 3D",
}

import bpy

def setviewport(self, context):
    
    vpqt_vars = bpy.context.scene.vpqt_vars
    view_3d = bpy.context.preferences.themes[0].view_3d

    if vpqt_vars.presets == 'default':
        
        vpqt_vars.line_color = [0.4, 0.4, 0.4, 0.301961]
        vpqt_vars.color1 = [0.224,0.224,0.224]
        vpqt_vars.color2 = (0,0,0)
        vpqt_vars.bgtype = 'SINGLE_COLOR'
                
    if vpqt_vars.presets == 'blackout':
        
        vpqt_vars.line_color = (0.8,0.8,0.8,0.3)
        vpqt_vars.color1 = (0,0,0)
        vpqt_vars.color2 = (0.2,0.2,0.2)
        vpqt_vars.bgtype = 'SINGLE_COLOR'
                
    if vpqt_vars.presets == 'whiteout':
        
        vpqt_vars.line_color = (0,0,0,1)
        vpqt_vars.color1 = (1,1,1)
        vpqt_vars.color2 = (0.2,0.2,0.2)
        vpqt_vars.bgtype = 'SINGLE_COLOR'
                
    if vpqt_vars.presets == 'blueprint':
        
        vpqt_vars.line_color = (0.8,0.8,0.8,0.3)
        vpqt_vars.color1 = (0,0,0.7)
        vpqt_vars.color2 = (0,0,0.2)
        vpqt_vars.bgtype = 'RADIAL'
                
    if vpqt_vars.presets == 'matrix':
        
        vpqt_vars.line_color = [0, 0.8, 0, 0.3]
        vpqt_vars.color1 = [0.02, 0.133, 0]
        vpqt_vars.color2 = [0.004, 0.05, 0]
        vpqt_vars.bgtype = 'RADIAL'
                
    if vpqt_vars.presets == 'hollywood':
        
        vpqt_vars.line_color = [0.672443, 0.608, 0.000000,0.3]
        vpqt_vars.color1 = [0.3, 0.15, 0.000000]
        vpqt_vars.color2 = [0.000000, 0.000000, 0.54480]
        vpqt_vars.bgtype = 'RADIAL'
        
    if vpqt_vars.presets == 'tropicalia':
        
        vpqt_vars.line_color = [0,0,0,0.5]
        vpqt_vars.color1 = [0.5, 0.5, 0.000000]
        vpqt_vars.color2 = [0.000000, 0.2, 0.0]
        vpqt_vars.bgtype = 'RADIAL'
        
    if vpqt_vars.presets == 'sunset':
        
        vpqt_vars.line_color = [0,0,0,0.5]
        vpqt_vars.color1 = [0.5, 0.5, 0.000000]
        vpqt_vars.color2 = [0.2, 0.02, 0.0]
        vpqt_vars.bgtype = 'LINEAR'
        
    if vpqt_vars.presets == 'sunrise':
        
        vpqt_vars.line_color = [0.6,0.6,0.6,0.5]
        vpqt_vars.color1 = [0.2, 0.02, 0.0]
        vpqt_vars.color2 = [0.5, 0.5, 0.000000]
        vpqt_vars.bgtype = 'LINEAR'

    if vpqt_vars.presets == 'petal':
        
        vpqt_vars.line_color = [0.7,0.2,0.7,0.5]
        vpqt_vars.color1 = [0.35, 0.22, 0.36]
        vpqt_vars.color2 = [0.22, 0, 0.325]
        vpqt_vars.bgtype = 'RADIAL'

    if vpqt_vars.presets == 'arctic':
        
        vpqt_vars.line_color = [0.039,0,0.231,0.6]
        vpqt_vars.color1 = [1,1,1]
        vpqt_vars.color2 = [0.255, 0.267, 0.388]
        vpqt_vars.bgtype = 'LINEAR'

    if vpqt_vars.presets == 'nightsky':
        
        vpqt_vars.line_color = [0.678,0.776,1,0.3]
        vpqt_vars.color1 = [0.031,0,0.122]
        vpqt_vars.color2 = [0,0,0]
        vpqt_vars.bgtype = 'RADIAL'

    if vpqt_vars.presets == 'synthwave':
        
        vpqt_vars.line_color = [0,0.204,0.525,0.3]
        vpqt_vars.color1 = [0,0,0]
        vpqt_vars.color2 = [0.161, 0, 0.153]
        vpqt_vars.bgtype = 'RADIAL'

    if vpqt_vars.presets == 'curtaincall':
        
        vpqt_vars.line_color = [0.525,0.463,0,0.3]
        vpqt_vars.color1 = [0.3,0,0.012]
        vpqt_vars.color2 = [0,0,0]
        vpqt_vars.bgtype = 'LINEAR'
    
    line_color = vpqt_vars.line_color
    line_color3 = (line_color[0],line_color[1],line_color[2])
    color1 = vpqt_vars.color1
    color2 = vpqt_vars.color2
    bgtype = vpqt_vars.bgtype    

    view_3d.grid = line_color
    view_3d.wire = line_color3
    view_3d.wire_edit = line_color3
    view_3d.gp_vertex = line_color3

    view_3d.camera = line_color3
    if vpqt_vars.presets == 'default':
        view_3d.camera = (0,0,0)

    view_3d.empty = line_color3

    view_3d.light = line_color
    if vpqt_vars.presets == 'default':
        view_3d.light = [0,0,0,1]

    view_3d.speaker = line_color3
    view_3d.vertex = line_color3
    view_3d.vertex_active = line_color3
    view_3d.vertex_unreferenced = line_color3
    view_3d.handle_free = line_color3
    view_3d.handle_sel_free = line_color3
    view_3d.extra_edge_len = line_color3
    view_3d.camera_path = line_color3
    view_3d.view_overlay = line_color3
    
    view_3d.space.gradients.high_gradient = color1 # Central, Top color
    view_3d.space.gradients.gradient = color2 # Outer, Bottom color
    view_3d.space.gradients.background_type = bgtype # 'RADIAL' 'LINEAR' 'SINGLE_COLOR'
    

class ViewportQuickThemeVariables(bpy.types.PropertyGroup):

    presets : bpy.props.EnumProperty(
        name='Presets',
        items=[
            ('default','Default','Default Blender color theme'),
            ('blackout','Blackout','A black background with white lines'),
            ('whiteout','Whiteout','A white background with black lines'),
            ('blueprint','Blueprint','A blue background with white lines'),
            ('matrix','Matrix','A dark green gradient background with light green lines'),
            ('hollywood','Hollywood','A blue to orange gradient with golden lines'),
            ('tropicalia','Tropicalia','A yellow to green gradient with black lines'),
            ('sunset','Sunset','A yellow to red linear gradient with black lines'),
            ('sunrise','Sunrise','A red to yellow linear gradient with white lines'),
            ('petal','Petal','A mauve to purple gradient with pink lines'),
            ('arctic','Arctic','A white to grey-blue linear gradient with navy lines'),
            ('nightsky','Night Sky','A black to navy blue gradient with white lines'),
            ('synthwave','Synthwave','A black to purple gradient with blue lines'),
            ('curtaincall','Curtain Call','A crimson to black linear gradient with gold lines'),

        ],
        update=setviewport,
    )

    line_color : bpy.props.FloatVectorProperty(
        name="Line Color",
        default=(1,1,1,0.5),
        subtype='COLOR',
        size=4
    )

    color1 : bpy.props.FloatVectorProperty(
        name="BG Color 1",
        default=(0.5,0.5,0.5),
        subtype='COLOR',
        size=3
    )

    color2 : bpy.props.FloatVectorProperty(
        name="BG Color 2",
        default=(0.2,0.2,0.2),
        subtype='COLOR',
        size=3
    )
    
    bgtype : bpy.props.EnumProperty(
        name='BG Type',
        items=[
            ('SINGLE_COLOR','SINGLE_COLOR','A solid color'),
            ('LINEAR','LINEAR','A linear, 2 color gradient'),
            ('RADIAL','RADIAL','A circular, 2 color gradient'),
        ]
    )    


class ViewportQuickThemePanel(bpy.types.Panel):
    """Quick Viewport Theming Shortcuts"""
    bl_label = "Viewport QuickTheme"
    bl_idname = "OBJECT_PT_viewport_quicktheme"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category='QuickTheme'
    
    def draw(self, context):
        layout = self.layout

        layout.prop(bpy.context.scene.vpqt_vars,'presets')
        layout.prop(context.preferences.themes[0].view_3d,"grid", text="Line Color")
        layout.prop(context.preferences.themes[0].view_3d.space.gradients, "high_gradient", text="BG Color 1")
        layout.prop(context.preferences.themes[0].view_3d.space.gradients, "gradient", text="BG Color 2")
        layout.prop(context.preferences.themes[0].view_3d.space.gradients, "background_type", text="BG Type")

def register():
    bpy.utils.register_class(ViewportQuickThemeVariables)
    bpy.utils.register_class(ViewportQuickThemePanel)
    bpy.types.Scene.vpqt_vars = bpy.props.PointerProperty(type=ViewportQuickThemeVariables)

def unregister():
    bpy.utils.unregister_class(ViewportQuickThemePanel)
    bpy.utils.unregister_class(ViewportQuickThemeVariables)