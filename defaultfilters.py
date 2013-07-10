#This file is part nereid-demo app for Flask.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
import jinja2
from flask.ext.babel import Babel, gettext as _

def keys(text):
    """
    Split by ,
    """
    return text.split(',')

jinja2.filters.FILTERS['keys'] = keys
