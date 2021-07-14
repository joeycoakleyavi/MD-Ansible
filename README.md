# Virtual Service Migration
This Ansible playbook can be used in scenarios where virtual services need to be migrated from one service engine group to another, as long as they belong to the same Avi cloud.

## Getting Started
This automation is tested using specific versions of Ansible and makes use of libraries which are needed for playbooks to execute successfully. When developing your own automation, it is highly encouraged to make use of Python's virtual environments to avoid conflicts with other version of packages which may already be installed.

```
git clone https://github.com/joeycoakleyavi/MD-Ansible.git
cd MD-Ansible
python3 -m venv env
source env/bin/activate
pip install pip --upgrade
pip install -r requirements.txt
ansible-galaxy install avinetworks.avisdk
```

Once the environment is prepared, edit the `hosts.yml` file to include the address of your controller cluster.

```
[all]
ctl ansible_host=<ip or fqdn of controller>
```

Then, edit `vars.yml` to suit your environment

```
avi_credentials:
  controller: "{{ ansible_host }}"                          <--- Do not edit
  username: admin                                           <--- Controller Username
  password:                                                 <--- Controller Password
  api_version: 20.1.4                                       <--- Your controller version
ansible_python_interpreter: "{{ ansible_playbook_python }}" <--- Do not edit

cur_seg: My-SEG-2                                           <--- Existing Service Engine Group
new_seg: Default-Group                                      <--- New Service Engine Group
cloud_name: AWS                                             <--- Cloud Name 

vsvip_migration_list:                                       <--- Add which IPs should be migrated as separate entries
  - 10.20.200.100
  - 10.20.200.194
```

Once complete, you can run the Ansible playbook

`ansible-playbook main.yml`

## Compatibility
This automation has been tested on Avi Vantage 20.1.4