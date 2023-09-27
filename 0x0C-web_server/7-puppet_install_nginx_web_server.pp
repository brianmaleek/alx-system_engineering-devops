# Automating nginx server using puppet

package { 'nginx':
  ensure => 'installed',
}

file_line { 'install':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4',
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'Hello World',
}

service { 'nginx':
  ensure  => 'running',
  enable  => 'true',
  require => Package['nginx'],
}
