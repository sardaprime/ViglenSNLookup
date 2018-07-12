import os, subprocess, urlparse, webbrowser, requests, bs4

wmicOutput = subprocess.check_output(['wmic', 'baseboard', 'get', 'serialnumber'])
serialNumber = wmicOutput[17:24]
viglenLookup = 'http://www.viglen.co.uk/Viglen/Support/Configuration/?sn=' + serialNumber
viglenInfo = requests.get(viglenLookup)
viglenSoup = bs4.BeautifulSoup(viglenInfo.text, "html.parser")
elems = viglenSoup.select('#lblServiceExpire')
print('Hostname: ' + subprocess.check_output(['hostname']))
print('Serial Number: ' + serialNumber)
print('Warranty Expires: ' + elems[0].getText())
raw_input("Press Enter to exit...")
