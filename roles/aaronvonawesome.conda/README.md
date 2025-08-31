# Role Name: conda

This Ansible Role will install [conda](https://conda.io) using the [Conda Debian Repository](https://docs.conda.io/projects/conda/en/latest/user-guide/install/rpm-debian.html).

## Requirements

- Ubuntu-based system.

## Role Variables

- N/A

## Dependencies

- N/A

## Example Playbook

```yaml
---
- name: "Install Minicoda Playbook Example"
  hosts:
    - all
  become: true


  tasks:

    - name: "Install conda on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.conda
```

## License

AGPL-3.0-or-later

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
