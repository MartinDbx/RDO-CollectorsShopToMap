#   From: https://github.com/MartinDbx/RDO-CollectorShopToMap
#   File: utilities/generator.py
#   Author: Martin Debaisieux
#   Date: 19 May 2024

import shutil, items, datetime


def __generateCart(fileName: str) -> list:
    cart = []
    fileName = "utilities/rdo-collector-shop-list.txt"
    with open(fileName, "r") as file:
        lines = file.readlines()
        for collection in items.COLLECTIONS:
            for item in collection[1:]:
                for line in lines:
                    if item in line:
                        cart.append(collection[0]) if collection[0] not in cart else None
                        break
    return cart

def __generateUncollectedItems(fileName: str) ->list:
    fileName = "utilities/rdo-collector-shop-list.txt"
    with open(fileName, "r") as file:
        lines = file.readlines()
        uncollectedItems = [item[:-1] for item in lines[:-1]]
        uncollectedItems.append(lines[-1])
    return uncollectedItems


def __dateOfToday():
    """Creates the .json line for the date of today."""

    today = datetime.date.today()
    formattedDate = today.strftime("%Y-%m-%d")

    return "    \"rdr2collector.date\": \"" + formattedDate + "\",\n"


def __collectionsToShow(cart: list):
    """Creates the .json line to show only the selected collections."""

    txt = ""

    for collection in cart[:-1]:
        txt += "\\\"" + collection + "\","

    txt += "\\\"" + cart[-1] + "\""

    return "    \"rdr2collector.enabled-categories\": \"[" + txt + "]\","


def makeFileJR(collectionsToShow: list, uncollectedItems: list):
    """Generate 'collector-list.json' where only uncollectedItems of
    collectionsToShow are visible. This file can be uploaded into
    https://jeanropke.github.io/RDR2CollectorsMap/."""

    shutil.copyfile("utilities/template-collector-list.json", "collector-list.json")
    idx = 0

    for item in uncollectedItems:

        with open("collector-list.json", "r") as file:
            lines = file.readlines()

        with open("collector-list.json", "w") as file:
            for line in lines:
                if idx == 0 and len(line) == 1:
                    file.write(__dateOfToday())
                    file.write(__collectionsToShow(collectionsToShow))
                    idx = 1
                if "collected" not in line or item not in line:
                    file.write(line)