import jproperties
from helpers import Paths


class Configreader:
    config = jproperties.Properties()

    def __init__(self, properties_file):
        pageobjects = Paths.projectpaths.HOME_DIR + "\\PageObjects\\" + properties_file + ".properties"
        with open(pageobjects, 'rb') as pageobj:
            self.config.load(pageobj)

    def getData(self, key):
        return self.config.get(key).data
