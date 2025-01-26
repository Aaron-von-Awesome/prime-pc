# Role Name: redshift

This Ansible Role will install and configure Redshift-gtk with a "manual" location.

## Requirements

- Ubuntu-based system.

## Role Variables

### var_redshift_config_filename

***default:*** "redshift-conf.j2"

Name of jinja2 template file you would like to use for the `redshift.conf` file.

### var_redshift_username

***default:*** ""

Username under which to install the `redshift.conf` file.

### var_reshift_temp_day

***default:*** "7000"

Set the day screen temperature.

### var_reshift_temp_night

***default:*** "4000"

Set the night screen temperature.


### var_reshift_gamma_day

***default:*** "1.0"

Set the day screen gamma (for all colors, or each color channel individually).

**Example:**

```yaml
    - name: "Install Redshift on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.redshift"
      vars:
        var_redshift_username: "chucknorris"
        var_reshift_gamma_day: "1.0"  # for all colors
        var_reshift_gamma_day: "0.8:0.7:0.8"  # for each color channel individually
```

### var_reshift_gamma_night

***default:*** "0.9"

Set the night screen gamma (for all colors, or each color channel individually).

**Example:**

```yaml
    - name: "Install Redshift on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.redshift"
      vars:
        var_redshift_username: "chucknorris"
        var_reshift_gamma_night: "1.0"  # for all colors
        var_reshift_gamma_night: "0.8:0.7:0.8"  # for each color channel individually
```

## Dependencies

- N/A

## Example Playbook

```yaml
---
- name: "Example Playbook"
  hosts: all
  gather_facts: false
  vars:
    _username: "chucknorris"

  tasks:

    - name: "Install Redshift on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.redshift"
      vars:
        var_redshift_username: "{{ _username }}"
```

## License

BSD

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
