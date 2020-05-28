import pytest
import utils
import unittest

class UtilsTestCase(unittest.TestCase):

    def test_when_loading_customers_correct_shape_is_loaded(self):
        expected_shape = (2, 5)
        customers = utils.load_customers("./test_fixtures/customers.txt")
        assert(customers.shape == expected_shape)

    def test_distance_between_locatons_is_correctly_calculated(self):
        location_a = ()
        location_b = ()

        expected_distance = 0
        distance = utils.calculate_distance_between_locations(location_a, location_b)
        assert(expected_distance)

    # def filter_customers_by_distance_from_location(customers, location, distance):
    #     """
    #     This function filters the list of custoemrs to those within a set distance
    #     from the location
    #     """
    #     customers = generate_distance_from_location_for_customers(customers, location)
    #     in_range = (customers['distance'] <= distance)

    #     return customers[in_range]

    # def generate_distance_from_location_for_customers(customers, location):
    #     """
    #     This function generates a column with the distances from the location for each customer
    #     """

    #     distances = [generate_distance_from_location_for_customer(row, location) for index, row in customers.iterrows()]
    #     customers['distance'] = distances

    #     return customers

    # def generate_distance_from_location_for_customer(customer, location):
    #     """
    #     This function generates a distance from the location for a single customer
    #     """
    #     latitude = customer['latitude']
    #     longitude = customer['longitude']

    #     customer_location = (latitude, longitude)
        
    #     return calculate_distance_between_locations(customer_location, location)

    # def sort_customers_by_user_id(customers):
    #     """
    #     This function sorts the list of customers by the user_id column
    #     """
    #     return customers.sort_values('user_id')