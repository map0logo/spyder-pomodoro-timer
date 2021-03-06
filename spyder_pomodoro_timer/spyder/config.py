# Copyright © Spyder Project Contributors
# Licensed under the terms of the MIT License
# (see spyder/__init__.py for details)

"""Spyder terminal default configuration."""

# --- Constants
# ------ Time limits by default

POMODORO_DEFAULT = 25 * 60 * 1000  # 25 mins in milliseconds

CONF_SECTION = "spyder_pomodoro_timer"

CONF_DEFAULTS = [
    (
        CONF_SECTION,
        {
            "pomodoro_limit": POMODORO_DEFAULT / (60 * 1000),
        },
    ),
    ("shortcuts", {"pomodoro-timer start/pause": "Ctrl+Alt+Shift+P"}),
]

# IMPORTANT NOTES:
# 1. If you want to *change* the default value of a current option, you need to
#    do a MINOR update in config version, e.g. from 1.0.0 to 1.1.0
# 2. If you want to *remove* options that are no longer needed in our codebase,
#    or if you want to *rename* options, then you need to do a MAJOR update in
#    version, e.g. from 1.0.0 to 2.0.0
# 3. You don't need to touch this value if you're just adding a new option
CONF_VERSION = "1.0.0"
