# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def assert_update_quality_output(self, expected_sell_in, expected_quality, item_name, items):
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(item_name, items[0].name)
        self.assertEqual(item_name, gilded_rose.items[0].name)
        self.assertEqual(expected_sell_in, gilded_rose.items[0].sell_in)
        self.assertEqual(expected_quality, gilded_rose.items[0].quality)

    def test_foo(self):
        item_name = "foo"
        items = [Item(item_name, 0, 0)]
        self.assert_update_quality_output(-1, 0, "foo", items)
        self.assertEqual("foo, -1, 0", repr(items[0]))

    def test_foo_quality(self):
        item_name = "foo"
        items = [Item(item_name, 0, 1)]
        self.assert_update_quality_output(-1, 0, item_name, items)

    def test_foo_high_quality(self):
        item_name = "foo"
        items = [Item(item_name, 0, 50)]
        self.assert_update_quality_output(-1, 48, item_name, items)

    def test_ragnaros(self):
        item_name = "Sulfuras, Hand of Ragnaros"
        items = [Item(item_name, 0, 1)]
        self.assert_update_quality_output(0, 1, item_name, items)

    def test_Ragnaros_expired(self):
        item_name = "Sulfuras, Hand of Ragnaros"
        items = [Item(item_name, -1, 6)]
        self.assert_update_quality_output(-1, 6, item_name, items)

    def test_TAFKAL80ETC_sell_someday(self):
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_name, 12, 25)]
        self.assert_update_quality_output(11, 26, item_name, items)

    def test_TAFKAL80ETC_sell_now(self):
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_name, 5, 25)]
        self.assert_update_quality_output(4, 28, item_name, items)

    def test_TAFKAL80ETC_quality(self):
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_name, 0, 25)]
        self.assert_update_quality_output(-1, 0, item_name, items)

    def test_TAFKAL80ETC_sell_now_maxing_quality(self):
        item_name = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(item_name, 3, 49)]
        self.assert_update_quality_output(2, 50, item_name, items)

    def test_brie(self):
        item_name = "Aged Brie"
        items = [Item(item_name, 0, 0)]
        self.assert_update_quality_output(-1, 2, item_name, items)

    def test_brie_negative_sell_in(self):
        item_name = "Aged Brie"
        items = [Item(item_name, -1, 50)]
        self.assert_update_quality_output(-2, 50, item_name, items)


if __name__ == '__main__':
    unittest.main()
