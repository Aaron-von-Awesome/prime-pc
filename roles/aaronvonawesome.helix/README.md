# Role Name: helix

This Ansible Role will install [Helix editor](https://helix-editor.com/) using the [Helix editor Personal Package Archive (PPA)](https://launchpad.net/~maveonair/+archive/ubuntu/helix-editor).

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
- name: "Install Helix Playbook Example"
  hosts:
    - all
  become: true
  vars:
    _lts_codename: "noble"


  tasks:

    - name: "Install Helix on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.helix
      vars:
        var_lts_codename: "{{ _lts_codename }}"
```

## License

BSD

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
