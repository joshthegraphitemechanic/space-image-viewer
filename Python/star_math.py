from astroquery.mast import Observations
import PyQt5
from PyQt5 import QtCore
from astropy.table import Table

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

    print(type(obs_table))
    data = obs_table.to_pandas()
    return(data)

def download_selected(selection):
    obs = Table.from_pandas(selection)
    data_products = Observations.get_product_list(obs)
    print(data_products)
    manifest = Observations.download_products(data_products, productType="SCIENCE")
    print(manifest)