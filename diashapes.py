# !/usr/bin/python
# -*- coding: utf-8
import sys
import os
from os.path import exists, expanduser
import re
import subprocess
from zipfile import ZipFile
from urllib.request import urlretrieve
import webbrowser
import xml.etree.ElementTree as ET
import requests


# URLS
DOWNLOAD_URL = "http://dia-installer.de/download.html"
SHEETS_URL = "http://dia-installer.de/sheets.xml"
SEARCH_URL = "http://dia-installer.de/shapes/search.html"
VERSIONS_URL = "http://dia-installer.de/versions.xml"

#$HOME/.dia directory for UNIX
DOTDIA = expanduser("~/.dia")


def open_in_browser(url):
    "opens url in a new tab in the default web browser."
    webbrowser.open_new_tab(url)


def open_search_page():
    "opens search page in a new tab."
    open_in_browser(SEARCH_URL)


def open_download_page():
    "opens download page in a new tab."
    open_in_browser(DOWNLOAD_URL)


def get_installed_dia_version():
    "get installed dia version."
    s = subprocess.check_output(["dia", "-v"])
    s = s.decode()  # bytes to string.
    m = re.search("([0-9.]+)", s)
    if m:
        return m.group(0)

    return '0.0.0'  # any version is newer than noninstalled dia!


def get_data_from_url(url):
    return requests.get(url).text.encode("utf-8")


class DiaSheet(object):

    def __init__(self, name, description, creator, website, download, selected=False):
        self.name = name
        self.description = description
        self.creator = creator
        self.website = website
        self.download = download
        self.selected = False

    def get_data(self):
        return [self.name, self.description, self.creator, self.website, self.download, self.selected]

    def __str__(self):
        return "<DiaSheet: %s>" % str(self.get_data())


def diasheets_from_xml(xml):
    root = ET.fromstring(xml)
    diasheets = []
    for sheet in root.findall("sheet"):
        name = sheet.get("name")
        desc = sheet.get("description")
        creator = sheet.get("creator")
        website = sheet.get("website")
        download = sheet.get("download")
        diasheets.append(DiaSheet(name, desc, creator, website, download))

    return diasheets


def get_data_from_diasheets(diasheets):
    return [x.get_data() for x in diasheets]


def get_sheets_data():
    return get_data_from_diasheets(diasheets_from_xml(get_data_from_url(SHEETS_URL)))


def get_versions():

    # DIA version/DIASHAPES-MONO version
    xml = get_data_from_url(VERSIONS_URL)
    root = ET.fromstring(xml)
    dia_lastversion = None
    diashapes_mono_lastversion = None
    for p in root.findall("product"):
        name = p.get('name')
        version = p.get('version')
        if name == "dia":
            dia_lastversion = version
        else:
            diashapes_mono_lastversion = version

    return {"dia": dia_lastversion, "diashapes_mono": diashapes_mono_lastversion}


def update_available():
    lastdia = get_versions().get('dia')
    return lastdia > get_installed_dia_version()


def prepare_dotdia():

    if not exists(DOTDIA):
        os.mkdir(DOTDIA)


def install_sheets(sheetsdata):
    # check if HOME directory exists else use Desktop directory
    # create $HOME/.dia if not exists for UNIX
    # setcwd to $HOME/.dia

    prepare_dotdia()
    os.chdir(DOTDIA)
    for idx, sheetdata in enumerate(sheetsdata):
        sheet = DiaSheet(*sheetdata)
        zippedname = sheet.name + ".zip"
        urlretrieve(sheet.download, zippedname)
        zipfile = ZipFile(zippedname)
        zipfile.extractall(sheet.name)
        os.remove(zippedname)
        yield idx
