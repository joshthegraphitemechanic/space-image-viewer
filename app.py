import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic, QtCore
from Python.star_math import *
import pandas as pd


state_dict = {}


class PandasModel(QtCore.QAbstractTableModel):
    """
    Class to populate a table view with a pandas dataframe
    """
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.iloc[index.row()][index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None


def write_state(win):
    global state_dict
    state_dict["telescope"] = window.source_telescope_selector.currentText()
    state_dict["object name"] = window.object_name_edit.text()
    state_dict["object type"] = window.object_type_selector.currentText()
    state_dict["galactic coordinates"] = [window.RA_edit.text(), window.DEC_edit.text()]
    state_dict["date range"] = [
        window.start_date_edit.date(),
        window.end_date_edit.date(),
    ]
    state_dict["last_name"] = window.last_name_edit.text()
    state_dict["sort_by"] = window.sort_by_selector.currentText()
    display = space_query(state_dict).to_pandas()
    model = PandasModel(display)
    window.query_display.setModel(model)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    ui_file = "assets/front_end.ui"
    window = uic.loadUi(ui_file)
    window.source_telescope_selector.addItems(populate_sources())

    # Signals and Slots

    window.search_button.clicked.connect(write_state)
    window.show()
    sys.exit(app.exec())
