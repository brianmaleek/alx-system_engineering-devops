# using Puppet make changes to our configuration file. To set up your client SSH configuration
# file to connect to a server without typing a password.
# Requirements:
# Your SSH client configuration must be configured to use the private key ~/.ssh/school
# Your SSH client configuration must be configured to refuse to authenticate using a password

# Setup SSH config using Puppet
file_line { 'Turn off password auth':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  line   => '    passwordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school',
}
