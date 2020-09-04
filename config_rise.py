#!/usr/bin/env python3
from traitlets.config.manager import BaseJSONConfigManager
from pathlib import Path

path = Path.home() / ".jupyter" / "nbconfig"
cm = BaseJSONConfigManager(config_dir=str(path))
cm.update(
    "rise",
    {
        "theme": None,
        "transition": None,
        "start_slideshow_at": "selected",
        "leap_motion": {
            "naturalSwipe"  : True,     # Invert swipe gestures
            "pointerOpacity": 0.5,      # Set pointer opacity to 0.5
            "pointerColor"  : "#d80000" # Red pointer"nat.png"
        },
        "header": "<h3>Francisco Perez-Sorrosal</h3>",
        "footer": "<h3>Deep Learning Reading Group</h3>",
        "scroll": True,
        "enable_chalkboard": True
     }
)

print("RISE config updated!!!")