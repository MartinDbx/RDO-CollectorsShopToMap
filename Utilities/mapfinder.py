#   From: https://github.com/MartinDbx/RDO-CollectorsShopToMap
#   File: Utilities/mapfinder.py
#   Author: Martin Debaisieux
#   Date: 20 May 2024

import datetime, shutil


def __dateOfToday(formattedDate: str) -> str:
    """Formats the .json date line."""

    return "    \"rdr2collector.date\": \"" + formattedDate + "\",\n"


def __collectionsToShow(collections: list) -> str:
    """Creates the .json line to show only the selected collections."""

    txt = ""

    for collection in collections[:-1]:
        txt += "\\\"" + collection + "\","

    txt += "\\\"" + collections[-1] + "\""

    return "    \"rdr2collector.enabled-categories\": \"[" + txt + "]\","


def makeFileJR(collectionsToShow: list, uncollectedItems: list):
    """Generate 'collector-list.json' where only uncollectedItems of
    collectionsToShow are visible. This file can be uploaded into
    https://jeanropke.github.io/RDR2CollectorsMap/."""

    idx = 0
    today = datetime.date.today()
    formattedDate = today.strftime("%Y-%m-%d")
    fileName = "rdo-collector-map-list-" + formattedDate + ".json"

    shutil.copyfile("Utilities/template-collector-list.json", fileName)

    for item in uncollectedItems:

        with open(fileName, "r") as file:
            lines = file.readlines()

        with open(fileName, "w") as file:
            for line in lines:
                if idx == 0 and len(line) == 1:
                    file.write(__dateOfToday(formattedDate))
                    file.write(__collectionsToShow(collectionsToShow))
                    idx = 1
                if "collected" not in line or item not in line:
                    file.write(line)
