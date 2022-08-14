import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

state_dict = {}

def write_state(win):
    global state_dict
    state_dict["telescope"] = window.source_telescope_selector.currentText()
    state_dict["object name"] = window.object_name_edit.text()
    state_dict["object type"] = window.object_type_selector.currentText()
    state_dict["galactic coordinates"] = [window.RA_edit.text(), window.DEC_edit.text()]
    state_dict["date range"] = [window.start_date_edit.date(), window.end_date_edit.date()]
    state_dict["last_name"] = window.last_name_edit.text()
    state_dict["sort_by"] = window.sort_by_selector.currentText()
    print(state_dict)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui_file = "assets/front_end.ui"
    window = uic.loadUi(ui_file)
    window.source_telescope_selector.currentIndexChanged.connect(write_state)
    window.show()
    sys.exit(app.exec())
