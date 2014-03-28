WGET = wget -q --no-check-certificate --output-document=src/csv/
NULLOUT = > /dev/null
E = 

all:
	cp src/pnml/* build/
	python src/render.py
csv:
	$(E)$(WGET)trams.csv \
	"http://docs.google.com/spreadsheet/ccc?key=\
	0AtusRKUv7vK5dDVBZ1BhaFlKajlhUk83LU5HUTNiY3c&gid=0&output=csv"
	$(E)$(WGET)cargodefs.csv \
	"http://docs.google.com/spreadsheet/ccc?key=\
	0AtusRKUv7vK5dDVBZ1BhaFlKajlhUk83LU5HUTNiY3c&gid=2&output=csv"
	$(E)$(WGET)cost_factors.csv \
	"http://docs.google.com/spreadsheet/ccc?key=\
	0AtusRKUv7vK5dDVBZ1BhaFlKajlhUk83LU5HUTNiY3c&gid=1&output=csv"
