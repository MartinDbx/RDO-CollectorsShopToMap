#   From: https://github.com/MartinDbx/RDO-CollectorsShopToMap
#   File: main.py
#   Author: Martin Debaisieux
#   Date: 20 May 2024

import sys
sys.path.append("Utilities")
import reader, mapfinder


if __name__ == "__main__":

    fileName = ("rdo-collector-shop-list.txt" if len(sys.argv) == 1
               else sys.argv[1])

    COLLECTIONS = reader.collectionsExtractor(fileName)
    UNCOLLITEMS = reader.itemsExtractor(fileName)

    mapfinder.makeFileJR(COLLECTIONS, UNCOLLITEMS)