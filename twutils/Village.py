"""
Village.py
A part of TwUtility, a python package to speed up tribal wars projects
in python.

"""

__author__ = 'johnp80'
__email__ = 'johnp90380@gmail.com'


# noinspection PyDefaultArgument
class Village:
    """

    :param v_id: village id
    :param v_name: village name
    :param player: player id
    :param x: x coordinate
    :param y: y coordinate
    :param points: village points
    :param rank: village type
    :param covered: number of villages covered
    :param villages: a list of villages that would be covered by the church
    """

    def __init__(self, v_id, v_name, player,
                 x, y, points, rank, covered=0, villages=[]):
        self.v_id = v_id
        self.name = v_name
        self.player = player
        self.x = x
        self.y = y
        self.points = points
        self.rank = rank
        self.covered = covered
        self.villages = villages
        self.coords = (str(x) + '|' + str(y))

    def __repr__(self):
        """


        :return: repr
        """
        return repr((int(self.v_id), self.name, int(self.x), int(self.y),
                     int(self.points), int(self.rank), self.covered))

    def __str__(self):
        return __str__(self.coords)

    def bonus_type(self, rank):
        """

        :param rank: the village type
        :return: string
        """

        new_bonus = {'None': "None", 'Wood': '100% more wood production',
                     'Clay': '100% more clay production',
                     'Iron': '100% more iron production',
                     'Farm': '10% higher farm population ',
                     'Barracks': '50% faster infantry production',
                     'Stable': '50% faster cavalry production',
                     'Workshop': '100 % faster infantry production',
                     'Resources': '30% more production of all resources',
                     'Market': '50% more storage capacity and merchants'}

        old_bonus = {'None': "None",
                     'Wood': '10% more wood production',
                     'Clay': '10% more clay production ',
                     'Iron': '10% more iron production',
                     'Farm': '10% higher farm population ',
                     'Barracks': '10% faster infantry production',
                     'Stable': '10% faster cavalry production',
                     'Workshop': '50% faster infantry production',
                     'Resources': '3% more production of all resources',
                     'Market': 'None'}







