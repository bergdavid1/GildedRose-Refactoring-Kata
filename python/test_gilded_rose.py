# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def assert_update_item(self, item_name, initial_sell_in, initial_quality, expected_sell_in, expected_quality):
        # All items have a SellIn value which denotes the number of days we have to sell the item
        # All items have a Quality value which denotes how valuable the item is
        items = [Item(item_name, initial_sell_in, initial_quality)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual(item_name, items[0].name)
        self.assertEqual(item_name, gilded_rose.items[0].name)
        self.assertEqual(
            "{}, {}, {}".format(item_name, expected_sell_in, expected_quality),
            repr(items[0])
        )

        self.assertEqual(expected_sell_in, gilded_rose.items[0].sell_in)
        self.assertEqual(expected_quality, gilded_rose.items[0].quality)

    def test_foo_quality(self):
        # At the end of each day our system lowers both values for every item
        item_name = "foo"
        sell_in = 0
        quality = 1
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality-1)

    def test_foo_quality_expired(self):
        # Once the sell by date has passed, Quality degrades twice as fast
        item_name = "foo"
        sell_in = 0
        quality = 50
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality-2)

    def test_foo(self):
        # The Quality of an item is never negative
        item_name = "foo"
        sell_in = 0
        quality = 0
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality)

    def test_brie(self):
        # "Aged Brie" actually increases in Quality the older it gets
        item_name = "Aged Brie"
        sell_in = 0
        quality = 0
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality+2)

    def test_brie_negative_sell_in(self):
        # The Quality of an item is never more than 50
        item_name = "Aged Brie"
        sell_in = -1
        quality = 50
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality)

    def test_ragnaros(self):
        # "Sulfuras", being a legendary item, never has to be sold or
        # decreases in Quality
        item_name = "Sulfuras, Hand of Ragnaros"
        sell_in = 0
        quality = 1
        self.assert_update_item(item_name, sell_in, quality, sell_in, quality)

    def test_ragnaros_high_quality_allowed(self):
        # "Sulfuras", being a legendary item, never has to be sold or
        # decreases in Quality

        # Just for clarification, an item can never have its Quality increase
        # above 50, however "Sulfuras" is a legendary item and as such its
        # Quality is 80 and it never alters.
        item_name = "Sulfuras, Hand of Ragnaros"
        sell_in = 0
        quality = 80
        self.assert_update_item(item_name, sell_in, quality, sell_in, quality)

    def test_TAFKAL80ETC_sell_someday(self):
        # "Backstage passes", like aged brie, increases in Quality as its SellIn value approaches;
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        sell_in = 12
        quality = 25
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality + 1)

    def test_TAFKAL80ETC_sell_soon(self):
        # Quality increases by 2 when there are 10 days or less...
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        sell_in = 9
        quality = 25
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality + 2)

    def test_TAFKAL80ETC_sell_now(self):
        # Quality increases ... by 3 when there are 5 days or less
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        sell_in = 5
        quality = 25
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality + 3)

    def test_TAFKAL80ETC_expired(self):
        # Quality drops to 0 after the concert
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        sell_in = 0
        quality = 25
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, 0)

    def test_conjured_item1_normal(self):
        # "Conjured" items degrade in Quality twice as fast as normal items
        item_name = "Conjured Item1"
        sell_in = 10
        quality = 25
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality-2)

    def test_conjured_item2_expired(self):
        # "Conjured" items degrade in Quality twice as fast as normal items
        item_name = "Conjured Item2"
        sell_in = -2
        quality = 39
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, quality-4)

    def test_conjured_item3_min_quality(self):
        # "Conjured" items degrade in Quality twice as fast as normal items
        item_name = "Conjured Item3"
        sell_in = -1
        quality = 3
        self.assert_update_item(item_name, sell_in, quality, sell_in-1, 0)


if __name__ == '__main__':
    unittest.main()
