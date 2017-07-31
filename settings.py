## Price

MIN_PRICE = 4000

MAX_PRICE = 8000

## Location preferences

# The Craigslist site you want to search on.
# For instance, https://sfbay.craigslist.org is SF and the Bay Area.
# You only need the beginning of the URL.
CRAIGSLIST_SITE = 'sfbay'

AREAS = ["sfc"]

# A list of neighborhoods and coordinates that you want to look for apartments in.  Any listing that has coordinates
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "haight": [
        [37.77059, -122.42688],
        [37.77086, -122.45401],
    ],
    "bernal heights": [
        [37.73132, -122.42489],
        [37.7491, -122.40361],
    ],
    "castro": [
        [37.755398, -122.44646],
        [37.76958, -122.42638],
    ],
    "mission": [
        [37.747549, -122.429894],
        [37.77062, -122.406376],
    ],
    "potrero hill": [
        [37.749303, -122.403793],
        [37.766946, -122.379588],
    ],
    "dogpatch": [
        [37.750150, -122.391858],
        [37.764272, -122.386347],
    ],
    "hayes": [
        [37.770536, -122.429548],
        [37.778847, -122.422167],
    ],
    "duboce triangle": [
        [37.762631, -122.435665],
        [37.769687, -122.426138],
    ]
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = [ "cow hollow", "haight", "haight ashbury", "bernal heights",  "mission", "potrero hill", "dogpatch", "castro", "hayes", "duboce triangle", "twin peaks"]


## Search type preferences

CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

SLEEP_INTERVAL = 20 * 60 # 20 minutes

SLACK_CHANNEL = "#housing"

SLACK_TOKEN ="xoxp-218963705857-220389055126-219557281076-0f8bc6da415ce350e19f69f564ce3b82"

