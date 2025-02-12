"""

Provisioning: Dashboards
========================

Contains
--------

Dashboards for ships

:copyright: (C) 2011-2015 riot@hackerfleet.org
:license: GPLv3 (See LICENSE)

"""

__author__ = "Heiko 'riot' Weinen <riot@hackerfleet.org>"

from hfos.provisions.base import provisionList
from hfos.database import dashboardobject
from hfos.logger import hfoslog

Dashboards = [
    {
        'name': 'Default',
        'uuid': '7df83542-c1c1-4c70-b754-51174a53453a',
        'description': 'Default blank dashboard',
        'shared': True,
        'locked': False,
        'cards': []
    }
]

def provision():
    provisionList(Dashboards, dashboardobject)
    hfoslog('[PROV] Provisioning: Dashboards: Done.')

if __name__ == "__main__":
    provision()