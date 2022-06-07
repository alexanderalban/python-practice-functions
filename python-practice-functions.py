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
    def __init__(self, name, color, zord, weapon):
        self.name = name
        self.color = color
        self.zord = zord
        self.weapon = weapon

    def morph(self):
        print(self.zord + "!")

    def catchphrase(self):
        print("Go Go Power Rangers!")


jason = ranger("Jason Lee Scott", "Red", "Tyrannosaurus", "Power Sword")
kimberly = ranger('Kimberly Hart', "Pink", "Pterodactyl", "Power Bow")
trini = ranger("Trini Kwan", "Yellow", "Sabretooth Tiger", "Power Daggers")
zack = ranger("Zack Taylor", "Black", "Mastodon", "Power Axe")
billy = ranger("Billy Cranston", "Blue", "Triceratops", "Power Lance")
tommy = ranger("Tommy Oliver", "Green", 'Dragonzord', 'Dragon Dagger')

# DC classes


class jla_member(earth_defender):
    def __init__(self, name, alter_ego, powers):
        self.name = name
        self.alter_ego = alter_ego
        self.powers = powers

# Marvel Classes


class avenger(earth_defender):
    def __init__(self, name, alter_ego, powers):
        self.name = name
        self.alter_ego = alter_ego
        self.powers = powers


# Lets have fun

print(kimberly.name)
tommy.morph()
print(billy.alignment)
