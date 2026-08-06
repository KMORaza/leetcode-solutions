class SQL:
    def __init__(self, names, columns):
        self.tables = {}
        for i, name in enumerate(names):
            self.tables[name] = {
                'expected_cols': columns[i],
                'rows': {},  # row_id -> [values...]
                'next_id': 1
            }

    def ins(self, name, row):
        if name not in self.tables:
            return False
        table = self.tables[name]
        if len(row) != table['expected_cols']:
            return False

        row_id = table['next_id']
        table['next_id'] += 1
        table['rows'][row_id] = row[:]
        return True

    def rmv(self, name, rowId):
        if name not in self.tables:
            return
        table = self.tables[name]
        if rowId in table['rows']:
            del table['rows'][rowId]

    def sel(self, name, rowId, columnId):
        if name not in self.tables:
            return "<null>"
        table = self.tables[name]
        if rowId not in table['rows']:
            return "<null>"
        row = table['rows'][rowId]
        if columnId < 1 or columnId > len(row):
            return "<null>"
        return row[columnId - 1]

    def exp(self, name):
        if name not in self.tables:
            return []
        table = self.tables[name]
        result = []
        for row_id in sorted(table['rows'].keys()):
            row_data = [str(row_id)] + table['rows'][row_id]
            result.append(','.join(row_data))
        return result