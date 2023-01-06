import click
import arcgis
import datetime
from datetime import timedelta
import time
from time import mktime

def date_check():
    present_time = datetime.now()
    # Currently set to 90 days
    old_account_time = present_time - timedelta(90)
    formatted_time = old_account_time.strftime("%m/%d/%Y %H:%M:%S")
    return old_account_time

def total_count(gis):
    # Function returns the total number of users on the portal
    users = arcgis.gis.UserManager(gis)
    totalUsers = users.counts('user_type', as_df=False)[0]['count']
    # print("Total Users: " + str(totalUsers))
    return totalUsers

def get_users(gis):
    # users_num = total_count()
    users_num = total_count()
    # For development this is set to 15 people. If set higher, for example 10000 takes a long time to process.
    p_users = gis.users.search(max_users=users_num)
    # p_users = gis.users.advanced_search(query='*', max_users=users_num)
    print(f"There are currently {p_users} in your portal.")
    return p_users

@click.command()
def account_checker(gis):
    """Returns Total # of Active/Inactive/Never Logged-In Users"""
    # This calls the get_users() function, which returns all the users on the portal.
    current_users = get_users(gis)
    # This calls the date_check() function, which establishes a "dead account" with no activity in x number of days
    dead_account = date_check()
    active_accounts = []
    dead_accounts = []
    never_logged = []
    for user in current_users:
        # Since some portals can create users w/o those users never signing in, which breaks the code.
        # So that is why this is here.
        if user.lastLogin != -1:
            # Due to how ArcGIS Portal stores the date in unix time it needs to be converted from int to
            # time.struct_time
            last_accessed = time.localtime(user.lastLogin / 1000)
            created = time.localtime(user.created / 1000)
            # Then converted again from a time.struct_time to a datetime.datetime
            new_time_example = datetime.fromtimestamp(mktime(last_accessed))
            created_new_time = datetime.fromtimestamp(mktime(created))
            if new_time_example > dead_account:
                active_accounts.append(user)
            else:
                dead_accounts.append(user)
                # print(f"{user.username}, {created_new_time}, {new_time_example}, {user.email}, {user.roleId}")
        else:
            never_logged.append(user)
            # print(f"{user.username}: Has never logged in to the portal.")
    return active_accounts, dead_accounts, never_logged