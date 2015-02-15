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
        'jenkins_jobs.wrappers': [
            'pyenv=modules.pyenv:pyenv',
        ]
    }
)
