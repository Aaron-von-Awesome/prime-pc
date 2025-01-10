.PHONY: test reset

test:
	@scenario_names=""
	@for scenario in $$(find molecule/ -maxdepth 1 -mindepth 1 -type d); do \
			scenario_name=$$(basename $$scenario); \
			if [ "$$scenario_name" = "shared" ] ; then \
						continue; \
			fi; \
			echo "Running scenario: $$scenario_name"; \
			molecule --base-config ./molecule/molecule.yml test -s $$scenario_name; \
			scenario_names="$$scenario_names\n$$scenario_name"; \
	done; \
	echo ""; \
	echo ""; \
	echo "Summary of scenarios run:"; \
	echo "$$scenario_names"; \
	echo ""; \
	echo ""

reset:
	@scenario_names=""
	@for scenario in $$(find molecule/ -maxdepth 1 -mindepth 1 -type d); do \
			scenario_name=$$(basename $$scenario); \
			if [ "$$scenario_name" = "shared" ] ; then \
						continue; \
			fi; \
			echo "Reset scenario: $$scenario_name"; \
			molecule --base-config ./molecule/molecule.yml destroy -s $$scenario_name; \
			molecule --base-config ./molecule/molecule.yml reset -s $$scenario_name; \
			scenario_names="$$scenario_names\n$$scenario_name"; \
	done; \
	echo ""; \
	echo ""; \
	echo "Summary of scenarios reset:"; \
	echo "$$scenario_names"; \
	echo ""; \
  echo ""
