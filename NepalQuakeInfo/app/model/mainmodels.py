'''
Created on Apr 28, 2015

@author: harendra
'''

from google.appengine.ext import ndb

class HelpRequestReport(ndb.Model):
    attributes = [ "reporter_name", "reporter_email", "reporter_phone", "help_type", "help_address", "latitude", "longitude", "freetext", "imagelink"]

    reporter_name=ndb.StringProperty()
    reporter_email=ndb.StringProperty()
    reporter_phone=ndb.StringProperty()
    reported_date=ndb.StringProperty()
    help_type=ndb.StringProperty()
    help_address=ndb.StringProperty()
    latitude=ndb.StringProperty()
    longitude=ndb.StringProperty()
    status=ndb.StringProperty()
    freetext=ndb.StringProperty()
    imagelink=ndb.StringProperty()
    
    
        