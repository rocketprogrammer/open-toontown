if __debug__:
    from panda3d.core import loadPrcFile
    loadPrcFile("etc/Configrc.prc")
else:
    import sys
    sys.path = [""]


from panda3d.core import loadPrcFileData
from distutils.util import strtobool
import os

if strtobool(os.getenv("USE_LIVE_SERVER")):
    # Production environment
    loadPrcFileData("Override Client Config",
                    "game-server unite.sunrise.games:6667")

from toontown.launcher.QuickLauncher import QuickLauncher
launcher = QuickLauncher()
launcher.notify.info("Reached end of StartQuickLauncher.py.")
