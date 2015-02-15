#!/usr/bin/env python
# encoding: utf-8

"""
Jenkins Job Builder - Git Publisher

This class provides JJB with what it needs to generate jenkins configurations
for wrapping publishing build artifacts to a git repository.
"""

import xml.etree.ElementTree as XML


def git_publisher(parser, xml_parent, data):
    """yaml: git_publisher
    """
    obj = XML.SubElement(xml_parent, 'hudson.plugins.git.GitPublisher',
                         attrib={
                             'plugin': 'git@2.3.4'
                         })

    defaults = {
        'configVersion': '2',
        'pushMerge': False,
        'pushOnlyIfSuccess': True,
        'forcePush': False,
    }
    options = {}
    for default in defaults:
        options[default] = data.get(default, defaults[default])

    for opt, value in options.items():
        if isinstance(value, bool):
            value = str(value).lower()
        option = XML.SubElement(obj, '%s' % str(opt))
        option.text = value
        if isinstance(value, basestring):
            option.text = value

    branches = XML.SubElement(obj, 'branchesToPush')
    branches = XML.SubElement(branches,
                              'hudson.plugins.git.GitPublisher_-BranchToPush')
    remoteRepoName = XML.SubElement(branches, "targetRepoName")
    remoteRepoName.text = data['remote']
    branchName = XML.SubElement(branches, "branchName")
    branchName.text = data['branch']
