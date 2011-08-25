import re

from trac.core import *
from trac.web.api import IRequestHandler

class AutocompleteKeywordsProvider(Component):

    implements(IRequestHandler)

    min_length = 2

    ### methods for IRequestHandler

    def match_request(self, req):
        """Return whether the handler wants to process the given request."""
        return req.path_info.rstrip('/') == '/ac-keywords'

    def process_request(self, req):
        """Process the request. Return a (template_name, data, content_type) tuple, 
        where `data` is a dictionary of substitutions for the template.

        "text/html" is assumed if `content_type` is `None`.

        Note that if template processing should not occur, this method can
        simply send the response itself and not return anything.
        """

        query = req.args.get('q', '').lower()
        if len(query) < self.min_length:
            req.send(''.encode('utf-8'), 'text/plain')
            return

        keywords_set = set()
        sql = '''SELECT DISTINCT keywords 
                              FROM ticket 
                              WHERE keywords LIKE %s'''
        args = ['%%%s%%' % query]

        db = self.env.get_db_cnx()
        cursor = db.cursor()
        cursor.execute(sql, args)
        for ticket_keywords, in cursor:
            tokens = re.split('[ ,]+', ticket_keywords)
            keywords_set.update([s for s in tokens if s.startswith(query)])

        keywords = list(keywords_set)
        keywords.sort()

        req.send('\n'.join(keywords).encode('utf-8'), 'text/plain')


