# Install Nginx and configure with a custom HTTP header
# Install the Nginx package
package { 'nginx':
    ensure  => installed,
}

# Create the index.html file with content "Hello World"
file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World',
}

# Add the custom HTTP header response to Nginx configuration
file_line { 'add-header':
    ensure => present,
    path   => '/etc/nginx/sites-available/default',
    line   => "\add_header X-Served-By ${hostname};",
    after  => 'server_name _;',
}

# Ensure Nginx service is running
service { 'nginx':
    ensure  => running,
}
