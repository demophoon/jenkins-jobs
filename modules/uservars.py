#!/usr/bin/env python
# encoding: utf-8

"""
Jenkins Job Builder - Build User Vars Wrapper

This class provides JJB with what it needs to generate jenkins configurations
for adding the build user vars plugin
"""

import xml.etree.ElementTree as XML


def setup_base(xml_parent, base_type):
    obj = XML.SubElement(
        xml_parent,
        base_type,
        attrib={
            'plugin': 'build-user-vars-plugin@1.4'
        })
    return obj


def build_user_vars(parser, xml_parent, data):
    """yaml: build_user_vars
    Property
    """
    setup_base(
        xml_parent,
        'org.jenkinsci.plugins.builduser.BuildUser'
    )
