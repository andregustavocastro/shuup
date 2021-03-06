# This file is part of Shuup.
#
# Copyright (c) 2012-2017, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

import shuup.apps


class AppConfig(shuup.apps.AppConfig):
    name = __name__
    verbose_name = _("Simple CMS")
    label = "shuup_simple_cms"

    provides = {
        "front_urls_post": [__name__ + ".urls:urlpatterns"],
        "admin_module": [
            "shuup.simple_cms.admin_module:SimpleCMSAdminModule"
        ],
        "front_template_helper_namespace": [
            "shuup.simple_cms.template_helpers:SimpleCMSTemplateHelpers"
        ],
        "xtheme_plugin": [
            "shuup.simple_cms.plugins:PageLinksPlugin"
        ],
    }


default_app_config = __name__ + ".AppConfig"
