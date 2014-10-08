"""helpers.py
    a collection of various functions that don't fit into other files
"""

import re

#MAX number of fields covered by a church.
L1_CHURCH = 4
L2_CHURCH = 6
L3_CHURCH = 8
FIRST_CHURCH = 6

#Not Religious Penalty:
NOT_RELIGIOUS = -.50

# Maximum percentage that the wall bonus can be dropped in a single attack.
MAX_WALL_BONUS_DAMAGE = .50

#For 3 tech level worlds(15 tech)
LEVEL_TWO_UNIT = 1.25
LEVEL_THREE_UNIT = LEVEL_TWO_UNIT * 1.12




class TextHelper:
    """
        a set of text helpers, mostly regular expressions to help process text
        related to the browser game tribal wars.

    """

    def __init__(self):
        """
        >>> t = TextHelper()
        ... r = re.match(t.coord_tag_open, '[coord]')
        ... if r:
        ...     print(r.group(coord_tag))
        ... [coord]

        :return:
        :rtype: None
        """
        self.tag_open = '['
        self.tag_close = ']'
        self.tag_close_open = '[/'
        self.coord_tag = 'coord'
        self.claim_tag = 'claim'
        self.player_tag = 'player'
        self.ally_tag = 'ally'
        self.ally_tag_open_match = re.compile(r'{}{}{}'.format(self.tag_open,
                                                               self.ally_tag,
                                                               self.tag_close),
                                              re.X | re.M)
        self.coord_tag_open = re.compile(
            r'(?P<coord_tag>(\[(/)coord\]))', (re.M | re.DOTALL))
        self.coord_tag_close = re.compile(r'(?P<coord_tag>(\[(/)?coord\]))',
                                          re.M | re.X)
        self.coords = re.compile(r'(?P<coord>(\d{3}\|\d{3}))',
                                 (re.M | re.DOTALL))
        self.coord_wrp = re.compile(r'(?P<coord_wrp>[\(|\)])',
                                    (re.MULTILINE | re.DOTALL))
        self.coord_wrapped_tags = re.compile(
            r'((?P<coord_tag_open>(\[coord\])(?P<coord>((?P<x>(\d{3})\|('
            r'?P<y>\d{3}))))(?P<coord_tag_close>(\[/coord\]))))',
            re.M | re.DOTALL)


    def strip_tags(self, tags):
        """

        >>> t = TextHelper()
        ... t.strip_tags('[coord]500|500[/coord]')
        ... 500|500

        :param tags: the string to be stripped of tags
        :type tags: str
        :return: coordinates or tags
        :rtype: str
        """
        coord_match = re.match(self.coord_wrapped_tags, tags)
        if coord_match:
            coords = re.search(self.coords, tags)
            coords = coords.group(1)
            return coords
        else:
            return tags


