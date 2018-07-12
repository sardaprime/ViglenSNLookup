import os, subprocess, urlparse, webbrowser, bs4

wmicOutput = subprocess.check_output(['wmic', 'baseboard', 'get', 'serialnumber']) #Get serial number from WMIC
serialNumber = wmicOutput[17:] #Slice string to just SN
viglenLookup = 'http://www.viglen.co.uk/Viglen/Support/Configuration/?sn=' + serialNumber #Build lookup URL
webbrowser.open(viglenLookup) #Open lookup URL