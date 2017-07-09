import os

import testinfra.utils.ansible_runner

# Testinffra testing
# more info : http://testinfra.readthedocs.io/en/latest/modules.html#file

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_result1_file(host):
    f = host.file('/tmp/result1')

    assert f.exists
    assert f.contains('CRAZY NEW FILTER')


def test_result2_file(host):
    f = host.file('/tmp/result2')

    assert f.exists
    assert f.contains('- the - filters')
