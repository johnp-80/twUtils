"""
Village.py
A part of TwUtility, a python package to speed up tribal wars projects
in python.

"""
import worldConfig
import tw_map


class Village(object):
    """

    :param v_id: village id
    :param v_name: village v_name
    :param player: player id
    :param x: x coordinate
    :param y: y coordinate
    :param points: village points
    :param rank: village type
    :param villages: a list of villages that would be covered by the church
    """

    def __init__(self, v_id, v_name, player,
                 x, y, points, rank, villages=[]):
        """

        :param v_id: village id
        :param v_name: village v_name
        :param player: player id
        :param x: x coordinate
        :param y: y coordinate
        :param points: village points
        :param rank: village type
        :param covered: If the village is covered by a church or not
        :param villages: a list of villages that would be covered by the church
        """
        w = worldConfig.WorldConfig.get_world_config()

        self.v_id = v_id
        self.v_name = v_name
        self.player = player
        self.x = x
        self.y = y
        self.points = points
        self.rank = rank
        if w['game']['church'] == 1:
            self.covered = covered
        self.villages = villages
        self.coords = (str(x) + '|' + str(y))

    def __repr__(self):
        """


        :return: repr
        """
        return repr((int(self.v_id), self.v_name, int(self.x), int(self.y),
                     int(self.points), int(self.rank), self.covered))

    def __str__(self):
        return __str__(self.coords)


class BonusVillage(Village):
    """
        Extends Village, to provide bonus village functions
    """
    super(Village, self).__init__(Village.v_id, Village.name, Village.player,
                                  Village.x, Village.y, Village.points,
                                  Village.rank, Village.villages)


    @property
    def print_bonus_type(self):
        """


        :rtype : dict value
        :param rank: the village type
        :return: string
        """
        # ######################################################################
        # From the tribal wars wiki:
        # http://help.tribalwars.net/wiki/Bonus_villages
        # ######################################################################
        # Type	    #Old style bonus	                    #
        # Wood	    #10% more wood production	            #
        # Clay	    #10% more clay production	            #
        # Iron	    #10% more iron production	            #
        # Farm	    #10% higher farm population	            #
        # Barracks	#10% faster infantry production	        #
        # Stable	#10% faster cavalry production	        #
        # Workshop	#50% faster infantry production	        #
        # Resources	#3% more production of all resources    #
        # Market	#Unavailable	                        #
        # ######################################################################
        # Type	    #Type      #Enhanced style bonus        #
        # Wood	    #100% more wood production              #
        # Clay	    #100% more clay production              #
        # Iron	    #100% more iron production              #
        # Farm	    #10% higher farm population             #
        # Barracks  #50% faster infantry production         #
        # Stable    #50% faster cavalry production          #
        # Workshop  #100% faster infantry production        #
        # Resources #30% more production of all  resources  #
        # Market    #50% more store capacity and merchants#
        # ######################################################################
        new_bonus = {'0': "None",
                     '1': '100% more wood production',
                     '2': '100% more clay production',
                     '3': '100% more iron production',
                     '4': '10% higher farm population ',
                     '5': '50% faster infantry production',
                     '6': '50% faster cavalry production',
                     '7': '100 % faster infantry production',
                     '8': '30% more production of all resources',
                     '9': '50% more store capacity and merchants'}

        old_bonus = {'0': "None",
                     '1': '10% more wood production',
                     '2': '10% more clay production ',
                     '3': '10% more iron production',
                     '4': '10% higher farm population ',
                     '5': '10% faster infantry production',
                     '6': '10% faster cavalry production',
                     '7': '50% faster infantry production',
                     '8': '3% more production of all resources'}

        config = worldConfig.WorldConfig.return_config
        if not config['config']['coord']['bonus_old']:
            try:
                return new_bonus[rank].item()
            except KeyError:
                print("Key not found. Valid ranges are between 0 and 9 for new"
                      "bonuses, and 0-8 for old bonuses")
        else:
            try:
                return old_bonus[rank].item()
            except KeyError:
                print("Key not found. Valid ranges are between 0 and 9 for new"
                      "bonuses, and 0-8 for old bonuses")


    @property
    def bonus_value(self):
        """

            >>>b = BonusVillage('Wood')
            ... bonus = b.bonus_value
            ... print bonus
            ... .100
            ... print bonus
            ... .100
            ... print bonus
            ... .100
            ... print bonus
            ... .100
        :param rank: type of bonus village.
        """"""
    """"""
    """"""
    """"""
    """"""
    """
        new_bonus = dict(None=0, Wood=.100, Clay=.100, Iron=100, Farm=.10,
                         Barracks=.50, Stable=.50, Garage=.100, Resource=.30,
                         Store=.50)
        old_bonus = dict(None=0, Wood=.10, Clay=.10, Iron=.10, Farm=.10,
                         Barracks=.10, Stable=.10, Garage=.50, Resource=.03)

        config = worldConfig.WorldConfig.return_config
        if not config['config']['coord']['bonus_old']:
            try:
                return new_bonus[self.rank].item()
            except KeyError as err:
                print("Key not found. Valid ranges are between 0 and 9 for new"
                      "bonuses, and 0-8 for old bonuses", err.args, err.message)
        else:
            try:
                return old_bonus[self.rank].item()
            except KeyError:
                print(
                    "Key not found. Valid ranges are between 0 and 9 for new"
                    "bonuses, and 0-8 for old bonuses")

class ChurchVillage(Village):
    """
        Extends Village, to provide church specific functions
    """

    def __init__(self, church_size=6):
        """

        :param church_size: default is first church radius
        """
        self.first_church = 6
        self.level_one = 4
        self.level_two = 6
        self.level_three = 8
        self.church_size = church_size
        super(Village, self).__init__()

    def covered_by_church(self, dest_x, dest_y):

        """
            Checks if a village is covered by the village.
        :param dest_x: x coordinates of the target village
        :param dest_y: y coordinates of the target village
        :return: :rtype: boolean
        """
        field = tw_map.get_fields(self.x, self.y, dest_x, dest_y)
        if field > self.church_size:
            return False
        return True






