import hashlib
import pycurl
import sys
import urllib2
from StringIO import StringIO

import feedparser


def get_html_doc(url):
    """
    :rtype: object
    """
    buffer = StringIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.WRITEDATA, buffer)
    c.setopt(pycurl.USERAGENT, 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:8.0) Gecko/20100101 Firefox/8.0')
    c.setopt(pycurl.SSL_VERIFYPEER, 1)
    c.setopt(pycurl.SSL_VERIFYHOST, 2)
    c.perform()
    c.close()
    body = buffer.getvalue()
    return body


if __name__ == "__main__":
    url = str(sys.argv[1])
    d = feedparser.parse("http://" + url)
    page = urllib2.urlopen("http://" + url)
    fake_etag = hashlib.sha256(page.read(1024)).hexdigest()
    try:
        print "ETag:", str(d.etag)
    except:
        pass
    print "Fake ETag: ", fake_etag
