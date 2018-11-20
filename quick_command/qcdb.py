import pickledb
from fuzzywuzzy import fuzz


class QCDB(object):
    """
    KV Store <command, description>
    e.g. 'tar -xvf test.tar' => 'extract a tar file'
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
        return [record
                for record
                in self.getall()
                if fuzz.partial_ratio(record[1], query) > 50
                ]

    def getall(self, sort=False):
        records = [(k, self.db.get(k)) for k in self.db.getall()]
        if sort:
            records.sort()

        return records

    def delete(self, query):
        if self.db.exists(query):
            return self.db.rem(query)

        return False
