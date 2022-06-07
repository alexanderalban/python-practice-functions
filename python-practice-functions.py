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
red_ranger = ranger("Jason Lee Scott", "Red", "Tyrannosaurus", "Power Sword")

print(red_ranger.name)
