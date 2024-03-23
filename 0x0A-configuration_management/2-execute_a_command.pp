#!/usr/bin/pup
# Using the exec resource to kill the "killmenow" process
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell'
}
