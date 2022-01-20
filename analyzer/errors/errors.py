class SyntaxError(Exception):

    def __init__(self, msg):
        super().__init__()
        self.code = '101'
        self.msg = msg

    def __str__(self):
        error_message = ('\n\x1b[0;31mError {code}:\n'
                         '  {msg}\n'
                         '  control your query or fiels syntax!\x1b[0;37m\n'
                         '  API documentation can be fuond at:\n'
                         '  https://patentsview.org/apis/api-query-language')
        return error_message.format(code=self.code, msg=self.msg)


class MissingQuery(Exception):

    def __init__(self):
        super().__init__()
        self.code = '102'

    def __str__(self):
        return 'Error {code}: No query specified.'.format(code=self.code)


class InvalidEndpoint(Exception):

    def __init__(self, endpoint):
        super().__init__()
        self.endpoint = endpoint
        self.code = '103'

    def __str__(self):
        error_message = ('\n\x1b[0;31mError {code}:\n'
                         '  {end} is not a valid API endpoint.\x1b[0;37m\n'
                         '  Try with one of the following values:\n'
                         '    • "patents"\n'
                         '    • "inventors"\n'
                         '    • "assignees"\n'
                         '    • "location"\n'
                         '    • "cpc_subsections"\n'
                         '    • "uspc_mainclasses"\n'
                         '    • "nber_subcategories"'
                         ).format(code=self.code, end=self.endpoint)
        return error_message


class NoData(Warning):

    def __init__(self):
        super().__init__()
        self.code = '104'

    def __str__(self):
        warning_message = ('\033[93m\n'
                           'Warning {}:\n'
                           '  This Request() object does not currently contain'
                           ' any data.\033[37m\n'
                           '  Try to use the .make_request method with a valid'
                           ' query before to call .get_data').format(self.code)
        return warning_message