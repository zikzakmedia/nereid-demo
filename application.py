#!/usr/bin/env python
import ConfigParser
import os

from nereid import Nereid
from nereid.sessions import Session
from nereid.contrib.locale import Babel

from werkzeug.contrib.sessions import FilesystemSessionStore
from flask.ext.babel import Babel, gettext as _

def get_config():
    '''Get values from cfg file'''
    conf_file = '%s/config.cfg' % os.path.dirname(os.path.realpath(__file__))
    config = ConfigParser.ConfigParser()
    config.read(conf_file)

    results = {}
    for section in config.sections():
        results[section] = {}
        for option in config.options(section):
            option = option.upper()
            results[section][option] = config.get(section, option)
    return results

config = get_config()

app = Nereid()
app.config.update(config.get('nereid'))
app.root_path = os.path.dirname(os.path.abspath(__file__))
app.session_interface.session_store = FilesystemSessionStore(
    '/tmp', session_class=Session
)
#~ app.config['BABEL_DEFAULT_LOCALE'] = 'es_ES'

# Initialise the app, connect to cache and backend
app.initialise()
babel = Babel(app)

#~ print app.config['BABEL_DEFAULT_LOCALE']

class NereidHostChangeMiddleware(object):
    """
    A middleware which alters the HTTP_HOST so that you can test
    the site locally. This middleware replaces the HTTP_HOST with
    the value you prove to the :attr: site

    :param app: The application for which the middleware needs to work
    :param site: The value which should replace HTTP_HOST WSGI Environ
    """
    def __init__(self, app, site):
        self.app = app
        self.site = site

    def __call__(self, environ, start_response):
        environ['HTTP_HOST'] = self.site
        return self.app(environ, start_response)


if __name__ == '__main__':
    site = config['nereid']['SITE']

    app.wsgi_app = NereidHostChangeMiddleware(app.wsgi_app, site)
    #~ app.static_folder = '%s/static' % site
    #~ app.static_folder = 'static'
    app.run()
