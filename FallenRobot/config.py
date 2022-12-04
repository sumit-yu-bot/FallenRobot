class Config(object):
    LOGGER = True

  # Get this value from my.telegram.org/apps
    API_ID =17221046 
    API_HASH = "233ef51a2c05a3979f95d7c7730cf320"

    CASH_API_KEY = "45NY3SDVBOAP584U"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://odrbmbxr:e3emtPKXSuW_DtPYfVgkLaY7nDtTlH2T@heffalump.db.elephantsql.com/odrbmbxr"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Belly:belly55@atlascluster.ends7zl.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

  # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/1296994c1a55dde6323b2.jpg"

    SUPPORT_CHAT = "ab_sumit"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5616489321:AAH0uo59epc6mHNcpCCu3RfB3vnDM4NOc4c"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "7S6DECSEM9NA"  # Get this value from https://timezonedb.com/api

    OWNER_ID =2139088940   # User id of your telegram account (Must be integer)

  # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = (8)

class Production(Config):
    LOGGER = True

class Development(Config):
    LOGGER = True
