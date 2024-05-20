# RDO - Collector's Shop to Map

The jeanropke's [Collectors Map](https://jeanropke.github.io/RDR2CollectorsMap/) is an efficient way to complete your Red Dead Online collections. Compare your collections and hide the items you've collected is quite tedious. This repository automates this process, by letting you choose the items you want to appear and generating a settings file that can be imported into the map. This method is ideal for groups of collectors who want to merge their list of items to be collected.

## Supported collections

For some collections, it is not possible to determine the location of a given item. This tool is therefore only designed for deterministic collections.

- [ ] American Wild Flowers	(soon)
- [x] Antique Alcohol Bottles
- [ ] Bird Eggs (soon)
- [x] Family Heirlooms
- [x] Suit of Cups Tarot Cards
- [x] Suit of Pentacles Tarot Cards
- [x] Suit of Swords Tarot Cards
- [x] Suit of Wands Tarot Cards


## Usage

1. Open `index.html`, check the boxes corresponding to the items you want to fetch and click on 'Generate List'.  This builds the file `rdo-collector-shop-list.json` that you can download.
2. Run `main.py` in your shell, followed by the path to the file `rdo-collector-shop-list.json`.  This builds the file `rdo-collector-map-list-date.json`.
3. Import `rdo-collector-map-list-date.json` as settings into jeanropke's [Collectors Map](https://jeanropke.github.io/RDR2CollectorsMap/).

## Options

If you store the file `rdo-collector-shop-list.json` at the same level as `main.py`, you can run the former without specifying the path.