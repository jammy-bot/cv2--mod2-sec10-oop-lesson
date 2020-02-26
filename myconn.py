class MyDatabase():

    def __init__(self, filename=None): # dunders
        self.create_connection(filename=filename)


    def create_connection(self, filename):
        # creating our connection to our sqlite file
        self.connction = sqlite3.connect(filename)
        # creating our cursor attribute
        self.api = self.connction.cursor()


    def get_table_list(self):
        query = "select name from sqlite_master WHERE type = 'table';"
        table_names_result = self.api.execute(query).fetchall(
        table_names = [result[0] for result in table_names_result]
        return table_names


    # select everything from table
    def select_all_table(self, table_name=None):
        query = f"select * from {table_name}"
        res = self.api.execute(query).fetchall()
        return res

    # show table in dataframe
    def load_table_as_df(self, table_name=None):
        query = f"select * from {table_name}"
        df = pd.read_sql(query, self.connection)
        return df
