# Copyright (c) Ansible Project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import pytest

from ansible_collections.community.general.plugins.modules import linode
from ansible_collections.community.internal_test_tools.tests.unit.plugins.modules.utils import set_module_args

from .linode_conftest import api_key, auth  # noqa: F401, pylint: disable=unused-import

if not linode.HAS_LINODE:
    pytestmark = pytest.mark.skip('test_linode.py requires the `linode-python` module')


def test_name_is_a_required_parameter(api_key, auth):
    with pytest.raises(SystemExit):
        with set_module_args({}):
            linode.main()
