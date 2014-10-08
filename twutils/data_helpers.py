"""
    data_helpers is a helper file
"""
import worldConfig


DATA_PREFIX = '/MAP/'
COMPRESSED_FILE_EXT = '.txt.gz'
UNCOMPRESSED_FILE_EXT = '.csv'
ALLY_FILE = 'ally'  # ally aka tribe
ALLY_ODA = 'kill_att_tribe'  # opponents defeated as attacker for the tribe
ALLY_ODD = 'kill_def_tribe'  # opponents defeated as defender for the tribe
ALLY_ODT = 'kill_all_tribe'  # opponents defeated total for the tribe
CONQUER_FILE = 'conquer'
PLAYER_FILE = 'player'  # player data file
PLAYER_ODA = 'kill_att'  # opponents defeated as attacker
PLAYER_ODD = 'kill_def'  # opponents defeated as defender
PLAYER_ODT = 'kill_all'  # opponents defeated total
VILLAGE_FILE = 'village'
SERVER_PROTOCOL = 'http://'
TRIBALWARS = '.tribalwars.'
INTERNATIONAL_SERVER = 'net'
BETA_TW = '.beta'
UK_TW = 'co.uk'
US_TW = 'us'
NL_TW = 'nl'

#Get the active servers
w = worldConfig.WorldConfig()
ACTIVE_SERVERS = w.get_active_servers()

#dict(list) of data files
DATA_FILES = dict(ally=ALLY_FILE, ally_oda=ALLY_ODA, ally_odd=ALLY_ODD,
                  ally_odt=ALLY_ODT, player=PLAYER_FILE, player_oda=PLAYER_ODA,
                  player_odd=PLAYER_ODD, player_odt=PLAYER_ODT,
                  village=VILLAGE_FILE, conquer=CONQUER_FILE)

#list(dict) of markets
MARKETS = dict(uk=UK_TW, US=US_TW, beta=BETA_TW, net=INTERNATIONAL_SERVER,
               nl=NL_TW)

#dict containing the names of all the update stored procedures

UPDATE_QUERIES = dict(ally='updateAlly', a_oda='updateAllyODA',
                      a_odd='updateAllyODD', a_odt='updateAllyODT',
                      conquer='updateConquer', player='updatePlayer',
                      p_oda='updatePlayerODA', p_odd='updatePlayerODD',
                      p_odt='updatePlayerODT', village='updateVillage')

#recent conquers
CONQUERS_SINCE = '/interface.php?func=get_conquer&since='