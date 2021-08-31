# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Francisco Palm
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Pomodoro Timer Main Container.
"""
# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation
from spyder.api.widgets.main_container import PluginMainContainer


# Local imports
from spyder_pomodoro_timer.spyder.widgets import PomodoroTimerStatus

_ = get_translation("spyder_pomodoro_timer.spyder")


class SpyderPomodoroTimerContainer(PluginMainContainer):

    # Signals

    # --- PluginMainContainer API
    # ------------------------------------------------------------------------
    def setup(self):
        # Widgets
        self.pomodoro_timer_status = PomodoroTimerStatus(self)

    def update_actions(self):
        pass

    # --- Public API
    # ------------------------------------------------------------------------
