"""
    
    .py
"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

import database


class TwDb(Db):
    """
        Provides tribalwars specific implementations of the Db class
    """

    def __init__(self):
        """
        """
        super(Db, self).__init__()

    def get_player_id(self, player):
        """

        :param player: player name
        :type player: str
        :return: player information
        :rtype: tuple
        """
        return Db.sp_db_query('findPlayerId', player)

    def find_player(self, player):
        return Db.sp_db_query('findPlayer', player)

    def find_village(self, x, y):
        return Db.sp_db_query('findVillage', (x, y))

