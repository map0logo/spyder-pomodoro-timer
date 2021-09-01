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
import qtawesome as qta

# Spyder imports
from spyder.api.plugin_registration.decorators import on_plugin_available
from spyder.api.plugins import Plugins, SpyderPluginV2
from spyder.api.translations import get_translation
from spyder.utils.icon_manager import ima

# Local imports
from spyder_pomodoro_timer.spyder.confpage import SpyderPomodoroTimerConfigPage
from spyder_pomodoro_timer.spyder.container import SpyderPomodoroTimerContainer
from spyder_pomodoro_timer.spyder.config import CONF_DEFAULTS, CONF_VERSION


_ = get_translation("spyder_pomodoro_timer.spyder")


class SpyderPomodoroTimer(SpyderPluginV2):
    """
    Spyder Pomodoro Timer plugin.
    """

    NAME = "spyder_pomodoro_timer"
    REQUIRES = [Plugins.Preferences, Plugins.StatusBar, Plugins.Toolbar]
    OPTIONAL = []
    CONTAINER_CLASS = SpyderPomodoroTimerContainer
    CONF_SECTION = NAME
    CONF_WIDGET_CLASS = SpyderPomodoroTimerConfigPage
    CONF_DEFAULTS = CONF_DEFAULTS
    CONF_VERSION = CONF_VERSION

    # --- Signals

    # --- SpyderPluginV2 API
    # ------------------------------------------------------------------------
    def get_name(self):
        return _("Spyder Pomodoro Timer")

    def get_description(self):
        return _("A very simple pomodoro timer that shows in the status bar.")

    def get_icon(self):
        return qta.icon("mdi.av-timer", color=ima.MAIN_FG_COLOR)

    def on_initialize(self):
        print("SpyderPomodoroTimer registered!")

    @on_plugin_available(plugin=Plugins.Preferences)
    def on_preferences_available(self):
        preferences = self.get_plugin(Plugins.Preferences)
        preferences.register_plugin_preferences(self)

    @on_plugin_available(plugin=Plugins.StatusBar)
    def on_statusbar_available(self):
        statusbar = self.get_plugin(Plugins.StatusBar)
        if statusbar:
            statusbar.add_status_widget(self.pomodoro_timer_status)

    @on_plugin_available(plugin=Plugins.Toolbar)
    def on_toolbar_available(self):
        container = self.get_container()
        toolbar = self.get_plugin(Plugins.Toolbar)
        toolbar.add_application_toolbar(container.pomodoro_timer_toolbar)

    def check_compatibility(self):
        valid = True
        message = ""  # Note: Remember to use _("") to localize the string
        return valid, message

    def on_close(self, cancellable=True):
        return True

    # --- Public API
    # ------------------------------------------------------------------------

    @property
    def pomodoro_timer_status(self):
        container = self.get_container()
        return container.pomodoro_timer_status
