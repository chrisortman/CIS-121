print "Enter your numbers:"
# wood = int(input("Wood: "))
# meat = raw_input("Meat: ")
# leather = raw_input("Leather: ")
# iron = raw_input("Iron: ")
# fur = raw_input("Fur: ")
# cured = raw_input("Cured Mead: ")
# bait = raw_input("Bait: ")

g = int(input('Gatherer: '))
c = int(input('Charcurier: '))
h = int(input('Hunter: '))
i = int(input('Iron Miner: '))
n = int(input('Tanner: '))
t = int(input('Trapper: '))

#builder gives you an automatic +2 wood per 10s
wood = 2.0
meat = 0.0
leather = 0.0
iron = 0.0
fur = 0.0
cured = 0.0
bait = 0.0

def gatherer():
    global wood
    wood += 1
    
def charcutier():
    global meat
    global cured
    global wood
    meat -= 5
    wood -= 5
    cured += 1
    
def hunter():
    global fur 
    global meat
    fur += 0.5
    meat += 0.5
    
def iron_miner():
    global cured
    global iron
    cured -= 1
    iron += 1
    
def tanner():
    global fur
    global leather
    fur -= 5
    leather += 1
    
def trapper():
    global meat
    global bait
    meat -= 1
    bait += 1
    
for num in range(g):
    gatherer()
    
for num in range(c):
    charcutier()
    
for num in range(h):
    hunter()
    
for num in range(i):
    iron_miner()
    
for num in range(n):
    tanner()
    
for num in range(t):
    trapper()

print "%r wood per 10s" % wood
print "%r meat per 10s" % meat
print "%r leather per 10s" % leather
print "%r iron per 10s" % iron
print "%r fur per 10s" % fur
print "%r cured meat per 10s" % cured
print "%r bait per 10s" % bait