#!/bin/sh
cd ..

export LOGIN_TOKEN=dev
export USE_LIVE_SERVER=false

python3 -m toontown.launcher.QuickStartLauncher
