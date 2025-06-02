# Ansible Role: Lazygit

[![CI](https://github.com/pluggero/ansible-role-lazygit/actions/workflows/ci.yml/badge.svg)](https://github.com/pluggero/ansible-role-lazygit/actions/workflows/ci.yml) [![Ansible Galaxy downloads](https://img.shields.io/ansible/role/d/pluggero/lazygit?label=Galaxy%20downloads&logo=ansible&color=%23096598)](https://galaxy.ansible.com/ui/standalone/roles/pluggero/lazygit)

An Ansible Role that installs Lazygit on various Linux distributions.

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

```yaml
lazygit_version: "x.x.x"
```

- The version of Lazygit to install.

```yaml
lazygit_install_method: "dynamic"
```

The method used to install lazygit can be defined in the variable `lazygit_install_method`.
The following methods are available:

- `source`: Installs lazygit from source
- `package`: Installs lazygit from the package manager of the distribution
  - **NOTE**: This method installs the latest version available in the package manager and not the version defined in `lazygit_version`.
  - In that distributions where the lazygit is not available in the package manager, it will be installed from the source.
- `dynamic`: Installs lazygit from package manager if available in the correct version, otherwise installs from source

## Dependencies

None.

## Example Playbook

```yaml
- hosts: all
  roles:
    - pluggero.lazygit
```

## License

MIT / BSD

## Author Information

This role was created in 2025 by Robin Plugge.
