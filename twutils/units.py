"""
    units.py
    a module that contains helper functions for the browser game tribalwars
"""
import worldConfig


class Troop(object):
    """
        provides unit related functions
    """

    def __init__(self):
        self.unit_config = worldConfig.WorldConfig()
        self.world_config = self.unit_config.get_world_config()

        self.spear = self.unit_config.get_specific_unit_config('spear')
        self.sword = self.unit_config.get_specific_unit_config('sword')
        self.axe = self.unit_config.get_specific_unit_config('axe')
        if self.world_config.is_archer_world():
            self.archer = self.unit_config.get_specific_unit_config('archer')
            self.marcher = self.unit_config.get_specific_unit_config('marcher')
        self.spy = self.unit_config.get_specific_unit_config('spy')
        self.light = self.unit_config.get_specific_unit_config('light')
        self.heavy = self.unit_config.get_specific_unit_config('heavy')
        self.ram = self.unit_config.get_specific_unit_config('ram')
        self.cat = self.unit_config.get_specific_unit_config('cat')
        if self.world_config.paladin_active():
            self.knight = self.unit_config.get_specific_unit_config('knight')
        self.snob = self.unit_config.get_specific_unit_config('snob')
        self.unit_stats = dict(spear=self.spear, sword=self.sword, axe=self.axe,
                               archer=self.archer, spy=self.spy,
                               light=self.light, marcher=self.marcher,
                               heavy=self.heavy, ram=self.ram, cat=self.cat,
                               knight=self.knight, snob=self.snob)

    def get_unit_stats(self, unit_name):
        """

        :param unit_name: the name of the unit to return the stats for
        :return: :rtype: the stats of the requested unit:dict
        """
        try:
            if unit_name in self.unit_stats:
                return self.unit_stats[unit_name]
        except KeyError, err:
            print err
            return KeyError



