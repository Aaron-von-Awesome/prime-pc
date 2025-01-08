# Role Name: nextcloud_desktop_client

This Ansible Role will install the [Nextcloud Desktop Client](https://nextcloud.com/install/#desktop-files) using the [Nextcloud Desktop Client Personal Package Archive (PPA)](https://launchpad.net/~nextcloud-devs/+archive/ubuntu/client).

## Requirements

- Ubuntu-based system.

## Role Variables

### var_lts_codename

***default:*** noble

Set the codename for the version (or base version) of Ubuntu you will be using.

## Dependencies

- N/A

## Example Playbook

```yaml
---
- name: "Install Nextcloud Desktop Client Playbook Example"
  hosts:
    - all
  become: true
  vars:
    _lts_codename: "noble"


  tasks:

    - name: "Install the Nextcloud Desktop Client on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.nextcloud_desktop_client
      vars:
        var_lts_codename: "{{ _lts_codename }}"
```

## License

BSD

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
