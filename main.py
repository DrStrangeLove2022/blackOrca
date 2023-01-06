import sys
from arcgis.gis import GIS
import arcgis
import argparse as ap

from t_users import commands as group1
from version import commands as version
from account_check import commands as account_check
from domain_check import commands as d_check
from org_content import commands as o_content
from storage_use import commands as storage

def startUp(url, username, password):
    try:
        gis = GIS(url, username, password)
        group1.total_count(gis)
        d_check.email_check(gis)
    except Exception as X:
        print(X)
def total_count(gis):
    users = arcgis.gis.UserManager(gis)
    totalUsers = users.counts('user_type', as_df=False)[0]['count']
    print("Total Users: " + str(totalUsers))
    return totalUsers

if __name__ == "__main__":

    try:
        parser = ap.ArgumentParser(
            prog='blackOrca',
            description='blackOrca does things'
        )

        parser.add_argument(
            '--url',
            type=str,
            help='This is the url to your portal or AGOL site.',
            required=True
        )

        parser.add_argument(
            '--username',
            type=str,
            help='This is the username to your portal or AGOL site.',
            required=True
        )

        parser.add_argument(
            '--password',
            type=str,
            help='This is the password to your portal or AGOL site.',
            required=True
        )

        parser.add_argument(
            '--tu', type=str,
            help='This returns the total users in your organization.',
            metavar='Total Users',
            required=False
        )

        parser.add_argument(
            '--dc',
            type=str,
            help='This returns the domain count of users in your organization.',
            metavar='Domain Count',
            required=False
        )

        parser.add_argument(
            '--oc',
            type=str,
            help='This returns the total count of content in your organization.',
            metavar='Content Count',
            required=False
        )

        parser.add_argument(
            '--su',
            type=str,
            help='This returns the total storage use in your organization.',
            metavar='Storage Use',
            required=False
        )

        parser.add_argument(
            '--ac',
            help='This returns the total users in your organization.',
            metavar='Organizational Content',
            required=False
        )
        parser.print_help()
        args = parser.parse_args()

        startUp(args.url, args.username, args.password)

    except Exception as X:
        print(X)
        sys.exit(1)
