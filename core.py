from random import randint, choice
from termcolor import colored, cprint


def get_class():
    classes = [Ninja, SoulReaper, Saiyan]
    class_type = choice(classes)
    return class_type


def damage_finder(a, b):
    d1 = randint(a, b)
    d2 = randint(a, b)
    return min(d1, d2), max(d1, d2)


class Fighter:
    def __init__(self, name, damage_low, damage_high):
        self.health = 100
        self.rage = 0
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high

    def attack(self, other):
        crit_chance = self.rage
        attacks = randint(self.damage_low, self.damage_high)
        crit = False
        if crit_chance >= randint(1, 100):
            crit = True
            attacks *= 2
            other.health = max(other.health - attacks, 0)
            self.rage = 0
            message = 'CRIT Hit for {}!'.format(attacks)
            return message
        else:
            other.health = max(other.health - attacks, 0)
            self.rage = min(100, self.rage + 15)
            message = 'Hit for {}!'.format(attacks)
            return message

    def heal(self):
        message = 'You Do Not Have Enough Rage!'
        if self.rage >= 10:
            self.health = min(self.health + 5, 100)
            self.rage = max(self.rage - 10, 0)
            message = 'You Healed +5'
        return message

    def is_dead(self):
        if self.health <= 0:
            return True
        return False

    def __str__(self):
        return 'Fighter:{}| Health: {}| Rage: {}| Damage_Low: {}| Damage_High: {}!'.format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    def __repr__(self):
        return 'Fighter:{}|Health:{}|Rage:{}!'.format(self.name, self.health,
                                                      self.rage)

    def get_choice(self, other, decision):
        if decision.title().strip() == 'a'.title().strip():
            message = self.attack(other)
            return message
        elif decision.title().strip() == 'h'.title().strip():
            message = self.heal()
            return message
        elif decision.title().strip() == 't'.title().strip():
            message = self.transform()
            return message
        elif decision.title().strip() == 's'.title().strip():
            message = self.skip()
            return message
        elif decision.title().strip() == 'j'.title().strip():
            message = self.jutsu(other)
            return message
        elif decision.title().strip() == 'r'.title().strip():
            message = self.hollow_form()
            return message

    def skip(self):
        self.rage += 30
        message = 'You Succesfully Skipped'
        return message


class Saiyan(Fighter):
    def __init__(self, name, damage_low, damage_high):
        self.health = 100
        self.rage = 60
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.action_string = colored(
            '-- [a]ttack\n-- [h]eal-*Must Have 10 Rage\n-- [t]ransform-*Must Have 80 Rage\n-- [s]kip-*Adds 30 Rage\n>>>',
            'red')

    def __str__(self):
        return 'Saiyan {}| Health: {}| Rage: {}| Damage_Low: {}| Damage_High: {}!'.format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    def __repr__(self):
        return 'Saiyan {}| Health: {}| Rage: {}!'.format(
            self.name, self.health, self.rage)

    def transform(self):
        message = 'You Do Not Have Enough Rage!'
        if self.rage >= 80:
            self.health += 20
            self.damage_high += 10
            self.damage_low += 10
            self.rage = 20
            message = 'Wow That Is A New Level'
            return message
        return message

    def possible_actions(self):
        actions = ['a', 's']
        if self.rage >= 10:
            actions.append('h')
        if self.rage >= 40:
            actions.append('t')
        return actions


class Ninja(Fighter):
    def __init__(self, name, damage_low, damage_high):
        self.health = 100
        self.rage = 20
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.action_string = colored(
            '-- [a]ttack\n-- [h]eal-*Must Have 10 Rage\n-- [j]utsu-*Must Have 50 Rage\n-- [s]kip-*Adds 30 Rage\n>>>',
            'red')

    def __str__(self):
        return 'Ninja {}| Health: {}| Rage: {}| Damage_Low: {}| Damage_High: {}!'.format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    def __repr__(self):
        return 'Ninja {}| Health: {}| Rage: {}!'.format(
            self.name, self.health, self.rage)

    def jutsu(self, other):
        message = 'You Do Not Have Enough Rage!'
        if self.rage >= 50:
            self.health += 5
            self.damage_high += 15
            self.damage_low += 5
            self.rage = 10
            other.health -= self.damage_high
            message = 'Your Jutsu Took {} Damage!!'.format(self.damage_high)
            return message
        return message

    def possible_actions(self):
        actions = ['a', 's']
        if self.rage >= 10:
            actions.append('h')
        if self.rage >= 50:
            actions.append('j')
        return actions


class SoulReaper(Fighter):
    def __init__(self, name, damage_low, damage_high):
        self.health = 100
        self.rage = 25
        self.name = name
        self.damage_low = damage_low
        self.damage_high = damage_high
        self.action_string = colored(
            '-- [a]ttack\n-- [h]eal-*Must Have 10 Rage\n-- [r]ampage-*Health Has To Be 25 or Lower\n-- [s]kip-*Adds 30 Rage\n>>>',
            'red')

    def __str__(self):
        return 'SoulReaper {}| Health: {}| Rage: {}| Damage_Low: {}| Damage_High: {}!'.format(
            self.name, self.health, self.rage, self.damage_low,
            self.damage_high)

    def __repr__(self):
        return 'SoulReaper {}| Health: {}| Rage: {}!'.format(
            self.name, self.health, self.rage)

    def hollow_form(self):
        message = 'The Hollow Can Not Take Over'
        if self.health <= 25:
            self.health += 30
            self.rage += 20
            self.damage_high += 10
            self.damage_low += 5
            message = 'You Are Now On A Rampage!!!'
        return message

    def possible_actions(self):
        actions = ['a', 's']
        if self.rage >= 10:
            actions.append('h')
        if self.rage <= 25:
            actions.append('r')
        return actions