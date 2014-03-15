#!/usr/bin/python

from ConfigParser import RawConfigParser
from cookielib import CookieJar
from csv import DictReader, reader
import sys
from StringIO import StringIO
from urllib2 import build_opener, HTTPCookieProcessor, HTTPError, URLError

from basecosts import write_basecosts
from cargos import Cargos 
from tram import Tram

def get_google_docs(url):
    """Read a Google docs csv url and write it as a file object"""
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    return opener.open(url).read()

def get_local_csv(path):
    """Read csv locally"""
    with open (path, 'rb') as outcsv:
        return outcsv

def fetcher(url, path, format_ = None):
    """Attempt to read CSV from url, fallback to local file. DictReader
    requires a file object, use StringIO"""
    try:
        print "Fetching CSV from '%s'" % url
        outcsv = get_google_docs(url)
        print "Success, saving to '%s'" % path
        with open (path, 'wb') as f:
            f.write(outcsv)
    except (HTTPError, URLError):
        print "Fetching CSV from Google URL failed, fetching locally "\
              "from '%s'" % path
        try:
            outcsv = get_local_csv(path)
            print "Success"
        except:
            print "No '%s' exists, or something else failed after "\
                  "attempting to get local csv." % path
            sys.exit()
    if format_ == 'strio':
        return StringIO(outcsv)
    else:
        return outcsv

def parse_rows(csv, id_):
    """Convert DictReader object into a list of dicts. Rows without a value in
    param cell are ignored"""
    out = []
    for row in csv:
        if row[id_]:
            out.append(row)
        else:
            continue
    return out

conf = 'config.ini'

# Read config file
configParser = RawConfigParser()
configParser.read(conf)

conf_base_costs = (configParser.get('base_costs', 'url'), configParser.get('base_costs', 'path'))
conf_vehs = (configParser.get('vehs', 'url'), configParser.get('vehs', 'path'))
conf_cargotable = (configParser.get('cargotable', 'url'), configParser.get('cargotable', 'path'))

base_costs = DictReader(fetcher(conf_base_costs[0], conf_base_costs[1], 'strio'))
vehs = DictReader(fetcher(conf_vehs[0], conf_vehs[1], 'strio'))
cargotable = fetcher(conf_cargotable[0], conf_cargotable[1])

vehs = parse_rows(vehs, 'name')
base_costs = parse_rows(base_costs, 'id')

# Write files
write_basecosts(base_costs, 'build/b_basecosts.pnml')

c = Cargos(cargotable)
c.write_cargotable('build/c_cargotable.pnml')

for veh in vehs:
    c = Cargos(cargotable)
    t = Tram(veh, c)
    t.all_out('build/d_%s.pnml', 'build/')
