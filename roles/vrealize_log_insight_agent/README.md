vrealize_log_insight_agent Ansible role
=======================================

Ansible role to install and configure VMware vRealize Log Insight Agent.

Requirements
------------

- Access to a VMware vRealize Log Insight cluster where the agent can be downloaded from.

Usage
----------------

```yml
- hosts: all
  
  collections:
    - universityofderby.vrealize_log_insight

  tasks:
    - name: Include vRealize Log Insight agent role
      include_role:
        name: vrealize_log_insight_agent
      vars:
        vrealize_log_insight_agent_server_hostname: loginsight.domain.local
```

Role Variables
--------------

Defaults:

```yml
# vRealize Log Insight agent download URL port (9000 | 443)
vrealize_log_insight_agent_download_url_port: '9000'
# vRealize Log Insight agent download URL scheme/protocol (http | https)
vrealize_log_insight_agent_download_url_scheme: http
# vRealize Log Insight agent server/cluster FQDN
vrealize_log_insight_agent_server_hostname: null
# vRealize Log Insight agent server protocol (cfapi | syslog)
vrealize_log_insight_agent_server_proto: cfapi
# vRealize Log Insight agent server port (syslog: 514 | syslog with ssl: 6514 | cfapi: 9000 | cfapi with ssl: 9543)
vrealize_log_insight_agent_server_port: '9543'
# vRealize Log Insight agent server ssl (yes | no)
vrealize_log_insight_agent_server_ssl: 'yes'
# vRealize Log Insight agent auto update (yes | no)
vrealize_log_insight_agent_update_auto_update: 'yes'
```

Debian:

```yml
vrealize_log_insight_agent_config_path: /var/lib/loginsight-agent/liagent.ini
vrealize_log_insight_agent_download_url: "{{ vrealize_log_insight_agent_download_url_scheme }}://{{ vrealize_log_insight_agent_server_hostname }}:{{ vrealize_log_insight_agent_download_url_port }}/api/v1/agent/packages/types/deb"
```

RedHat:

```yml
vrealize_log_insight_agent_config_path: /var/lib/loginsight-agent/liagent.ini
vrealize_log_insight_agent_download_url: "{{ vrealize_log_insight_agent_download_url_scheme }}://{{ vrealize_log_insight_agent_server_hostname }}:{{ vrealize_log_insight_agent_download_url_port }}/api/v1/agent/packages/types/rpm"

```

Windows:

```yml
vrealize_log_insight_agent_config_path: '%ProgramData%\VMware\Log Insight Agent\liagent.ini'
vrealize_log_insight_agent_download_url: "{{ vrealize_log_insight_agent_download_url_scheme }}://{{ vrealize_log_insight_agent_server_hostname }}:{{ vrealize_log_insight_agent_download_url_port }}/api/v1/agent/packages/types/msi"
vrealize_log_insight_agent_service_path: '%PROGRAMFILES(X86)%\VMware\Log Insight Agent\liwinsvc.exe'

```

Dependencies
------------

None.

License
-------

Apache-2.0

Author Information
------------------

Richard Lock
