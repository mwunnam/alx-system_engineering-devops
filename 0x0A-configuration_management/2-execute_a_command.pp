# Using the exec resource to kill the "killmenow" process
exec { 'kill_killmenow_process':
  command     => 'pkill -f killmenow',
  path        => '/bin:/usr/bin',
  refreshonly => true,
}
