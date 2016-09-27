states = {
    "Oregon":"OR",
    "New York":"NY",
    "Iowa":"IA",
    "Florida":"FL",
    "California":"CA"
}

cities = {
    "IA":"Des Moines",
    "CA":"San Francisco",
    "FL":"Tampa",
}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print "-" *10
print "New York has:", cities["NY"]
print "Oregon has:", cities["OR"]

print "-" * 10
print "Iowa's abbreviation is:", states["Iowa"]
print "Florida's abbreviation is:", states["Florida"]

print "-" * 10
print "California has:", cities[states["Florida"]]
print "Oregon has:", cities[states["Oregon"]]

print "-" * 10
for state, abbrev in states.items():
    "%s has the city %s" % (state, abbrev)

print "-" * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, state)

print "-" * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s and has city %s" % (state, abbrev, cities[abbrev])

print "-" * 10
states = states.get("TX")

if not state:
    print "Sorry, no Texas"

cities = cities.get("TX", "Does not exist")
print "The city for the state of 'TX' is %s" % city