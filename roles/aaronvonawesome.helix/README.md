> ⚠️ Attention
>
> The Helix Editor PPA is on longer maintained as [noted here](https://github.com/helix-editor/helix/issues/11914#issuecomment-2422440519).  You can install Helix Editor on Ubuntu-based sysetm [using the Snap Package](https://snapcraft.io/helix).

# Role Name: helix

This Ansible Role will install [Helix editor](https://helix-editor.com/) using the [Helix editor Personal Package Archive (PPA)](https://launchpad.net/~maveonair/+archive/ubuntu/helix-editor).

## Requirements

- Ubuntu-based system.

## Role Variables

### var_helix_state

***default:*** present

- Set to `present` to install Helix Editor.
- Set to `absent` to remove Helix Editor.

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

AGPL-3.0-or-later

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
