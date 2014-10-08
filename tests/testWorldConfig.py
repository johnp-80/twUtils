"""Tests for the twutils module"""
from nose.tools import *
from twutils import worldConfig




def setUp():
    print "Setup!"


def tearDown():
    print "tear down"

def test_server():
    """
    :return: True/False depending on whether the server url matches
     known tw servers
    :rtype: Boolean
    """
    test_server_url = worldConfig.WorldConfig.server


    if 'tribalwars.net' == test_server_url:
        return True
    else:
        return False


def test_get_world_config():
    try:
        assert isinstance(b_conf, dict)
    except AssertionError as e:
        print "{} failed with args: {}".format(e.message, e.args)
