# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Francisco Palm
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Pomodoro Timer Main Container.
"""

# Third party imports
import qtawesome as qta
from qtpy.QtWidgets import QToolButton

# Spyder imports
from spyder.api.config.decorators import on_conf_change
from spyder.api.translations import get_translation
from spyder.api.widgets.main_container import PluginMainContainer
from spyder.utils.icon_manager import ima

# Local imports
from spyder_pomodoro_timer.spyder.widgets import (
    PomodoroTimerStatus,
    PomodoroTimerToolbar,
    INTERVAL
)
from spyder_pomodoro_timer.spyder.api import (
    PomodoroToolbarActions,
    PomodoroToolbarSections,
    PomodoroMenuSections,
)

_ = get_translation("spyder_pomodoro_timer.spyder")


class SpyderPomodoroTimerContainer(PluginMainContainer):

    # Signals

    # --- PluginMainContainer API
    # ------------------------------------------------------------------------
    def setup(self):
        # Widgets
        self.pomodoro_timer_status = PomodoroTimerStatus(self)
        title = _("Pomodoro Timer Toolbar")
        self.pomodoro_timer_toolbar = PomodoroTimerToolbar(self, title)

        # Actions
        start_timer_action = self.create_action(
            PomodoroToolbarActions.Start,
            text=_("Start"),
            tip=_("Start timer"),
            icon=qta.icon("fa.play-circle", color=ima.MAIN_FG_COLOR),
            triggered=self.start_pomodoro_timer,
        )

        pause_timer_action = self.create_action(
            PomodoroToolbarActions.Pause,
            text=_("Pause"),
            tip=_("Pause timer"),
            icon=qta.icon("fa.pause-circle", color=ima.MAIN_FG_COLOR),
            triggered=self.pause_pomodoro_timer,
        )

        stop_timer_action = self.create_action(
            PomodoroToolbarActions.Stop,
            text=_("Stop"),
            tip=_("Stop timer"),
            icon=qta.icon("fa.stop-circle", color=ima.MAIN_FG_COLOR),
            triggered=self.stop_pomodoro_timer,
        )

        self.pomodoro_menu = self.create_menu(
            "pomodoro_timer_menu",
            text=_("Pomodoro timer"),
            icon=qta.icon("mdi.av-timer", color=ima.MAIN_FG_COLOR),
        )

        # Add actions to the menu
        for action in [start_timer_action, pause_timer_action, stop_timer_action]:
            self.add_item_to_menu(
                action,
                self.pomodoro_menu,
                section=PomodoroMenuSections.Main,
            )

        self.pomodoro_button = self.create_toolbutton(
            "pomodoro_timer_button",
            text=_("Pomodoro timer"),
            icon=qta.icon("mdi.av-timer", color=ima.MAIN_FG_COLOR),
        )

        self.pomodoro_button.setMenu(self.pomodoro_menu)
        self.pomodoro_button.setPopupMode(QToolButton.InstantPopup)

        # Add menu to toolbar
        self.add_item_to_toolbar(
            self.pomodoro_button,
            self.pomodoro_timer_toolbar,
            section=PomodoroToolbarSections.Controls,
        )

    def update_actions(self):
        pass

    # --- Public API
    # ------------------------------------------------------------------------

    def start_pomodoro_timer(self):
        """Start the timer."""
        self.pomodoro_timer_status.timer.start(INTERVAL)
        self.pomodoro_timer_status.pause = False

    def pause_pomodoro_timer(self):
        """Pause the timer."""
        self.pomodoro_timer_status.timer.stop()
        self.pomodoro_timer_status.pause = True

    def stop_pomodoro_timer(self):
        """Stop the timer."""
        self.pomodoro_timer_status.timer.stop()
        self.pomodoro_timer_status.pause = True
        self.pomodoro_timer_status.countdown = self.pomodoro_timer_status.pomodoro_limit
