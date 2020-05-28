import utils

CUSTOMERS_FILE_PATH = "./customers.txt"
OUTPUT_FILE_PATH = "./output.txt"
DUBLIN_OFFICE_LOCATION = (53.339428, -6.257664)
INVITE_DISTANCE_THRESHOLD = 100 # 100 km

customers = utils.load_customers(CUSTOMERS_FILE_PATH)
customers = utils.filter_customers_by_distance_from_location(
    customers,
    DUBLIN_OFFICE_LOCATION,
    INVITE_DISTANCE_THRESHOLD
)
customers = utils.sort_customers_by_user_id(customers)
utils.write_customers(customers, OUTPUT_FILE_PATH)