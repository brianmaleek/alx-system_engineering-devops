# Automating nginx server using puppet

package { 'nginx':
  ensure => 'installed',
}

file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World',
}

file_line { 'install':
  ensure => present,
  path   => '/etc/nginx/sites-enabled/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com\/watch?v=QH2-TGUlwu4',
  after  => 'listen 80 default_server;',
}

service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => Package['nginx'],
}
