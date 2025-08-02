# Role Name: lube_logger

Ansible Role to install and configure [Lube Logger](https://github.com/hargata/lubelog) using the Docker container.

## Requirements

- Ubuntu-based system.
- Docker engine installed (https://docs.docker.com/engine/install) on **target** node.
  - `sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`

## Role Variables

### var_lube_logger_docker_compose_input_filename

***default:*** "lube-logger_docker-compose.j2"

The Docker Compose file that will be used to start up the Lube Logger Docker Services (minus the Network Services).  The settings for this file work in conjunction with the `var_lube_logger_compose_with_default_network_input_filename` or `var_lube_logger_compose_with_swag_input_filename`.

You can use a `jinja2` template file or standard `YAML` file.

### var_lube_logger_docker_compose_output_filename

***default:*** "docker-compose.yaml"

Name of the Docker Compose file (base configuration) that will be output into the directory set by `var_lube_logger_docker_compose_directory`.

### var_lube_logger_docker_compose_directory

***default:*** "~/Container-Apps/LubeLogger"

Directory in which the Lube Logger Docker Compose and configuration files will be stored.

### var_lube_logger_compose_with_default_network_input_filename

***default:*** "lube-logger_compose-with-default-network.j2"

The Docker Compose file that holds the configuration of the Network Services.  This Docker Compose file will be merged with the file specified in the `var_lube_logger_docker_compose_input_filename` variable.

### var_lube_logger_compose_with_default_network_output_filename

***default:*** "compose-with-default-network.yaml"

Name of the Docker Compose file (for network configuration) that will be output into the directory set by `var_lube_logger_docker_compose_directory`.

### var_lube_logger_compose_with_swag_input_filename

***default:*** "lube-logger_compose-with-swag.j2"

When `var_should_deploy_with_swag_container` is set to `true`, this value will supersede `var_lube_logger_compose_with_default_network_input_filename`.

The Docker Compose file that holds the configuration of the Network Services plus a [SWAG](https://hub.docker.com/r/linuxserver/swag) container (for setting up LetsEncrypt).  This Docker Compose file will be merged with the file specified in the `var_lube_logger_docker_compose_input_filename` variable.

### var_lube_logger_compose_with_swag_output_filename

***default:*** "compose-with-swag.yaml"

Name of the Docker Compose file (for network and [SWAG](https://hub.docker.com/r/linuxserver/swag) configuration) that will be output into the directory set by `var_lube_logger_docker_compose_directory`.

### var_lube_logger_container_image_version

***default:*** "v1.4.9"

Version of LubeLogger to install.  This will be used for the tag of the Container Image (https://hub.docker.com/r/hargata/lubelogger/tags).

### var_lube_logger_container_name

***default:*** "lubelog-ui"

Name of the Lube Logger Container, i.e. value shown under `NAMES` when running `docker ps`.

### var_lube_logger_container_port

***default:*** "9001"

Port under which LubeLogger will run.

### var_lube_logger_container_username

***default:*** ""

Linux User under which the Docker Compose and configuration files will be installed. ***Note:*** *This User should be a part of the `docker` group.*

### var_lube_logger_postgres_container_image_version

***default:*** "17"

Version of [Postgres Docker Container](https://hub.docker.com/_/postgres) that will be used.

### var_lube_logger_postgres_container_name

***default:*** "lubelog-db"

Name of [Postgres Docker Container](https://hub.docker.com/_/postgres).

### var_lube_logger_postgres_db

***default:*** "lubelogdb"

Name of [Postgres Docker Container](https://hub.docker.com/_/postgres) database.

### var_lube_logger_postgres_user

***default:*** "lubelogger"

Login Username for [Postgres Docker Container](https://hub.docker.com/_/postgres) database.

### var_lube_logger_postgres_password

***default:*** "changemeplease"

Password for [Postgres Docker Container](https://hub.docker.com/_/postgres) database.

### var_lube_logger_project_name

***default:*** "lube_log"

Docker Compose project name.

### var_lube_logger_state

***default:*** "present"

Values of either `present` or `absent` are accpted.

- `present`: will install Lube Logger Docker Container service, volumes, and configuration files.
- `absent`: will completely remove Lube Logger Docker Container service, volumes, and configuration files.

### var_lube_logger_swag_cloudflare_api_token

***default:*** ""

Cloudflare "Account API Token" with `Zone.DNS` premissions.

Used with [SWAG](https://hub.docker.com/r/linuxserver/swag) Docker Container.  Currently only Cloudflare and a DNS challenge is used with the LetsEncrypt functionality.

*Only used if `var_should_deploy_with_swag_container` is set to `true`.*

### var_lube_logger_swag_cloudflare_ini_input_filename

***default:*** "cloudflare-ini.j2"

Configuration file used with [SWAG](https://hub.docker.com/r/linuxserver/swag) for Certbot and the DNS challenge.

*Only used if `var_should_deploy_with_swag_container` is set to `true`.*

### var_lube_logger_swag_container_image_version

***default***: "amd64-latest"

Docker Image version of [SWAG](https://hub.docker.com/r/linuxserver/swag) Container to use.

*Only used if `var_should_deploy_with_swag_container` is set to `true`.*

### var_lube_logger_swag_container_name

***default:*** "lubelog-swag"

Name of the [SWAG](https://hub.docker.com/r/linuxserver/swag) Container, i.e. value shown under `NAMES` when running `docker ps`.

### var_lube_logger_swag_email_address

***default:*** ""

Email address to be used with the [SWAG](https://hub.docker.com/r/linuxserver/swag) Container's DNS challenge.

*Only used if `var_should_deploy_with_swag_container` is set to `true`.*

### var_lube_logger_swag_tld

***default:*** ""

Top-level domain to used with `lubelogger` sub-domain.

**Example:** "`chucknorris.com`"

- This will yield: `lubelogger.chucknorris.com`

*Only used if `var_should_deploy_with_swag_container` is set to `true`.*

### var_lube_logger_swag_timezome

***default:*** "America/Detroit"

Timezone used in Containers.

### var_should_delete_docker_compose_file

***default:*** false

- If set to `true`: After Docker Compose starts up all Services, then the Docker Compose files used are deleted.
- If set to `false`: Docker Compose files are copied to **target** node and remain in directory specified by the `var_lube_logger_docker_compose_directory` variable.

### var_should_deploy_with_swag_container

***default:*** false

Set to `true` in order use a [SWAG](https://hub.docker.com/r/linuxserver/swag) Container (LetsEncrypt) with Lube Logger; enabling HTTPS/SSL connections to instance.

### var_should_test_docker_compose_copy_only

***default:*** false

*Used only for Molecule testing Scenarios. Most likely you will want to leave the default value.*

Set to `true` to test the output of the generated Docker Compose files in a Molecule Scenario.

## Dependencies

- `community.docker` Collection installed on node running Ansible.
  - You can run `ansible-galaxy install -r requirements.yaml` from Role's directory.

## Example Playbook

```yaml
---
- name: "Example Playbook: Default Lube Logger Settings"
  hosts: all
  gather_facts: false
  vars:
    _username: "chucknorris"


  tasks:

    - name: "Install LubeLogger on my system please!"
      ansible.builtin.include_role:
        name: "aaronvonawesome.lube_logger"
      vars:
        var_lube_logger_container_username: "{{ _username }}"
```

## License

Apache 2.0

## Author Information

| Name | Website |
| --  | -- |
| Aaron von Awesome | https://aaronvonawesome.com |
