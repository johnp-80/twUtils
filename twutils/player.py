"""
    player.py
    A part of TwUtility, a python package to speed up tribal wars projects
    in python.
"""

import sys


class Player:
    """
        Contains the player information
    """

    def __init__(self, player_id, player_name, player_ally, player_villages,
                 player_points, player_rank):
        self.p_id = player_id
        self.p_name = player_name
        self.p_ally = player_ally
        self.p_villages = player_villages
        self.p_points = player_points
        self.p_rank = player_rank
        self.player_data = dict(p_id=self.p_id,
                                p_name=self.p_name,
                                p_ally=self.p_ally,
                                p_villages=self.p_villages,
                                p_points=self.p_points,
                                p_rank=self.p_rank)

    def __str__(self):
        """
            :rtype: str
        """
        return __str__("Name:{}\nPoints:{}\nAlly{}\n".format(self.p_name,
                                                             self.p_points,
                                                             self.p_ally))

    def player_stats(self):
        """
        >>> p = Player("12334", "something", "", 3, 15000, 1)
        ... my_player = p.player_stats()
        ... 15000

        :return: player_points
        :rtype: int
        """
        print self.p_points

    def get_player(self):
        """

        :return: dict containing the player data
        :rtype: dict

        >>> p = Player("12334", "something", "", 3, 15000, 1)
        ... my_player = p.get_player()
        ... 12334, something, , 3, 15000, 1

        """
        print self.player_data


def main(*args, **kwargs):
    """
        stores information about a player.
        This should be used in a list, as a list of dicts.
    :return: player
    :rtype: dict
    """

    usage = "This should be used in a list, " \
            "as it does not have any useful functions" \
            " for manipulating data by itself. " \
            "Example: p = Player(123456789, 'Foo', 300, 1233, 500,000, 1)"


    if sys.argv < 1:
        print usage
    elif sys.argv == 7:
        player = Player(player_id=kwargs[1], player_name=kwargs[2],
                        player_villages=kwargs[3], player_ally=kwargs[4],
                        player_points=kwargs[5], player_rank=kwargs[6])
    else:
        print "too many/few arguments" + usage

    return player


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main()