import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QPushButton
from PyQt5 import uic, QtCore
from Python.star_math import *
import pandas as pd
from astropy.time import Time
import pyqtgraph as pg
from astropy.utils.data import get_pkg_data_filename
from astropy.io import fits 

state_dict = {}

def write_state(win):
    global state_dict
    global df
    global selected_df
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
    selected_df = pd.DataFrame(columns = df.columns.values.tolist())
    print(headers)
    window.query_display.setHorizontalHeaderLabels(headers)
    for i in range(df.shape[0]):
        for j in range(df.shape[1]):
            entry = df.iloc[i, j]
            window.query_display.setItem(i, j+1, QTableWidgetItem(str(entry)))
    for index in range(window.query_display.rowCount()):
        btn = QPushButton(window.query_display)
        btn.setText('Select')
        btn.clicked.connect(add_data)
        window.query_display.setCellWidget(index, 0, btn)


def add_data():
    button = QApplication.focusWidget()
    index = window.query_display.indexAt(button.pos())
    if index.isValid():
        content = df.loc[index.row()].values.tolist()
        selected_df.loc[len(df)] = content
        window.selected_data_display.addItem(content[3])

    

def display_image():
    download_selected(selected_df)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui_file = "assets/front_end.ui"
    window = uic.loadUi(ui_file)
    window.source_telescope_selector.addItems(populate_sources())
    window.selected_data_display.itemDoubleClicked.connect(display_image)
    # Signals and Slots

    window.search_button.clicked.connect(write_state)
    window.show()
    sys.exit(app.exec())
