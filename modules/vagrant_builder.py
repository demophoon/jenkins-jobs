#!/usr/bin/env python
# encoding: utf-8

"""
Jenkins Job Builder - Vagrant Builder

This class provides JJB with what it needs to generate jenkins configurations
for building and tearing down vagrant boxes.
"""

import xml.etree.ElementTree as XML


def setup_base(xml_parent, base_type):
    obj = XML.SubElement(
        xml_parent,
        base_type,
        attrib={
            'plugin': 'vagrant@1.0.1'
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


def generate_vagrant_wrapper(xml_parent, data):
    wrapper = XML.SubElement(xml_parent, 'wrapper')
    options = {
        'vagrantFile': data['vagrant-file'],
        'vagrantVm': data.get('vagrant-vm', ''),
        'validated': str(data.get('validated', False)).lower(),
    }
    generate_xml(wrapper, options)


def provision(parser, xml_parent, data):
    """yaml: vagrant_provision
    """
    obj = setup_base(
        xml_parent,
        'org.jenkinsci.plugins.vagrant.VagrantProvisionCommand'
    )
    defaults = {
        'provisioners': 'Virtualbox',
        'parallel': False,
    }
    generate_xml(obj, defaults, data)
    generate_vagrant_wrapper(obj, data)


def up(parser, xml_parent, data):
    """yaml: vagrant_up
    """
    obj = setup_base(
        xml_parent,
        'org.jenkinsci.plugins.vagrant.VagrantUpCommand'
    )
    defaults = {
        'provisioners': 'Virtualbox',
        'parallel': False,
        'destroyOnError': False,
        'dontKillMe': False,
    }
    generate_xml(obj, defaults, data)
    generate_vagrant_wrapper(obj, data)


def command(parser, xml_parent, data):
    """yaml: vagrant_command
    """
    obj = setup_base(
        xml_parent,
        'org.jenkinsci.plugins.vagrant.VagrantSshCommand'
    )
    defaults = {
        'command': data['command'],
        'asRoot': False,
    }
    generate_xml(obj, defaults, data)
    generate_vagrant_wrapper(obj, data)


def destroy(parser, xml_parent, data):
    """yaml: vagrant_destroy
    """
    obj = setup_base(
        xml_parent,
        'org.jenkinsci.plugins.vagrant.VagrantDestroyCommand'
    )
    generate_vagrant_wrapper(obj, data)
