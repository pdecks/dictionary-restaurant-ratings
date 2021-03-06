# your code goes here
import random

def get_user_review(restaurant_dict):
    """Prompts the user to enter a new restaurant rating pair.
    """

    print "Enter the name of the restaurant you'd like to review:"
    rest_entry = raw_input("> ")

    print "Enter a rating from 1 to 5:"
    rating_entry = int(raw_input("> "))

    user_entered_pair = (rest_entry, rating_entry)
    add_user_review(user_entered_pair, restaurant_dict)

    print restaurant_dict
    return
     # (rest_entry, rating_entry)


def add_user_review(user_entered_pair, restaurant_dict):
    """Takes a tuple from user and converts into dictionary entry.
    """    
    restaurant_dict[user_entered_pair[0]] = user_entered_pair[1]

    return restaurant_dict


def updates_random_entry(restaurant_dict):
    """Ask user for new rating for random restaurant in dictionary.
    """
    print "Hello. What is your name?"
    user_name = raw_input("> ")
    sorted_restaurants = sorted(restaurant_dict)
    rand_rest = sorted_restaurants[random.randint(0,len(sorted_restaurants))]
    print "Thanks, {}. Let's update the rating for {}.".format(user_name, rand_rest)
    print "Enter a rating from 1 to 5:"
    new_rating = raw_input("> ")
    restaurant_dict[rand_rest] = new_rating

    return

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

# get_user_review(restaurant_dict)
updates_random_entry(restaurant_dict)

print restaurant_dict