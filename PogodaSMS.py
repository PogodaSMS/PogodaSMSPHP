import urllib2
import re

response = urllib2.urlopen('http://www.yr.no/place/Poland/Lesser_Poland/Krakow/hour_by_hour.html')
html = response.read()
file = open("html.txt", "w")
file.write(html)
file.close()

mod_file = open("html_mod.txt", "w")

f = open("html.txt","r+")
d = f.readlines()
f.seek(0)

licznik = 0

for i in d:
	if (licznik > 0):
		licznik = licznik - 1
		mod_file.write(i)
	else:
		found = re.match('.*<td scope="row">', i)
		if found:
			mod_file.write(i)
			licznik = 7
		
mod_file.truncate()		
mod_file.close()
