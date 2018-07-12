import os, subprocess, urlparse, webbrowser, bs4

wmicOutput = subprocess.check_output(['wmic', 'baseboard', 'get', 'serialnumber'])
serialNumber = wmicOutput[17:]
viglenLookup = 'http://www.viglen.co.uk/Viglen/Support/Configuration/?sn=' + serialNumber
webbrowser.open(viglenLookup)