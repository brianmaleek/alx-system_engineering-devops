# Your SSH client configuration
# Setup SSH config using Puppet
file_line { 'Turn off password auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'passwordAuthentication no',
}

file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
