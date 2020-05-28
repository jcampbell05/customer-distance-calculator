import pytest
import utils
import unittest

class UtilsTestCase(unittest.TestCase):

    def test_when_loading_customers_correct_shape_is_loaded(self):
        expected_shape = (2, 5)
        customers = utils.load_customers("./test_fixtures/customers.txt")
        assert(customers.shape == expected_shape)

    def test_distance_between_locatons_is_correctly_calculated(self):
        location_a = (53.339428, -6.257664) # Dublin
        location_b = (51.903614, -8.468399) # Cork

        expected_distance = 218
        distance = utils.calculate_distance_between_locations(location_a, location_b)
        assert(int(distance) == expected_distance)

    def test_when_customers_filtered_by_distance_shape_should_be_correct(self):
        expected_shape = (0, 5)
        location = (53.339428, -6.257664) # Dublin

        customers = utils.load_customers("./test_fixtures/customers.txt")
        customers = utils.filter_customers_by_distance_from_location(customers, location, 0)

        assert(customers.shape == expected_shape)

    def test_when_customers_sorted_by_id_customers_should_be_in_correct_order(self):

        expected_user_ids = [4, 5]

        customers = utils.load_customers("./test_fixtures/customers.txt")
        customers = utils.sort_customers_by_user_id(customers)
        user_ids = list(customers['user_id'])

        assert(user_ids == expected_user_ids)