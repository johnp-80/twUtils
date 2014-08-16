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
        self.world_config = '/interface.php?func=get_config'
        self.config_file = str(world)+'.ini'
        self.xml_config = str(world)+'.xml'

    def first_run(self, config_file):
        """
        :param config_file: world data configuration
        :return: config file
        """
        if not os.isfile(config_file):
            print("404")
            r = requests.get(('http://en70.tribalwars.net'+self.world_config))
            with open(self.xml_config, 'wb') as f:
                f.write(r.content())
            with open(self.config_file, 'wb') as g:
                converter = xml2json.convert(self.xml_config, encoding="utf-8")
                g.write(converter.get_json())
            return True
        else:
            return False



