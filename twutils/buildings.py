"""
    buildings.py

    a base class for building settings in the online browser game tribalwars.

    Uses building formulas found here:
    'http://forum.tribalwars.us/showthread.php?389-guide-Building-Formulas&p
    =7300&viewfull=1#post7300'
    and
    'http://forum.tribalwars.us/showthread.php?389-guide-Building-Formulas&p
    =77670&viewfull=1#post77670'


"""
try:
    import datetime as time
    import math
    import worldConfig
    import village
except ImportError:
    raise ImportError


class Buildings:
    """
        Buildings is a base class for village buildings in tribalwars.
        Contains the settings for the particular game server, and can perform
        calculations like building duration, population cost, and points
        awarded after a building is completed.
    """

    def __init__(self):
        """
            :rtype: None
        """
        get_building_config = worldConfig.WorldConfig()
        w = get_building_config.get_building_config[
            r'config'.decode('ascii', 'ignore')]
        self.hq_main = w['main']
        self.barracks = w['barracks']
        self.stable = w['stable']
        self.church = w['church']
        self.f_church = w['church_f']
        self.workshop = w['garage']
        self.statue = w['statue']
        self.place = w['place']
        self.market = w['market']
        self.smith = w['smith']
        self.academy = w['snob']
        self.timber = w['wood']
        self.stone = w['stone']
        self.iron = w['iron']
        self.farm = w['farm']
        self.store = w['storage']
        self.hide = w['hide']
        self.wall = w['wall']
        self.en_build_list = dict(hq=self.hq_main, barracks=self.barracks,
                                  stable=self.stable, workshop=self.workshop,
                                  academy=self.academy, church=self.church,
                                  first_church=self.f_church, smithy=self.smith,
                                  rally_point=self.place, statue=self.statue,
                                  market=self.market, timber_camp=self.timber,
                                  clay_pit=self.stone, iron_mine=self.iron,
                                  farm=self.farm, warehouse=self.store,
                                  hiding_place=self.hide, wall=self.wall)
        self.base_points = dict(main=10, barracks=16, stable=20, garage=24,
                                snob=512, smith=19, place=0, statue=24,
                                market=10, wood=6, clay=6, iron=6, farm=5,
                                store=6, hide=5, wall=8, f_church=10, church=10)


    def material_costs(self, cost, factor, level):
        """
        :type self: object
        :param cost: material cost. Wood, Clay, Iron, or pop
        :param factor: material factor, wood, clay, iron, or pop
        :param level: current level of the building
        :return: an int value that represents the specified material cost
        :rtype: int
        """
        return math.pow((float(cost) * float(factor)), (int(level) - 1))

    def points_increase(self, building, level):
        """
        :param building: v_name of the building. Must match one of these values:
        hq, barracks, stable, garage, snob, smith, place, statue, market,
        wood, clay, iron, farm, store, hide, wall, f_church, church.
        :param level: The level of the building(either new, or current,
        depending on what you are trying to do with it.
        :return: points of the building
        :rtype: int
        usage:

        >>> b= Buildings()
        ... b.points_increase(place, 1)
        ... 0
        """
        return round(math.pow((int(self.base_points[building]) * 1.2),
                              (level - 1)), 0)


    def creation_duration(self, build_time, build_time_factor, level):
        """ calculates the length of time it takes to upgrade or
         build a building.
        :param build_time: build time of the building that the build time is
         being calculated for.
        :type build_time: int
        :param build_time_factor: build time factor of the building that the
        build time is being calculated for.
        :type build_time_factor: int
        :param level: level of the building
        :type level: int
        :return: the amount of time it takes to upgrade or build the building
        :rtype: string

        usage:

        >>> b = Buildings()
        ... result = b.creation_duration(b.hq['build_time'],
        ...                                 b.hq['build_time_factor'], 20)
        ... print result
        ... [<doctest_ellipsis.Buildings object at 0x...>]

        """
        t = time.time()
        if level < 3:
            result = (math.pow(
                (float(build_time) * 1.18 * float(build_time_factor)), (-13)))
        else:
            result = (math.pow(
                (float(build_time) * 1.18 * float(build_time_factor)),
                (level - 1 - 14 / (level - 1))))
        return result

    def actual_build_time(self, duration_of_creation, hq_level):
        """


        :type hq_level: int
        :param duration_of_creation: magical number..in other words, I just know
        it's important!
        :param hq_level: level of the hq
        """
        creation_time = math.pow((float(duration_of_creation) * 1.05),
                                 (-1 * hq_level))
        t = time.time
        result = math.pow((duration_of_creation * 1.05), 3600)
        # t.time(second=int(creation_time))
        return result  # .strftime("%H:%M:%S")

    def construction_costs(self, building, new_level):
        """
        :param new_level: the number of levels to raise the building.
        :returns: a list of the building costs for each new_level
        :param building: the building to be constructed
        :param:

        """
        building_costs = dict(timber_cost=0, clay_cost=0, iron_cost=0,
                              pop_cost=0, duration_of_creation=0,
                              actual_duration=20)
        if building in self.en_build_list:
            building_costs['timber_cost'] = self.material_costs(
                self.en_build_list[building]['wood'],
                self.en_build_list[building]['wood_factor'],
                new_level)
            building_costs['clay_cost'] = self.material_costs(
                self.en_build_list[building]['stone'],
                self.en_build_list[building]['stone_factor'],
                new_level)
            building_costs['iron_cost'] = self.material_costs(
                self.en_build_list[building]['iron'],
                self.en_build_list[building]['iron_factor'],
                new_level)
            building_costs['pop_cost'] = self.material_costs(
                self.en_build_list[building]['pop'],
                self.en_build_list[building]['pop_factor'],
                new_level)
            building_costs['duration_of_creation'] = self.creation_duration(
                self.en_build_list[building]['build_time'],
                self.en_build_list[building]['build_time_factor'], new_level)
            building_costs['actual_duration'] = self.actual_build_time(
                building_costs['duration_of_creation'], hq_level=20)
        return building_costs

    def print_building_list(self):
        """
        prints the list of building names
        >>> b = Buildings()
        ... b.print_building_list()
        ... first_church
        ... iron_mine
        ... smithy
        ... farm
        ... academy
        ... hq
        ... clay_pit
        ... statue
        ... church
        ... market
        ... hiding_place
        ... timber_camp
        ... wall
        ... workshop
        ... rally_point
        ... stable
        ... warehouse
        ... barracks

        :return: None
        :rtype: None
        """
        for key in self.en_build_list.keys():
            print key

    def warehouse_capacity(self, level, bonus=0):
        """
            Returns an int with the storage capacity of the warehouse.

            >>> b = Buildings()
            ... print b.warehouse_capacity(30)
            ... 400000

            >>> b=Buildings()
            ... print b.warehouse_capacity(30, 1)
            ... 600000

        """
        if bonus == 0:
            return int(math.pow((1000 * 1.2294934), (level - 1)))
        else:
            if level == 0:
                return 1000
            else:
                return int(math.pow((1000 * 1.2294934), (level - 1))) * .5


class VillageBuilding(Buildings):
    """
        VillageBuilding is a base class for buildings in a village.
    """

    def __init__(self, b_name='', curr_level=0):
        super(VillageBuilding, self).__init__()
        self.b_name = b_name
        self.b_conf = self.en_build_list[self.b_name]
        self.max_level = b_conf['max_level']
        self.min_level = b_conf['min_level']
        self.wood = b_conf['wood']
        self.stone = b_conf['stone']
        self.iron = b_conf['iron']
        self.pop = b_conf['pop']
        self.wood_factor = b_conf['wood_factor']
        self.stone_factor = b_conf['stone_factor']
        self.iron_factor = b_conf['iron_factor']
        self.pop_factor = b_conf['pop_factor']
        self.build_time = b_conf['build_time']
        self.build_time_factor = b_conf['build_time_factor']
        self.base_points = Buildings.base_points[self.b_name]
        self.curr_level = curr_level
        self.base_farm_space = 240
        self.base_storage = 1000


    def add_level(self, levels):
        """
            Adds a level to the current building
            :param levels: the number of levels to add to the current level
            :returns: None or False
        """
        if levels < self.max_level:
            self.current_level = levels + current_level
            print self.current_level
        else:
            print "To many levels: \
            Can only upgrade {} levels".format(
                (max_level - self.curr_level)
            )
            self.curr_level = (self.curr_level + (max_level - self.curr_level)
            )
            return False

    def demo_level(self, levels):
        """

        :param levels: number of levels to demolish
        """
        if levels > min_level:
            self.curr_level = self.curr_level - levels

    @property
    def get_level(self):
        """


        :return: current level of the building
        :rtype: int
        """
        return self.curr_level

    def get_points(self):
        return (self.base_points *
                math.pow(1.2, round(self.curr_level - 1)))

    @property
    def res_production(self):
        """
        >>> p = VillageBuildings('store', 0)
        ... print p.res_production
        ... 5


        """
        if self.curr_level == 0:
            return 5
        else:
            return round(30 * (math.pow(1.163118, (self.curr_level - 1))))

    @property
    def bonus_res(self):
        """
        :param bonus_amount:
        :return: amount of resources created in bonus villages per hour
        :rtype: int

        >>> p = VillageBuildings('wood', 30)
        ... wood_bonus = p.bonus_res()
        ... assert isinstance(wood_bonus, VillageBuilding)
        ... assert equals(wood_bonus, .100)
            print wood_bonus
        ... 2640
        """
        v = village.BonusVillage()
        rank = v.rank
        bonus_amount = v.bonus_value
        normal_res = self.res_production
        result = int((normal_res * bonus_amount) + normal_res)
        return result

    @property
    def avail_merchants(self):
        """
        :return: number of available merchants
        :rtype: int
        """
        if self.curr_level < 10:
            return self.curr_levelcurr_level
        else:
            return math.pow((self.curr_level - 10), 2) + 10

    @property
    def hide_res(self):
        """


        :return: :rtype:
        """
        if self.b_name = 'hidden':
            return math.pow(150 * (4 / 3)), (curr_level - 1)
        else:
            return 0.

    @property
    def wall_bonus(self):
        """

            :param level:
            returns: either 0 or the wall bonus
            :type level: int
            """
        if self.b_name = 'wall':
            return math.pow(1.037, level)
        else:
            return 0


def main():
    """

    :return: NONE
    :rtype: None
    """

    b = Buildings()
    build_costs = b.construction_costs('hq', 21)
    result = b.actual_build_time(build_costs['duration_of_creation'], 20)
    print result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()
