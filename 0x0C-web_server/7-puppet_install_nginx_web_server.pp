# 0-nginx_redirect.pp

# Ensure nginx package is installed
package { 'nginx':
  ensure => installed,
}

# Ensure nginx service is running and enabled
service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  hasstatus  => true,
  require    => Package['nginx'],
}

# Create the index.html file with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  mode    => '0644',
  require => Package['nginx'],
}

# Update the Nginx default config to include the redirect
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  mode    => '0644',
  require => Package['nginx'],
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

