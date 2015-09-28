# your code goes here

def make_restaurant_dict(filename):
    """Opens a file of ratings and converts pairs into a dictionary.
    """
    ratings_file = open(filename)

    restaurant_dict = {}
    for line in ratings_file:
        line = line.strip()
        # print line
        restaurant_pair = line.split(":")
        # print restaurant_pair
        restaurant_dict[restaurant_pair[0]] = restaurant_pair[1]
    # print restaurant_dict

    return restaurant_dict


def print_sorted_restaurants(restaurant_dict):
    """Prints the restaurant pairs in alphabetical order.

    Creates sorted list of restaurant names from dictionary keys, and then
    loops through the dictionary to print the ratings (values).
    """
    sorted_restaurants = sorted(restaurant_dict)
    # print sorted_restaurants

    for item in sorted_restaurants:
        print "{} is rated at {}.".format(item, restaurant_dict[item])

    return

restaurant_dict = make_restaurant_dict("scores.txt")
print_sorted_restaurants(restaurant_dict)
# print restaurant_dict