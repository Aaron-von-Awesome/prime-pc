# Role Name: install_docker

This Ansible Role will install Docker on an Ubuntu-based system (e.g. - Linux Mint, Ubuntu Cinnamon, etc.)

## Requirements

Ubuntu-based system.

## Role Variables

### var_docker_daemon_file

**_default:_** ""

Custom `daemon.json` file. Provide the name (or path) of a file located in the `files` folder of your Ansible Project. If you want to use the custom `daemon.json` provided by this Role, then pass in `install-docker_custom-docker-daemon.json`.

To use the default `daemon.json` file installed with Docker, pass in `""`:

```yaml
var_docker_daemon_file: ""
```

### var_lts_codename

**_default:_** noble

Set the codename for the version of Ubuntu you will be using. This is especially needed if you are installing Docker on Linux Mint; you cannot use the codename of the Linux Mint version, you will need the codename of the Ubuntu version on which your version of Linux Mint is based.

### var_should_install_ansible_community_docker_collection_compatibility

**_default:_** false

Boolean value. Set to `true` if you want to install the `pip` packages that allow you to use Docker with Ansible Playbooks.

### var_should_install_extra_docker_tools

**_default:_** true

Boolean value. Set to `false` if you do not want to install extra Docker tools like Oxker and Dockly.

### var_user_list

**_default:_** []

Single username or list of usernames to add into the `docker` group.

## Dependencies

Be sure to run your Playbook with `gather_facts: true`.

## Example Playbook

```yaml
---
- name: Example Playbook
  hosts: all
  gather_facts: true
  vars:
    _lts_codename: "noble"
    _user_list:
      - username: "orionpax"
      - username: "grimlock"
      - username: "computron"

  tasks:
    - name: "Install Docker on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.install_docker"
      vars:
        var_lts_codename: "{{ _lts_codename }}"
        var_user_list: "{{ _user_list }}"
```

## License

AGPL-3.0-or-later

## Author Information

| Name              | Website                     |
| ----------------- | --------------------------- |
| Aaron von Awesome | https://aaronvonawesome.com |
