AUTHOR = 'Department of Technology (Khalti)'
SITENAME = 'Bits in Skewers'
SITESUBTITLE = 'Engineering | Khalti.com'
SITEURL = 'http://localhost:8000'
SHOW_SITESUBTITLE_IN_HTML = True

THEME = 'attila-1.5'
# All theme settings (for attilia)
# Reference https://github.com/arulrajnet/attila-demo/blob/master/pelicanconf.py


PATH = 'content'
OUTPUT_PATH = 'docs/'
STATIC_PATHS = ['assets/', 'extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'}, 
}

TIMEZONE = 'Asia/Kathmandu'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Khalti Digital Wallet', 'https://khalti.com/'),
)
# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/khalti'),
)
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

CSS_OVERRIDE = ['assets/css/kwati.css']
# COLOR_SCHEME_CSS = 'tomorrow_night.css'


GOOGLE_ANALYTICS = "G-0K4GR3CZ37"

# Theme configurations 
HOME_COVER = 'assets/images/skewers.jpg'

AUTHORS_BIO = {
  "dhruba-adhikari": {
    # "name": "Zutrinken",
    # "cover": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    # "image": "https://arulrajnet.github.io/attila-demo/assets/images/avatar.png",
    # "website": "http://blog.arulraj.net",
    # "location": "Chennai",
    # "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

SHOW_FULL_ARTICLE = False

HEADER_COVERS_BY_CATEGORY = {'food': '/images/junkie-stuff.png'}
HEADER_COVERS_BY_TAG = {'food': '/images/food.png', 'drinks':'/images/orange-juice.png'}
SHOW_CREDITS = False

