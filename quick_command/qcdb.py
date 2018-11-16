import pickledb
from fuzzywuzzy import fuzz
from itertools import compress


class QCDB(object):
    """
    Persistant KV Store <command, description>
    """
    def __init__(self, path_to_db):
        self.db = pickledb.load(path_to_db, True)

    def put(self, cmd, desc):
        return self.db.set(cmd, desc)

    def get_by_cmd(self, query):
        return [(cmd, self.db.get(cmd))
                for cmd
                in self.db.getall()
                if cmd.startswith(query)
                ]

    def get_by_desc(self, query):
        records = self.getall()
        ratios = [fuzz.partial_ratio(query, desc) for _, desc in records]
        selectors = [ratio > 50 for ratio in ratios]
        records = list(compress(records, selectors))

        return records

    def getall(self, sort=False):
        records = [(k, self.db.get(k)) for k in self.db.getall()]
        if sort:
            records.sort()

        return records

    def delete(self, query):
        if self.db.exists(query):
            self.db.rem(query)
            return True

        return False
