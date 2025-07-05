# Role Name: neovim

This Ansible Role will install [Neovim](https://neovim.io/) using the [Neovim Personal Package Archive (PPA)](https://launchpad.net/~neovim-ppa/+archive/ubuntu/unstable).

## Requirements

- Ubuntu-based system.

## Role Variables

### var_lts_codename

***default:*** noble

Set the codename for the version (or base version) of Ubuntu you will be using.

### var_neovim_username

***default:*** ""

Only needed if you set `var_neovim_should_replace_vim_command` to `true`.  This User's `.bashrc` file will have alias set so `vim` and `vi` will run `nvim` command.

### var_neovim_should_replace_vim_command

***default:*** false

When set to `true`, aliases for `vim` and `vi` will be create to run the `nvim` command.  You will need to specify a User in the `var_neovim_username` variable as well.

## Dependencies

- N/A

## Example Playbook

```yaml
---
- name: "Install Neovim Playbook Example"
  hosts:
    - all
  become: true
  vars:
    _lts_codename: "noble"


  tasks:

    - name: "Install Neovim on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.neovim
      vars:
        var_lts_codename: "{{ _lts_codename }}"
```

## License

BSD

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
