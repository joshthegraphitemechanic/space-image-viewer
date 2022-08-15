import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtCore
from Python.star_math import *
import pandas as pd
from astropy.time import Time

state_dict = {}


def write_state(win):
    global state_dict
    state_dict["telescope"] = window.source_telescope_selector.currentText()
    state_dict["object name"] = window.object_name_edit.text()
    state_dict["object type"] = window.object_type_selector.currentText()
    state_dict["ra"] = window.RA_edit.text()
    state_dict["dec"] = window.DEC_edit.text()
    state_dict["date toggle"] = window.date_toggle.isChecked()
    state_dict["date min"] = Time(window.start_date_edit.date().toString("yyyy-MM-dd"), scale='utc').mjd
    state_dict["date max"] = Time(window.end_date_edit.date().toString("yyyy-MM-dd"), scale='utc').mjd
    state_dict["last name"] = window.last_name_edit.text()
    state_dict["sort by"] = window.sort_by_selector.currentText()
    window.query_display.setModel(space_query(state_dict))



if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui_file = "assets/front_end.ui"
    window = uic.loadUi(ui_file)
    window.source_telescope_selector.addItems(populate_sources())

    # Signals and Slots

    window.search_button.clicked.connect(write_state)
    window.show()
    sys.exit(app.exec())
