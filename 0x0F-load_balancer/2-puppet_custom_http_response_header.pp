# Install Nginx and configure with a custom HTTP header
# Ensure that the package list is up to date
exec { 'apt-update':
    command     => '/usr/bin/env/apt-get -y update',
    path        => '/usr/bin/env',
    refreshonly => true,
}

# Install the Nginx package
package { 'nginx':
    ensure  => installed,
    require => Exec['apt-update'], # Ensure apt-update is executed first
}

# Create the index.html file with content "Hello World"
file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World',
}

# Add the custom HTTP header response to Nginx configuration
file_line { 'add-header':
    ensure  => present,
    path    => '/etc/nginx/sites-available/default',
    line    => "\tadd_header X-Served-By ${hostname};",
    before  => 'server_name _;',
    require => Package['nginx'], # Ensure Nginx is installed before modifying the config
}

# Ensure Nginx service is running
service { 'nginx':
    ensure  => running,
    enable  => true,
    require => [File['/var/www/html/index.html'], File_line['add-header']], # Require necessary resources
}
