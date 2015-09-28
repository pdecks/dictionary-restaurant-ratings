# your code goes here

def get_rating(filename):
    ratings_file = open(filename)

    restaurant_dict = {}
    for line in ratings_file:
        line = line.strip()
        # print line
        restaurant_pair = line.split(":")
        # print restaurant_pair
        restaurant_dict[restaurant_pair[0]] = restaurant_pair[1]
    # print restaurant_dict

    sorted_restaurants = sorted(restaurant_dict)
    # print sorted_restaurants

    for item in sorted_restaurants:
        print "{} is rated at {}.".format(item, restaurant_dict[item])
    return


get_rating("scores.txt")
# print restaurant_dict