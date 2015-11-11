from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    )

import Utils.utils

@view_config(route_name='main', renderer='templates/main.jinja2')
def main(request):
    gmapAPIKey = 'AIzaSyCfHLNcaqTGEcYj0EU1Yqr0v78LwMoQiMM'
    Utils.utils.parseKML()
    return { 'gmapAPIKey' : gmapAPIKey }

@view_config(route_name='stub', renderer='templates/stub.jinja2')
def stub(request):
    gmapAPIKey = 'AIzaSyCfHLNcaqTGEcYj0EU1Yqr0v78LwMoQiMM'
    return { 'gmapAPIKey' : gmapAPIKey }


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_foodie_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

