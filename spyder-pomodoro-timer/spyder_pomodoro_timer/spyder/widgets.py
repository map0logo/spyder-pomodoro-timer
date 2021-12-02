# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Francisco Palm
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Pomodoro Timer Main Widget.
"""

# Third party imports
import qtawesome as qta

# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation

from spyder.api.widgets.status import BaseTimerStatus
from spyder.utils.icon_manager import ima


# Localization
_ = get_translation("spyder_pomodoro_timer.spyder")


# ---- Widgets
# ----------------------------------------------------------------------------


class PomodoroTimerStatus(BaseTimerStatus):
    """Status bar widget to display the pomodoro timer"""

    ID = "pomodoro_timer_status"
    CONF_SECTION = "spyder_pomodoro_timer"

    def __init__(self, parent):
        super().__init__(parent)
        self.value = "25:00"

    def get_tooltip(self):
        """Override api method."""

        return "I am the Pomodoro timer!"

    def get_icon(self):
        return qta.icon("mdi.av-timer", color=ima.MAIN_FG_COLOR)

    # ---- BaseTimerStatus API
    def get_value(self):
        """Get current time of the timer"""

        return self.value
