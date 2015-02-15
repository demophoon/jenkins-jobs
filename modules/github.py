#!/usr/bin/env python
# encoding: utf-8

"""
Jenkins Job Builder - Github Builder

This class provides JJB with what it needs to generate jenkins configurations
for updating github status
"""

import xml.etree.ElementTree as XML


def setup_base(xml_parent, base_type):
    obj = XML.SubElement(
        xml_parent,
        base_type,
        attrib={
            'plugin': 'github@1.10'
        })
    return obj


def generate_xml(xml_parent, defaults, overrides=None, stringify_bool=True):
    if not overrides:
        overrides = {}
    options = {}
    for default in defaults:
        options[default] = overrides.get(default, defaults[default])

    for opt, value in options.items():
        if stringify_bool:
            if isinstance(value, bool):
                value = str(value).lower()
        option = XML.SubElement(xml_parent, '%s' % str(opt))
        if isinstance(value, basestring):
            option.text = value


def pending(parser, xml_parent, data):
    """yaml: github_pending_status
    Builder
    """
    setup_base(
        xml_parent,
        'com.cloudbees.jenkins.GitHubSetCommitStatusBuilder'
    )


def project_url(parser, xml_parent, data):
    """yaml: github_project_url
    Property
    """
    opt = setup_base(
        xml_parent,
        'com.coravy.hudson.plugins.github.GithubProjectProperty'
    )
    generate_xml(opt, data)
