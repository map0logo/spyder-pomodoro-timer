# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Francisco Palm
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Pomodoro Timer Preferences Page.
"""
from qtpy.QtWidgets import QGridLayout, QGroupBox, QVBoxLayout
from spyder.api.preferences import PluginConfigPage
from spyder.api.translations import get_translation

from spyder_pomodoro_timer.spyder.config import POMODORO_DEFAULT

_ = get_translation("spyder_pomodoro_timer.spyder")


class SpyderPomodoroTimerConfigPage(PluginConfigPage):

    # --- PluginConfigPage API
    # ------------------------------------------------------------------------
    def setup_page(self):
        limits_group = QGroupBox(_("Time limits"))
        pomodoro_spin = self.create_spinbox(
            _("Pomodoro timer limit"),
            _("min"),
            "pomodoro_limit",
            default=POMODORO_DEFAULT,
            min_=5,
            max_=100,
            step=1,
        )

        pt_limits_layout = QGridLayout()
        pt_limits_layout.addWidget(pomodoro_spin.plabel, 0, 0)
        pt_limits_layout.addWidget(pomodoro_spin.spinbox, 0, 1)
        pt_limits_layout.addWidget(pomodoro_spin.slabel, 0, 2)
        pt_limits_layout.setColumnStretch(1, 100)
        limits_group.setLayout(pt_limits_layout)

        vlayout = QVBoxLayout()
        vlayout.addWidget(limits_group)
        vlayout.addStretch(1)
        self.setLayout(vlayout)
