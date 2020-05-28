import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_vrealize_log_insight_agent_package_is_installed(host):
    os = host.system_info.distribution
    if os == 'debian' or os == 'redhat':
        assert host.package('VMware-Log-Insight-Agent.noarch').is_installed


def test_vrealize_log_insight_agent_configuration_file(host):
    os = host.system_info.distribution
    if os == 'debian' or os == 'redhat':
        f = host.file('/var/lib/loginsight-agent/liagent.ini')
        assert f.contains('hostname=loginsight.derby.ac.uk')
        assert f.contains('proto=cfapi')
        assert f.contains('port=9543')
        assert f.contains('ssl=yes')
        assert f.contains('auto_update=yes')
        assert f.exists
        assert f.group == 'root'
        assert f.mode == 0o644
        assert f.user == 'root'


def test_vrealize_log_insight_agent_service_is_enabled_and_running(host):
    os = host.system_info.distribution
    if os == 'debian' or os == 'redhat':
        s = host.service('liagentd')
        assert s.is_enabled
        assert s.is_running
