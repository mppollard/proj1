# Includes constants for use in all notebooks

# URLs for data download
TLC_URL = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'
EVENT_URL = 'https://data.cityofnewyork.us/api/views/6v4b-5gp4/rows.csv?accessType=DOWNLOAD&bom=true&format=true&delimiter=%3B'
TAXI_ZONE_CSV = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv'
TAXI_ZONE_SHP = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip'

# folders to be built
ALL_FOLDERS = ('../data/', '../plots/')

# data sub-folders structure to be built and used for access
LANDING_DATA = '../data/landing/'
RAW_DATA = '../data/raw/'
CURATED_DATA = '../data/curated/'
ANALYSIS_DATA = '../data/analysis/'
TAXI_ZONE_DATA = '../data/taxi_zones/'
PLOTS = '../plots/'
ALL_DATA_SUB = ('landing', 'raw', 'curated', 'analysis', 'taxi_zones')
ALL_SOURCES = ('yellow', 'green', 'fhvhv')

# take all data from May 2020 - May 2023
years = ['2020', '2021', '2022', '2023']
start_year = '2020'; start_month = 5
end_year = '2023'; end_month = 5

# max levels for filtering outliers out of TLC data
MAX_FARE = 500
MAX_DISTANCE = 100
MAX_TIME = 300
MAX_LOCATION_ID = 264




