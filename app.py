import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QPushButton
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
    df = space_query(state_dict)


    window.query_display.setRowCount(df.shape[0])
    window.query_display.setColumnCount(df.shape[1])
    window.query_display.verticalHeader().hide()
    headers = ['']
    headers = headers + df.columns.values.tolist()
    print(headers)
    window.query_display.setHorizontalHeaderLabels(headers)
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            entry = df.iloc[i, j]
            window.query_display.setItem(i, j+1, QTableWidgetItem(str(entry)))
    for index in range(window.query_display.rowCount()):
        btn = QPushButton(window.query_display)
        btn.setText('add')
        window.query_display.setCellWidget(index, 0, btn)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui_file = "assets/front_end.ui"
    window = uic.loadUi(ui_file)
    window.source_telescope_selector.addItems(populate_sources())

    # Signals and Slots

    window.search_button.clicked.connect(write_state)
    window.show()
    sys.exit(app.exec())
