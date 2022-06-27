# More or less just a digital play area to mess around with python functions, objects, etc


# Let's have fun. Let's make a frankly absurd amount of objects based on super heroes and whatever else comes to mind.


from ctypes import alignment


class earth_defender:
    alignment = "Good"

# Power Rangers classes


class morphin_grid_user(earth_defender):
    def __init__(self, name, planet, powers):
        self.name = name
        self.planet = planet
        self.powers = powers


class ranger(morphin_grid_user):
    def __init__(self, name, color, zord, weapon, city):
        self.name = name
        self.color = color
        self.zord = zord
        self.weapon = weapon
        self.city = city

    def morph(self):
        print(self.zord + "!")

    def catchphrase(self):
        print("Go Go Power Rangers!")

    def zord(self):
        print("We need Dinozord power, now!")

    def megazord(self):
        print("We need Megazord Power, now!")


jason = ranger("Jason Lee Scott", "Red", "Tyrannosaurus",
               "Power Sword", "Angel Grove")
kimberly = ranger('Kimberly Hart', "Pink", "Pterodactyl",
                  "Power Bow", "Angel Grove")
trini = ranger("Trini Kwan", "Yellow", "Sabretooth Tiger",
               "Power Daggers", "Angel Grove")
zack = ranger("Zack Taylor", "Black", "Mastodon", "Power Axe", "Angel Grove")
billy = ranger("Billy Cranston", "Blue", "Triceratops",
               "Power Lance", "Angel Grove")
tommy = ranger("Tommy Oliver", "Green", 'Dragonzord',
               'Dragon Dagger', "Angel Grove")

# DC classes


class jla_member(earth_defender):
    def __init__(self, name, alter_ego, city, powers):
        self.name = name
        self.alter_ego = alter_ego
        self.city = city
        self.powers = powers


class kryptonian:
    powers = "flight, super speed, x-ray vision, heat vision, super strength"
    planet = "Krypton"


class supermen(jla_member, kryptonian):
    pass

class green_lantern:
    weapon = "Power Ring"
    powers = "flight, energy projection, energy construct creation"
    motto = "\tIn Brightest Day\n\tIn Blackest Night\n\tNo Evil Shall Escape My Sight\n\tLet Those Who Worship Evil's Might\n\tBeware My Power\n\tGreen Lantern's Light!"

class earth_lantern(jla_member, green_lantern):
    pass


batman = jla_member("Batman", "Bruce Wayne", "Gotham City",
                    "World's Greatest Detective, intense physical training, scientist, billionaire")
superman = supermen("Superman", "Clark Kent", "Metropolis", kryptonian.powers)
supergirl = supermen("Supergirl", "Kara Zor-El", "Metropolis", kryptonian.powers)
hal_jordan = earth_lantern("Green Lantern", "Hal Jordan", "Coast City", green_lantern.powers)

# Marvel Classes


class avenger(earth_defender):
    def __init__(self, name, alter_ego, city, powers):
        self.name = name
        self.alter_ego = alter_ego
        self.city = city
        self.powers = powers

iron_man = avenger("Iron Man", "Tony Stark", "New York", "Iron man suit, billionare, genius, philanthropist")
captain_america = avenger("Captain America", "Steve Rogers", "Queens", "super soldier serum, super strength, endurance")

# Lets have fun

print(kimberly.name)
tommy.morph()
print(batman.powers)
print(superman.powers)
print(hal_jordan.motto)

# Let's actually do something now. A list of objects

rangerlist = [jason, tommy, trini, kimberly, zack, billy]
dclist = [superman, batman, supergirl, hal_jordan]
marvellist = [iron_man, captain_america]

def namefunc(listname):
    for fighter in listname:
        print(fighter.name)

namefunc(rangerlist)
namefunc(dclist)