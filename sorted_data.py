import sys

userinput = sys.argv[1]
f = open(userinput)

unsorteddata = f.read()
f.close()
unsorteddata = unsorteddata.strip().split('\n')

scores = {}
for line in unsorteddata:
    restaurant, score = line.split(":")
    scores[restaurant] = score

sorteddata = scores.items()
sorteddata.sort()

for restaurant_name, rating in sorteddata:
    print "Restaurant %r is rated at %s." % (restaurant_name,rating)