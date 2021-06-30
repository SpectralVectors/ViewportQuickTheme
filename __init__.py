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
from .ViewportQuickTheme import (
    ViewportQuickThemePanel,
    ViewportQuickThemeVariables,

    )

classes = (
    ViewportQuickThemePanel,
    ViewportQuickThemeVariables,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)

    bpy.types.Scene.vpqt_vars = bpy.props.PointerProperty(type=ViewportQuickThemeVariables)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__package__":
    register()