# Role Name: vagrant

This Ansible Role will install [Vagrant](https://www.vagrantup.com/) using the [HashiCorp Linux Repository](https://www.hashicorp.com/blog/announcing-the-hashicorp-linux-repository).

## Requirements

- Ubuntu-based system.

## Role Variables

### var_lts_codename

***default:*** noble

Set the codename for the version (or base version) of Ubuntu you will be using.

### var_should_install_virtualbox

***default:*** false

Set to `true` if you would like to also install Virtualbox.

## Dependencies

- N/A

## Example Playbook

```yaml
---
- name: "Install Virtualbox Playbook Example"
  hosts:
    - all
  become: true
  vars:
    _lts_codename: "noble"


  tasks:

    - name: "Install Vagrant on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.vargrant
      vars:
        var_lts_codename: "{{ _lts_codename }}"
```

## License

BSD

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
