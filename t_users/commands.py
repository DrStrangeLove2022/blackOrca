import arcgis
from arcgis.gis import GIS

def total_count(gis):
    """Display Total # of Users"""
    users = arcgis.gis.UserManager(gis)
    totalUsers = users.counts('user_type', as_df=False)[0]['count']
    # print("Total Users: " + str(totalUsers))
    print("Total Users: " + str(totalUsers))
    return totalUsers


