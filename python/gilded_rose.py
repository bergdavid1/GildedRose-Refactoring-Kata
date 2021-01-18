# -*- coding: utf-8 -*-

def is_expired_item(item):
    return


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                pass
            elif item.name == "Aged Brie":
                item.quality = min(item.quality + 2, 50)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.quality = min(item.quality + 1, 50)
                if item.sell_in < 11:
                    item.quality = min(item.quality + 1, 50)
                if item.sell_in < 6:
                    item.quality = min(item.quality + 1, 50)
            else:
                if item.quality > 0:
                    item.quality = item.quality - 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0:
                if item.name in {"Sulfuras, Hand of Ragnaros", "Aged Brie"}:
                    pass
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = item.quality - item.quality
                else:
                    if item.quality > 0:
                        item.quality = item.quality - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
