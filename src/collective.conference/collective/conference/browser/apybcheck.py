import json
import urllib2
from zope.app.component.hooks import getSite

def check_apyb_membership(email):
    # XXX refactor the proxy config to run only once

    # If your site is behind a proxy,
    # you must configure a 'http_proxy' property for it
    #  (in its "Properties" tab in the ZMI)
    portal = getSite()
    if hasattr(portal, 'http_proxy'):
        proxy = urllib2.ProxyHandler({'http': portal.http_proxy})
        opener = urllib2.build_opener(proxy)
        urllib2.install_opener(opener)

    response = json.load(urllib2.urlopen("http://associados.python.org.br/members/status/?email=%s" % email))
    return response['status']

