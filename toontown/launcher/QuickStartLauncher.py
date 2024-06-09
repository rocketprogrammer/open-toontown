if __debug__:
    from panda3d.core import loadPrcFile
    loadPrcFile("etc/Configrc.prc")
else:
    import sys
    sys.path = [""]


from panda3d.core import loadPrcFileData
import json
import os

if json.loads(os.getenv("USE_LIVE_SERVER").lower()):
    # Production environment
    loadPrcFileData("Override Client Config",
                    "game-server unite.sunrise.games:6667")

from toontown.launcher.QuickLauncher import QuickLauncher
launcher = QuickLauncher()
launcher.notify.info("Reached end of StartQuickLauncher.py.")
