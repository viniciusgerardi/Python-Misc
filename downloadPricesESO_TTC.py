# Tool to automate the download of price lists from TamrielTradeCentre website, to use with
# Tamriel Trade Centre addon - https://www.esoui.com/downloads/info1245-TamrielTradeCentre.html
# Not afiliated with The Elder Scrolls®, ZeniMax®, https://tamrieltradecentre.com/ or its licensors.
#
# This tool shold be placed on the Tamriel Trade Center addon root folder, and the variables
# platform and region set according your necessities.


import os
import shutil
import requests


class TTC:

    def __init__(self, region, plataform):
        self.region = region
        self.plataform = plataform
        self.setServer()
        self.path = os.path.dirname(os.path.realpath(__file__)) + os.sep
        self.filename = 'prices.zip'

    def validateURL(self):
        if self.url == 'false':
            return False
        else:
            return True

    def download(self):
        if self.validateURL:
            print('Downloading file... ', end='')
            file = requests.get(self.url, allow_redirects=True)
            open(self.path + self.filename, 'wb').write(file.content)
            print('done')
        else:
            print('Invalid URL')

    def extract(self):
        if self.validateURL:
            print('Extracting files... ', end='')
            shutil.unpack_archive(self.path + self.filename, self.path)
            print('done')
        else:
            print('Invalid URL')

    def clear(self):
        if self.validateURL:
            print('Cleaning files... ', end='')
            os.remove(self.path + self.filename)
            print('done')
        else:
            print('Invalid URL')

    # Getters and Setters
    def setServer(self):
        if self.plataform == "PC" and self.region == "NA":
            self.url = 'https://us.tamrieltradecentre.com/download/PriceTable'
        elif self.plataform == "PC" and self.region == "EU":
            self.url = 'https://eu.tamrieltradecentre.com/download/PriceTable'
        else:
            self.url = 'false'

    def setRegion(self, region):
        self.region = region
        self.setServer()

    def setPlataform(self, plataform):
        self.plataform = plataform
        self.setServer()

    def getServer(self):
        return self.url

    def getRegion(self):
        return self.region

    def getPlataform(self):
        return self.plataform


# Main program
region = 'NA'  # NA (North America) or EU (Eurpe) region
plataform = 'PC'  # Currently only support PC plataform
prices = TTC(region, plataform)

prices.download()
prices.extract()
prices.clear()
