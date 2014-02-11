import sys


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
            print "Restaurant %r is rated at %s" % (key, rating)
    

def find_by_name(scores, name):
    if scores.get(name):
        print "Restaurant %r is rated at %s." % (name, scores[name])
    else:
        print "Sorry, that restaurant is not found."


userinput = sys.argv[1]
step_1 = raw_input("""Welcome to Restaurant Ratings!
If you would like to
sort by rating, press 1
sort by name, press 2.
find by name, press 3.
find by rating, press 4.
quit, press q""")

if step_1 == "1":
    pass
elif step_1 == "2":
    pass
elif step_1 == "3":
    pass
elif step_1 == "4":
    pass
elif step_1 == "q":
    break
else:
    print "Sorry, that's not a valid option."

f = open(userinput)

unsorteddata = f.read()
f.close()
unsorteddata = unsorteddata.strip().split('\n')

scores = {}
for line in unsorteddata:
    restaurant, score = line.split(":")
    scores[restaurant] = score




