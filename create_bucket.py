#!/usr/bin/python

import os, sys

from twisted.internet import reactor
from twisted.python.failure import Failure

from lae_automation.initialize import create_user_bucket


if len(sys.argv) < 6:
    print "Usage: python create_bucket.py USER_ACCESS_KEY_ID USER_SECRET_KEY USER_TOKEN LONG_PRODUCT_TOKEN BUCKET_NAME [LOCATION]"
    print "Happy bucket-creating!"
    sys.exit(1)

useraccesskeyid = sys.argv[1]
usersecretkey = sys.argv[2]
usertoken = sys.argv[3]
producttoken = sys.argv[4]
bucketname = sys.argv[5]
if len(sys.argv) > 6:
    location = sys.argv[6]
else:
    location = None  # default

def cb(x):
    print str(x)
    if isinstance(x, Failure) and hasattr(x.value, 'response'):
        print x.value.response

d = create_user_bucket(useraccesskeyid, usersecretkey, usertoken, bucketname, sys.stdout, sys.stderr,
                       producttoken=producttoken, location=location)
d.addBoth(cb)
d.addCallbacks(lambda ign: os._exit(0), lambda ign: os._exit(1))
reactor.run()
