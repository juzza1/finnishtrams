#!/usr/bin/python

from chameleon import PageTemplateFile
from cookielib import CookieJar
from csv import DictReader
import os
import sys
from StringIO import StringIO
from urllib2 import build_opener, HTTPCookieProcessor

# Custom modules
from tram import Tram

def GetGoogleDocs():
    "Read a Google docs csv url and write it as a file object"
    url = 'https://docs.google.com/spreadsheet/ccc?key=0AtusRKUv7vK5dDVBZ1BhaFlKajlhUk83LU5HUTNiY3c&output=csv'
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    incsv = opener.open(url).read()
    outcsv = StringIO(incsv)
    return outcsv

def GetLocalCsv():
    "Read trams.csv locally"
    with open ('trams.csv', 'rb') as outcsv:
        return outcsv

try:
    getcsv = GetGoogleDocs()
except:
    print "Fetching CSV from Google URL failed, fetching locally..."
    try:
        getcsv = GetLocalCsv()
    except:
        print "No trams.csv exists, or something else failed after "\
              "attempting to get local csv."
        sys.exit()

incsv = DictReader(getcsv, delimiter=',', quotechar='"')

vehs = []
for row in incsv:
    name = row['name']
    # Rows with empty "name" cell are ignored
    if not name:
        pass
    else:
        vehs.append(row)


template = PageTemplateFile('tram_temp.tnml')

vehobjs = {}
for veh in vehs:
    name = veh['name']
    tram = Tram(**veh)
    vehobjs[name] = tram
    with open(name + '.pnml', 'wb') as out:
        out.write(template.render(**tram.__dict__))


#print vehobjs
