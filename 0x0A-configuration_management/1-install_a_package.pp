# This will install flask with version 2.1.0
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package ('Werkzeug':
  ensure  => '2.1.0',
  provide => 'pip3p'
}
