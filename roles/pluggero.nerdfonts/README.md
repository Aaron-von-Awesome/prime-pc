# Ansible Role: Nerd Fonts

[![CI](https://github.com/pluggero/ansible-role-nerdfonts/actions/workflows/ci.yml/badge.svg)](https://github.com/pluggero/ansible-role-nerdfonts/actions/workflows/ci.yml) [![Ansible Galaxy downloads](https://img.shields.io/ansible/role/d/pluggero/nerdfonts?label=Galaxy%20downloads&logo=ansible&color=%23096598)](https://galaxy.ansible.com/ui/standalone/roles/pluggero/nerdfonts)

An Ansible Role that installs selected nerdfonts.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
nerdfonts_version: "3.3.0"
```

The version of the installed nerdfont (https://github.com/ryanoasis/nerd-fonts) can be defined with `nerdfonts_version`.

```yaml
nerdfonts_font: "Hack"
```

The font to be installed can be defined with `nerdfonts_font`.
It can be namely identified by the font name in https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts.

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  roles:
    - pluggero.nerdfonts
```

## License

MIT / BSD

## Author Information

This role was created in 2025 by Robin Plugge.
