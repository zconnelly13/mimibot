import os
import pickledb

from mimibot.src.constants import DB_PATH

db = pickledb.load("%s%s" % (os.getcwd(), DB_PATH), False)
