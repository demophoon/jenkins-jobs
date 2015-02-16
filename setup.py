#!/usr/bin/env python
from setuptools import setup

setup(
    name="Jenkins Jobs",
    version="0.0.0",
    author="Britt Gresham",
    author_email="britt@brittg.com",
    description=("Jenkins jobs for jenkins.brittg.com"),
    license="MIT",
    install_requires=[
        "jenkins-job-builder",
    ],
    entry_points={
        'jenkins_jobs.properties': [
            'github_project_url=modules.github:project_url',
        ],
        'jenkins_jobs.builders': [
            'vagrant_provision=modules.vagrant_builder:provision',
            'vagrant_up=modules.vagrant_builder:up',
            'vagrant_command=modules.vagrant_builder:command',
            'vagrant_destroy=modules.vagrant_builder:destroy',
            'github_pending_status=modules.github:pending',
        ],
        'jenkins_jobs.wrappers': [
            'pyenv=modules.pyenv_wrapper:pyenv',
            'build_user_vars=modules.uservars:build_user_vars',
        ],
        'jenkins_jobs.publishers': [
            'git_publisher=modules.git_publisher:git_publisher',
            'github_status_on_failure=modules.github:failure',
        ],
    }
)
