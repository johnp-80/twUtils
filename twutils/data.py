"""
    data.py is designed to retrieve/store/archive data from the browser game
    Tribalwars
"""

import csv
import gzip
import requests


import database
import data_helpers

class TribalWarsData(object):
    """
    TribalWarsData is a class designed to help smooth the process of downloading
    world data from the tribalwars server.
    """
    def __init__(self, market, server):
        """
        :market the market, or language server that the world is located on.
        example: http://en70.tribalwars.net/ is on the net market, and world 70
        :server the world that the data is to be downloaded for
        :type server: str
        :type market: str
        :return:
        :rtype:
        """
        self.market = market
        self.server = server
        self.url = self.server + dh.TRIBALWARS + self.market
        self.dh = data_helpers
        self.data_file = dh.DATA_FILE
        self.db = database.Db()

    def get_data(self, data_file):
        """

        :param data_file: the name of the file being retrieved and written
        :type data_file: str
        :return: NONE
        :rtype: NONE
        """
        file_url = self.url + data_file + self.dh.COMPRESSED_FILE_EXT
        r = requests.get(file_url)
        with open(data_file + self.dh.COMPRESSED_FILE_EXT, 'w') as f:
            f.write(r.content)

    def decompress_data(self, data_file):
        """reads a compressed file and writes it to a new, uncompressed file

        :param data_file:
        """
        with gzip.open(data_file + self.dh.COMPRESSED_FILE_EXT, 'r' ) as f:
            data = f.read()
            with open(data_file + self.dh.UNCOMPRESSED_FILE_EXT, 'w') as g:
                g.write(data)

    def retrieve_tw_data(self):
        """
            Takes a dict of data files from data_helpers.py, and opens them.

        """
        for key in self.dh.DATA_FILES:
            self.get_data(data_file=key)
            self.decompress_data(data_file=key)

    def store_data(self, data_file, ):
        data = []
        with open(data_file + self.dh.UNCOMPRESSED_FILE_EXT, 'r') as f:
            data = csv.read()
            for row in data:
                self.db.sp_db_update(self.dh.UPDATE_QUERIES[data_file])
