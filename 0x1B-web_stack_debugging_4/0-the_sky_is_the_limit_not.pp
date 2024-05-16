# fix nginx to be able to serve more request at the sametime

exec {'modify epoll to take grant more resources':
  command  => 'sed -i "s/15/16384" /etc/default/nginx && sudo service nginx restart',
  path     => '/usr/local/sbin:/usr/local/bin',

}

