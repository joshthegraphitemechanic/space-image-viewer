from astroquery.mast import Observations
import PyQt5
from PyQt5 import QtCore


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


def populate_sources():
    telescope_sources = Observations.list_missions()
    return(telescope_sources)


def space_query(
    query_dict
):
    params = {}
    params["obs_collection"] = query_dict["telescope"]
    if query_dict["object name"] != '':
        params["target_name"] = query_dict["object name"]
    if query_dict["object type"] != 'N/A':
        params["target_classification"] = query_dict["object type"]
    if query_dict["dec"] != '':
        params["s_dec"] = query_dict["dec"]
    if query_dict["ra"] != '':
        params["s_ra"] = query_dict["ra"]
    if query_dict["date toggle"]:
        params["t_min"] = query_dict["date min"]
        params["t_max"] = query_dict["date max"]
    if query_dict["last name"] != '':
        params["proposal_pi"] = query_dict["last name"]
    sorting = query_dict["sort by"]



    obs_table = Observations.query_criteria(**params)
    data = obs_table.to_pandas()
    model = PandasModel(data)
    return(model)
