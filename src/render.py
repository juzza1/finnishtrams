#!/usr/bin/python

from csv import DictReader, reader
import sys

from basecosts import write_basecosts
from cargos import Cargos 
from tram import Tram

def parse_rows(csv, id_):
    """
    Convert DictReader object into a list of dicts. Rows without a value in
    param cell are ignored.
    """
    out = []
    for row in csv:
        if row[id_]:
            out.append(row)
        else:
            continue
    return out

csv_path = 'src/csv/'

with open (csv_path + 'cost_factors.csv', 'rb') as csv:
    base_costs = DictReader(csv)
    base_costs = parse_rows(base_costs, 'id')

with open (csv_path + 'trams.csv', 'rb') as csv:
    vehs = DictReader(csv)
    vehs = parse_rows(vehs, 'name')

with open (csv_path + 'cargodefs.csv', 'rb') as csv:
    cargotable = csv.read()

# Write files
write_basecosts(base_costs, 'build/b_basecosts.pnml')

c = Cargos(cargotable)
c.write_cargotable('build/c_cargotable.pnml')

for veh in vehs:
    c = Cargos(cargotable)
    t = Tram(veh, c)
    t.all_out('build/d_%s.pnml', 'build/')
