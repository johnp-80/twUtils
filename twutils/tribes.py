"""
    Tribes.py
    Contains helper functions for dealing with tribes(allies) in the browser
    game Tribalwars
"""
class Tribe(object):
    """
        http://en7.tribalwars.net/help2.php?article=map_data
       This file contains information about Tribes. The data is sorted in the
       following order:
        $id, $name, $tag, $members, $villages, $points, $all_points, $rank
    """
    def __init__(self, t_id, t_name, t_tag, t_members, t_villages, t_points,
                 t_all_points, t_rank):
        """

        :param t_id: the id number of the tribe
        :type t_id: int
        :param t_name: the name of the tribe
        :type t_name: str
        :param t_tag: the abbreviation of the tribe
        :type t_tag: str
        :param t_members: the number of members
        :type t_members: int
        :param t_villages: number of villages controlled by the tribe
        :type t_villages: int
        :param t_points: combined points of the top 40 members of the tribe
        :type t_points: int
        :param t_all_points:  combined points of the entire tribe
        :type t_all_points: int
        :param t_rank: world ranking of the tribe
        :type t_rank: int
        :return: None
        :rtype: None
        """
        self.t_id = t_id
        self.t_name = t_name
        self.t_tag = t_tag
        self.t_members = t_members
        self.t_villages = t_villages
        self.t_points = t_points
        self.t_all_points = t_all_points
        self.t_rank = t_rank

    def print_tribe(self):
        """

        :return:
        :rtype: None

        >>> t = Tribe(0, "The Avengers", "XMEN", 1, 1, 100, 100, 1)
        ... t.print_tribe()
        ... "Name:The Avengers"
        ... "Tag:XMEN"
        ... 1
        ... 100

        """
        print (
            "Name:{0}\nTag:{1}\nRank:{2}\nMembers:{3}\nPoints:{4}".format(
                self.t_name, self.t_tag, self.t_rank, self.t_members,
                self.t_points))

    @property
    def get_id(self):
        """
        :rtype : int
        :return: :rtype:

         >>> t = Tribe(0, "The Avengers", "XMEN", 1, 1, 100, 100, 1)
         ... t.get_id()
         ... 0
        """
        return self.t_id

    @property
    def get_tag(self):
        """Returns the tag of the tribe.
        :rtype : str
        :return: :rtype:


        >>> t = Tribe(0, "The Avengers", "XMEN", 1, 1, 100, 100, 1)
        ... t.get_tag()
        ... "XMEN"

        """
        return self.t_tag

    @property
    def get_villages(self):
        """

        :return: Number of villages controlled by the tribe
        :rtype: int

        >>> t = Tribe(0, "The Avengers", "XMEN", 1, 1, 100, 100, 1)
        ... t.get_villages()
        ... 1

        """
        return self.t_villages
