#   From: https://github.com/MartinDbx/RDO-CollectorShopToMap
#   File: main.py
#   Author: Martin Debaisieux
#   Date: 19 May 2024

import sys
sys.path.append("utilities")
import generator

if __name__ == "__main__":

    SHOPCART = generator.__generateCart(sys.argv[1])
    UNCOLITEMS = generator.__generateUncollectedItems(sys.argv[1])

    generator.makeFileJR(SHOPCART, UNCOLITEMS)