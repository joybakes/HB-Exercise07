import sys

def setup(userinput):
    f = open(userinput)

    unsorteddata = f.read()
    f.close()
    unsorteddata = unsorteddata.strip().split('\n')

    scores = {}
    for line in unsorteddata:
        restaurant, score = line.split(":")
        scores[restaurant] = score

    return scores

def sort_by_rating(scores):
    backwards = zip(scores.values(), scores.keys())
    backwards.sort()
    for rating, restaurant_name in backwards:
        print "Restaurant %r is rated at %s." % (restaurant_name,rating)


def sort_by_name(scores):
    datalist = scores.items()
    datalist.sort()
    for restaurant_name, rating in datalist:
        print "Restaurant %r is rated at %s." % (restaurant_name,rating)

def find_by_rating(scores, rating):
    for key, value in scores.iteritems():
        if value == rating:
            print "Restaurant %r is rated at %s. \n" % (key, rating)
        else:
            print "No restaurants with that rating.\n"
    

def find_by_name(scores, name):
    # TODO search for restaurant names that contain name
    found_a_restaurant = False

    for restaurant in scores.iterkeys():
        if name in restaurant:
            found_a_restaurant = True
            print "Restaurant %r is rated at %s. \n" % (restaurant, scores[restaurant])

    if found_a_restaurant == False:
        print "Sorry, that restaurant is not found.\n"

userinput = sys.argv[1]
scores = setup(userinput)

while True:
    print "\n" + "*" * 10
    step_1 = raw_input("""Welcome to Restaurant Ratings!
    If you would like to:
    1. Sort by rating
    2. Sort by name
    3. Find by name
    4. Find by rating
    Please choose an option 1-4 or q for Quit.
    > """)

    if step_1 == "1":
        sort_by_rating(scores)
    elif step_1 == "2":
        sort_by_name(scores)
    elif step_1 == "3":
        name = raw_input("What is the name of the restaurant you'd like to find: ")
        find_by_name(scores, name)
    elif step_1 == "4":
        rating = raw_input("What is the restaurant rating you'd like to find: ")
        find_by_rating(scores, rating)
    elif step_1 == "q":
        break
    else:
        print "Sorry, that's not a valid option."

