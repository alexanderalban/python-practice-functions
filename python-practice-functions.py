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


jason = ranger("Jason Lee Scott", "Red", "Tyrannosaurus", "Power Sword", "Angel Grove")
kimberly = ranger('Kimberly Hart', "Pink", "Pterodactyl", "Power Bow", "Angel Grove")
trini = ranger("Trini Kwan", "Yellow", "Sabretooth Tiger", "Power Daggers", "Angel Grove")
zack = ranger("Zack Taylor", "Black", "Mastodon", "Power Axe", "Angel Grove")
billy = ranger("Billy Cranston", "Blue", "Triceratops", "Power Lance", "Angel Grove")
tommy = ranger("Tommy Oliver", "Green", 'Dragonzord', 'Dragon Dagger', "Angel Grove")

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

batman = jla_member("Batman", "Bruce Wayne", "Gotham City", "World's Greatest Detective, intense physical training,, scientist, billionaire")
superman = supermen("Superman", "Clark Kent", "Metropolis", kryptonian.powers)

# Marvel Classes


class avenger(earth_defender):
    def __init__(self, name, alter_ego, city, powers):
        self.name = name
        self.alter_ego = alter_ego
        self.city = city
        self.powers = powers


# Lets have fun

print(kimberly.name)
tommy.morph()
print(batman.powers)
print(superman.powers)