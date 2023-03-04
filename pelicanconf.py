AUTHOR = 'Department of Technology (Khalti)'
SITENAME = 'Bits in Skewers'
SITESUBTITLE = 'engineering@khalti.com'
SITEURL = 'http://localhost:8000'
THEME = 'attila-1.5'

PATH = 'content'
OUTPUT_PATH = 'docs/'
STATIC_PATHS = ['assets/']

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


# Theme configurations 
HOME_COVER = 'assets/images/skewers.jpg'
# HOME_COVER = 'assets/images/skewers.jpg'
