import pytest
import utils
import unittest

class UtilsTestCase(unittest.TestCase):

        
    # def load_customers(customer_data_path):
    #     """
    #     This function is responsible for loading the customers.txt
    #     and teturning the data using pandas.
    #     """
    #     f = open(customer_data_path, "r")
    #     return pandas.read_json(f, lines=True)

    # def write_customers(customers, output_data_path):
    #     """
    #     This function is responsible for wriiting the output.txt
    #     """
    #     customers.to_json(output_data_path, 'records', lines=True)

    # def calculate_distance_between_locations(location_a, location_b):
    #     """
    #     Calculates and returns the distance between two locations in km
    #     """
    #     lat_a, lon_a = map(radians, location_a)
    #     lat_b, lon_b = map(radians, location_b)

    #     angle = acos(
    #         sin(lat_a) * sin(lat_b) +
    #         cos(lat_a) * cos(lat_b) *
    #         cos(lon_a - lon_b)
    #     )

    #     return EARTH_RADIUS * angle

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