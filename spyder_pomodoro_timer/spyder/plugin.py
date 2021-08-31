# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Francisco Palm
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Pomodoro Timer Plugin.
"""

# Third-party imports
from qtpy.QtGui import QIcon

# Spyder imports
from spyder.api.plugins import Plugins, SpyderPluginV2
from spyder.api.translations import get_translation

# Local imports
from spyder_pomodoro_timer.spyder.confpage import SpyderPomodoroTimerConfigPage
from spyder_pomodoro_timer.spyder.container import SpyderPomodoroTimerContainer

_ = get_translation("spyder_pomodoro_timer.spyder")


class SpyderPomodoroTimer(SpyderPluginV2):
    """
    Spyder Pomodoro Timer plugin.
    """

    NAME = "spyder_pomodoro_timer"
    REQUIRES = []
    OPTIONAL = []
    CONTAINER_CLASS = SpyderPomodoroTimerContainer
    CONF_SECTION = NAME
    CONF_WIDGET_CLASS = SpyderPomodoroTimerConfigPage

    # --- Signals

    # --- SpyderPluginV2 API
    # ------------------------------------------------------------------------
    def get_name(self):
        return _("Spyder Pomodoro Timer")

    def get_description(self):
        return _("A very simple pomodoro timer that shows in the status bar.")

    def get_icon(self):
        return QIcon()

    def register(self):
        container = self.get_container()
        print('SpyderPomodoroTimer registered!')

    def check_compatibility(self):
        valid = True
        message = ""  # Note: Remember to use _("") to localize the string
        return valid, message

    def on_close(self, cancellable=True):
        return True

    # --- Public API
    # ------------------------------------------------------------------------
