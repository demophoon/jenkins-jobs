#!/bin/bash

# Install Puppet and r10k
sudo apt-get install puppet -y
sudo gem install r10k

# Lay down r10k.yaml config
sudo bash -c "cat >/etc/r10k.yaml" <<EOF
:cachedir: '/var/cache/r10k'
:sources:
  :default:
    remote: 'https://github.com/demophoon/puppet-environment.git'
    basedir: '/etc/puppet/environments'
EOF

# Deploy r10k environments
sudo r10k deploy environment -pv

# Show diff of development and production
sudo diff -r --exclude=".git" /etc/puppet/environments/production /etc/puppet/environments/development

# Save head puppet apply
sudo puppet apply --parser={parser} --modulepath /etc/puppet/environments/development/modules /etc/puppet/environments/development/site.pp --noop > ~/current.log

# Save head puppet apply
sudo puppet apply --parser={parser} --modulepath /etc/puppet/environments/production/modules /etc/puppet/environments/production/site.pp --noop > ~/previous.log

# Save and echo diff
sudo diff ~/current.log ~/previous.log > ~/diff.log
sudo cat ~/diff.log
