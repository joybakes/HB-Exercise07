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
        print "\n Restaurant %r is rated at %s.\n" % (restaurant_name,rating)


def sort_by_name(scores):
    datalist = scores.items()
    datalist.sort()
    for restaurant_name, rating in datalist:
        print "\n Restaurant %r is rated at %s.\n" % (restaurant_name,rating)

def find_by_rating(scores, rating):
    found_a_rating = False
    for key, value in scores.iteritems():
        if value == rating:
            found_a_rating = True
            print "\n Restaurant %r is rated at %s. \n" % (key, rating)
    
    if found_a_rating == False:
        print "\n No restaurants with that rating.\n"
    

def find_by_name(scores, name):
    # TODO search for restaurant names that contain name
    found_a_restaurant = False

    for restaurant in scores.iterkeys():
        if name.lower() in restaurant.lower():
            found_a_restaurant = True
            print "\n Restaurant %r is rated at %s. \n" % (restaurant, scores[restaurant])

    if found_a_restaurant == False:
        print "\n Sorry, that restaurant is not found.\n"

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

    # Sort by rating
    if step_1 == "1":
        sort_by_rating(scores)
    
    # Sort by name
    elif step_1 == "2":
        sort_by_name(scores)
    
    # Find by Name
    elif step_1 == "3":
        name = raw_input("What is the name of the restaurant you'd like to find: \n>")
        find_by_name(scores, name)
    
    # Find by Rating
    elif step_1 == "4":
        rating = raw_input("What is the restaurant rating you'd like to find: \n>")
        if rating != "0":
            find_by_rating(scores, rating)
        else:
            print "\n You don't want to eat at those restaurants. Trust me."
    # monkey easter egg
    elif step_1 == "monkeys":
        print "While monkeys are amazing chefs, they are not legally allowed to own restaurants."
    
    # Quit the program
    elif step_1 == "q":
        break

    # Handle those who can't follow instructions 
    else:
        print "Sorry, that's not a valid option."

