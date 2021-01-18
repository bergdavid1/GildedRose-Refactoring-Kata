# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def assert_update_quality_output(self, expected_sell_in, expected_quality, item_name, items):
        # All items have a SellIn value which denotes the number of days we have to sell the item
        # All items have a Quality value which denotes how valuable the item is
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_name, items[0].name)
        self.assertEqual(item_name, gilded_rose.items[0].name)
        self.assertEqual(expected_sell_in, gilded_rose.items[0].sell_in)
        self.assertEqual(expected_quality, gilded_rose.items[0].quality)

    def test_foo_quality(self):
        # At the end of each day our system lowers both values for every item
        item_name = "foo"
        items = [Item(item_name, 0, 1)]
        self.assert_update_quality_output(-1, 0, item_name, items)

    def test_foo_quality_expired(self):
        # Once the sell by date has passed, Quality degrades twice as fast
        item_name = "foo"
        items = [Item(item_name, 0, 50)]
        self.assert_update_quality_output(-1, 48, item_name, items)

    def test_foo(self):
        # The Quality of an item is never negative
        item_name = "foo"
        items = [Item(item_name, 0, 0)]
        self.assert_update_quality_output(-1, 0, "foo", items)
        self.assertEqual("foo, -1, 0", repr(items[0]))

    def test_brie(self):
        # "Aged Brie" actually increases in Quality the older it gets
        item_name = "Aged Brie"
        items = [Item(item_name, 0, 0)]
        self.assert_update_quality_output(-1, 2, item_name, items)

    def test_brie_negative_sell_in(self):
        # The Quality of an item is never more than 50
        item_name = "Aged Brie"
        items = [Item(item_name, -1, 50)]
        self.assert_update_quality_output(-2, 50, item_name, items)

    def test_ragnaros(self):
        # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
        item_name = "Sulfuras, Hand of Ragnaros"
        items = [Item(item_name, 0, 1)]
        self.assert_update_quality_output(0, 1, item_name, items)

    def test_TAFKAL80ETC_sell_someday(self):
        # "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_name, 12, 25)]
        self.assert_update_quality_output(11, 26, item_name, items)

    def test_TAFKAL80ETC_sell_soon(self):
        # Quality increases by 2 when there are 10 days or less...
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_name, 9, 25)]
        self.assert_update_quality_output(8, 27, item_name, items)

    def test_TAFKAL80ETC_sell_now(self):
        # Quality increases ... by 3 when there are 5 days or less
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_name, 5, 25)]
        self.assert_update_quality_output(4, 28, item_name, items)

    def test_TAFKAL80ETC_expired(self):
        # Quality drops to 0 after the concert
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_name, 0, 25)]
        self.assert_update_quality_output(-1, 0, item_name, items)


if __name__ == '__main__':
    unittest.main()
