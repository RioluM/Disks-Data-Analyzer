import unittest
from main import count_disks_per_datacenter, convert_to_days, \
    calculate_datacenters_age_avg, get_broken_disks


class TestDataParsers(unittest.TestCase):

    def test_count_disks_per_datacenter(self):
        datacenter_occurrence = ["first", "second", "second", "third", "first", "first"]
        count_expected = {"first": 3, "second": 2, "third": 1}

        count_result = count_disks_per_datacenter(datacenter_occurrence)
        self.assertEqual(count_expected, count_result)

    def test_convert_to_days(self):
        seconds = 24*60*60 + 200
        expected_days = 1

        result_days = convert_to_days(seconds)

        self.assertEqual(expected_days, result_days)

    def test_calculate_datacenters_age_avg(self):
        datacenter_age_sum = {"first": 30*24*60*60, "second": 40*24*60*60, "third": 10*24*60*60}
        datacenter_quantity = {"first": 5, "second": 8, "third": 2}
        expected_age_avg = {"first": 6, "second": 5, "third": 5}

        result_age_avg = calculate_datacenters_age_avg(datacenter_age_sum, datacenter_quantity)

        self.assertEqual(expected_age_avg, result_age_avg)

    def test_get_broken_disks(self):
        disks_data = [[None, None, "first", None, None, None, None, "1", "2"],
                      [None, None, "second", None, None, None, None, "0", "0"],
                      [None, None, "third", None, None, None, None, "0", "2"]]
        expected_broken_disks = {"first": 3, "third": 2}

        result_broken_disks = get_broken_disks(disks_data)

        self.assertEqual(expected_broken_disks, result_broken_disks)
