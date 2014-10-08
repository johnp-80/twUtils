"""
    worldConfig.py

    stores the world settings for the desired world.

"""
import ConfigParser
import json
import xmlutils
import os.path
import requests
import xmltodict
import unicodedata


class WorldConfig:
    """
        WorldConfig a class to get the configuration variables for the server.
    """

    def __init__(self, server_url='tribalwars.net', world='en70'):
        """

        :param server_url: the tribalwars community that you are accessing
        data from
                default is tribalwars.net
        :type server_url: str
        :param world: the specific server_url/world that you are playing
        :type world: str
        :return: None
        :rtype: None
        """

        self.protocol = 'http://'
        self.server = server_url
        self.active_server_list = '{0}{1}/backend/get_servers_xml.php'.format(
            self.protocol, self.server)
        self.world = world
        self.config_location = '/interface.php?func='
        self.unit_config = 'get_unit_info'
        self.building_config = 'get_building_info'
        self.world_config = 'get_config'
        self.config_xml = (
            self.protocol + self.world + '.' + self.server +
            self.config_location)
        self.world_conf_location = (self.config_xml + self.world_config)
        self.build_config_location = (self.config_xml + self.building_config)
        self.unit_conf_location = (self.config_xml + self.unit_config)
        self.json_file = '.json'
        self.xml_file = '.xml'
        self.config_file = world + '.json'
        self.world_configuration_file = world
        self.build_configuration_file = world + '_buildings'
        self.unit_configuration_file = world + '_units'
        self.config = {}
        self.active_servers = {}
        self.config_type = dict(
            world_conf=dict(conf_location=self.world_conf_location,
                            conf_xml="{0}{1}".format(
                                self.world_configuration_file, self.xml_file),
                            conf_json="{0}{1}".format(
                                self.world_configuration_file, self.json_file)),
            building_conf=dict(conf_location=self.build_config_location,
                               conf_xml="{0}{1}".format(
                                   self.build_configuration_file,
                                   self.xml_file),
                               conf_json="{0}{1}".format(
                                   self.build_configuration_file,
                                   self.json_file)),
            unit_conf=dict(conf_location=self.unit_conf_location,
                           conf_xml="{0}{1}".format(
                               self.unit_configuration_file, self.xml_file),
                           conf_json="{0}{1}".format(
                               self.unit_configuration_file, self.json_file)))


    def get_active_servers(self):
        """
            Obtains the list of active servers from the tribalwars server.
            Currently only supports tribalwars.net, but more servers can be
            added later.
        >>> active_servers = WorldConfig()
        ... active_servers.get_active_servers
        ... [<doctest_ellipsis.WorldConfig object at 0x...>]
        """
        r = requests
        if not os.path.isfile('active_servers.xml'):
            try:
                r.get(self.active_server_list)
                with open("active_servers.xml", 'wb') as f:
                    content = r.content
                    content.encode('ascii', 'ignore')
                    f.write(content)
            except r.ConnectionError as e:
                raise r.ConnectionError, e.response, e.request
            except r.Timeout as e:
                raise r.Timeout, e.response, e.request
            except r.HTTPError as e:
                raise r.HTTPError, e.response, e.request

        with open('active_servers.xml', 'rb') as f:
            active_servers_xml = xmltodict.parse(f.read().encode('ascii',
                                                                 'ignore'))
        for x in xrange(0, len(active_servers_xml['urls']['url'])):
            self.active_servers.setdefault(
                (active_servers_xml['urls']['url'][x]['@id']).encode('ascii',
                                                                     'ignore'),
                (active_servers_xml['urls']['url'][x]["#text"]).encode('ascii',
                                                                       'ignore')
            )

        return self.active_servers

    def grab_config(self):
        """Grabs the world config from the server and writes it to an xml
        file

        >>> new_config = WorldConfig()
        ... new_config.grab_config()
        ... [<doctest_ellipsis.WorldConfig object at 0x...>]

        """
        try:
            for key in self.config_type:
                r = requests.get(self.config_type[key]['conf_location'])
                with open(self.config_type[key]['conf_xml'], 'wb') as f:
                    f.write(r.content)
        except requests.HTTPError as e:
            raise requests.HTTPError, e.response, e.request
        except requests.ConnectionError as e:
            raise requests.ConnectionError, e.request, e.response
        except requests.RequestException:
            raise requests.RequestException.response

    def convert_to_json(self):
        """Converts the settings.xml file to json
        :return:NONE
        :rtype:None

        >>> xml_to_json = WorldConfig()
        ... xml_to_json.convert_to_json()
        ...
        """
        try:
            for key in self.config_type:
                with open(self.config_type[key]['conf_json'], 'wb') as f:
                    converter = xmlutils.xml2json.xml2json(
                        self.config_type[key]['conf_xml'],
                        self.config_type[key]['conf_json'])
                    self.config = converter.get_json()
                    f.write(self.config)
        except IOError as e:
            print "{}:File {} not found".format(e.errno, e.filename)
        except RuntimeError as e:
            print '{}'.format(e.message)

    @property
    def return_config(self):
        """ :rtype list:
            :returns: the configuration for the requested server.

            >>> conf = WorldConfig()
            ... world_settings = conf.return_config
            ... print world_settings
            ... [<doctest_ellipsis.WorldConfig object at 0x...>]
        """
        for key in self.config_type:
            with open(self.config_type[key]['conf_json']) as f:
                self.config = json.load(f, encoding='UTF-8')
        return self.config


    def first_run(self):
        """Checks to see if this is the first run. If it's not the first
        run,
        then it will return false. On first run, it grabs the .xml config
        files,
        converts them to json, and returns the configuration settings
        for the world, buildings, and units
        """
        for key in self.config_type:
            if not os.path.isfile(self.config_type[key]['conf_json']):
                self.grab_config()
                self.convert_to_json()
                self.return_config
                return True
            else:
                return False


    def get_world_config(self):
        """
        returns the world settings
        :return: dict of world config settings
        :rtype: dict
        >>> w = WorldConfig
        ... w.get_world_config
        ... [<doctest_ellipsis.WorldConfig object at 0x...>]
        """
        with open(self.config_type['world_conf']['conf_json']) as f:
            w_conf = json.load(f, 'UTF-8')
        return w_conf['config']


    def get_building_config(self):
        """
        usage: building_config = worldConfig.WorldConfig.get_building_config()

        this will allow you to read the configuration for the designated server,
        and to make calculations based on the configuration settings.

        :return: b_config
        :rtype: dict
        >>> b = WorldConfig()
        ... b_config = b.get_building_config()
        ... [<doctest_ellipsis.WorldConfig object at 0x...>]


        """
        try:
            with open(self.config_type['building_conf']['conf_json']) as f:
                b_conf = json.load(f, "UTF-8")
        except IOError as e:
            print "File {} Was not found. Run first_run()".format(e.filename)
            raise IOError

        return b_conf['config']


    def get_unit_config(self):
        """
        usage: unit_config = worldConfig.WorldConfig.get_unit_config()

        :return: u_config
        :rtype: dict:
        >>> unit_config = WorldConfig()
        ... unit_config.get_unit_config
        ... [<doctest_ellipsis.WorldConfig object at 0x...>]
        """
        try:
            with open(self.config_type['unit_conf']['conf_json'], 'r') as f:
                u_conf = json.load(f, 'UTF-8')
        except IOError as e:
            print "File {} Was not found. Run first_run()".format(e.filename)
            raise IOError
        try:
            assert isinstance(u_conf, dict)
        except AssertionError as e:
            print "{} failed with args: {}".format(e.message, e.args)
        return u_conf['config']

    def get_specific_build_config(self, building):
        """

        :param building: the building that should be returned
        :type building: str
        :return: a dict containing the building configuration data for the
        requested building
        :rtype: dict
        """
        conf = self.get_building_config()
        return conf[building]

    def get_specific_unit_config(self, unit):
        """
        usage:

        >>> spear = WorldConfig()
        ... spear.stats = spear.get_specific_unit_config('spear')
        ... "spear": {"stone": "30", "defense": "15", "pop": "1",
        ...           "attack": "10", "wood": "50", "defense_cavalry": "45",
        ...           "build_time": "1020", "iron": "10", "carry": "25",
        ...           "defense_archer": "20", "speed": "18.000000000504"}

        :param unit: the v_name of the unit to be returned
        :type unit: str
        :return: unit configuration information
        :rtype: dict
        """
        conf = self.get_unit_config
        return conf[unit]


    def is_archer_world(self):
        world = self.get_world_config()
        if world['game']['archer'] == 0:
            return True
        else:
            return False


    def is_church_world(self):
        """
        Checks if the server has churches turned on or not.
        :return: True if churches are active
        :rtype: bool
        """
        world = self.get_world_config()
        if world['game']['church'] == 1:
            return True
        else:
            return False


    def paladin_is_active(self):
        """
        Checks if the server has paladins turned on or not
        :return: True, if paladin is active, otherwise false
        :rtype: bool
        """
        world = self.get_world_config()
        if world['game']['knight'] == 0:
            return False
        return True


    def paladin_new_items(self):
        """
        checks if the paladin uses improved items or not
        :return: True if new items are active
        :rtype: bool
        """
        world = self.get_world_config()
        if not self.paladin_is_active():
            return False
        if world['game']['knight_new_items'] == 1:
            return True


    def get_world_speed(self):
        """
            Returns the world speed from the world config file
        :return: world speed
        :rtype: int
        """
        world = self.get_world_config()
        return world['speed']


    def get_unit_speed(self):
        """
        Returns the unit speed

        :return: unit speed
        :rtype: int
        """
        world = self.get_world_config()
        return world['unit_speed']


def main(server='tribalwars.net', world='70', market='en'):
    """


        :param server: example: tribalwars
        :param world: example: 70
        :param market: The language settings for the game example: en.
        :return: list of world settings
        :rtype: list
        """
    world_config = WorldConfig(server, (market + world))
    try:
        if (market + world) in world_config.get_active_servers.keys():
            if world_config.first_run:
                print("Please select a server and world to download data for")
                server = raw_input(
                    'tribalwars.net is the only supported server')
                new_world = raw_input(
                    'Please enter only the number of the world')
                world_config = WorldConfig(server, (market + new_world))
                settings = world_config.return_config
                return settings
            else:
                settings = world_config.return_config
                return settings
    except:
        raise ValueError


if __name__ == '__main__':
    main()
    import doctest

    doctest.testmod()








