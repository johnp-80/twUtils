"""
    worldConfig.py

    stores the world settings for the desired world.

"""
import ConfigParser
from xmlutils.xml2json import xml2json
import os.path
import requests

__author__ = 'johnp80'

class WorldConfig:
    """
        WorldConfig a class to get the configurate variables for the server.
    """
    def __init__(self, server='tribalwars.net', world='en70'):
        """

        :param server: the tribalwars community that you are accessing data from
                default is tribalwars.net
        :type server: str
        :param world: the specific server/world that you are playing
        :type world: str
        :return: None
        :rtype: None
        """
        self.server = server
        self.world = world

