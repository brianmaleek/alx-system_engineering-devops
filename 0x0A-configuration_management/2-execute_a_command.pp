# Using Puppet, create a manifest that kills a process named killmenow.
# Requirements:
# Must use the exec Puppet resource
# Must use pkill

exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'pgrep killmenow',
}
