Role Name
=========

I developed this role as a quick template for validating Jinja2 filters within
an Ansible role. This is basically an implametation of the excelent
article on [Das Blinken Lichten](http://www.dasblinkenlichten.com/creating-ansible-filter-plugins/)

While there are probaly simpler ways to test jinja2 filters, I'm currently using them in Ansible, so I built a quick test infrastructure around it using [Molecule](http://molecule.readthedocs.io/en/master/).

Requirements
------------

To run the test framework you will need :

- Ansible
- Molecule
- Docker

(TODO: Test on a blank machine to see if anything is missing. Add a way to self install)

Role Variables
--------------

The role has no variables. It only contains filters in the ```filter_plugins```
directory.

Dependencies
------------

None.

Example Playbook
----------------

By including the role, the filter is loaded and can be used.

```
    - hosts: servers
      roles:
         - role: jinja2-ansible-test
```

TODO: Confirm this.

Usage
------

The framework uses molecule to build and test the different use cases for the role.
As stated above, I'm sure there is a better way to test Jinja2 filters, it is just
that I have been using molecule to test things.

Overall testing is done by ```molecule test```

The individual steps are ```molecule create``` to create the docker image,
,```molecule converge``` to run ```molecule/default/playbook.yml``` against the image
, and ```molecule verify``` to run the tests against the image.

The test cases need to be written into
the ```molecule/default/test/test_default.py``` using the TestInfra framework.

License
-------

BSD

Author Information
------------------

Author of the filter : JON LANGEMAK  ( http://www.dasblinkenlichten.com/ )
Author of the role/test framework: Alain Chiasson ( https://github.com/alainchiasson/jinja2-ansible-test )
