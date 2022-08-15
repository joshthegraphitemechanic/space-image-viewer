from astroquery.mast import Observations
import PyQt5

test_query = {
    "telescope": "Hubble",
    "object name": "",
    "object type": "N/A",
    "galactic coordinates": ["", ""],
    "date range": [PyQt5.QtCore.QDate(2000, 1, 1), PyQt5.QtCore.QDate(2000, 1, 1)],
    "last_name": "",
    "sort_by": "",
}


def populate_sources():
    telescope_sources = Observations.list_missions()
    return(telescope_sources)


def space_query(
    query_dict
):
    telescope = query_dict["telescope"]
    params = {"obs_collection": telescope}




    obs_table = Observations.query_criteria(**params)
    return(obs_table)
