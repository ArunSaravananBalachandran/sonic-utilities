from swsssdk import ConfigDBConnector, SonicV2Connector

class Db(object):
    def __init__(self):
        self.cfgdb = ConfigDBConnector()
        self.cfgdb.connect()
        self.db = SonicV2Connector(host="127.0.0.1")
        self.db.connect(self.db.APPL_DB)
        self.db.connect(self.db.CONFIG_DB)
        self.db.connect(self.db.STATE_DB)

    def get_data(self, table, key):
        data = self.cfgdb.get_table(table)
        return data[key] if key in data else None
