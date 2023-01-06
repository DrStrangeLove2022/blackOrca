import pandas as pd
import arcgis
from arcgis.gis import GIS

def total_count(gis):
    """Display Total # of Users"""
    users = arcgis.gis.UserManager(gis)
    totalUsers = users.counts('user_type', as_df=False)[0]['count']
    return totalUsers

def get_users(gis):
    users_num = total_count(gis)
    p_users = gis.users.search(max_users=users_num)
    return p_users
def email_check(gis):
    portal_users = get_users(gis)
    emails_list = []
    domain_list = []
    domain = []
    for user in portal_users:
        emails_list.append(user.email)
    for value in emails_list:
        email = value.split('@')[1]
        if email not in domain_list:
            domain_list.append(email)
    # print(domain_list)
    for value in emails_list:
        counters = domain.append(value.split('@')[1])
        domain_count = pd.Series(domain).value_counts()
    #print(Counter(domain))
    print(domain_count)