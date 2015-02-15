#!/usr/bin/env python
# encoding: utf-8

"""
Jenkins Job Builder - Pyenv Wrapper Module

This class provides JJB with what it needs to generate jenkins configurations
for wrapping a job in a Python virtual environment.
"""

import xml.etree.ElementTree as XML


def pyenv(parser, xml_parent, data):
    """yaml: pyenv
    """
    rpobj = XML.SubElement(xml_parent, 'ruby-proxy-object')
    robj = XML.SubElement(rpobj, 'ruby-object', attrib={
        'pluginid': 'pyenv',
        'ruby-class': 'Jenkins::Tasks::BuildWrapperProxy'
    })
    pluginid = XML.SubElement(robj, 'pluginid', {
        'pluginid': 'pyenv', 'ruby-class': 'String'
    })
    pluginid.text = 'pyenv'
    obj = XML.SubElement(robj, 'object', {
        'ruby-class': 'PyenvWrapper', 'pluginid': 'pyenv'
    })

    defaults = {
        'pyenv__revision': 'master',
        'pip__list': 'tox',
        'pyenv__root': '$HOME/.pyenv',
        'version': '2.7.3',
        'ignore__local__version': False,
        'pyenv__repository': 'https://github.com/yyuu/pyenv.git',
    }
    options = {}
    for default in defaults:
        options[default] = data.get(default, defaults[default])

    for opt, value in options.items():
        if isinstance(value, basestring):
            ruby_class = 'String'
        elif isinstance(value, bool):
            ruby_class = '%sClass' % str(value)
        option = XML.SubElement(obj, '%s' % opt, {
            'pluginid': 'pyenv', 'ruby-class': ruby_class
        })
        if isinstance(value, basestring):
            option.text = value
