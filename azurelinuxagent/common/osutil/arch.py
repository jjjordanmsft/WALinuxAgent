#
# Copyright 2014 Microsoft Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Requires Python 2.4+ and Openssl 1.0+
#

import os
import re
import pwd
import shutil
import socket
import array
import struct
import fcntl
import time
import base64
import azurelinuxagent.common.logger as logger
import azurelinuxagent.common.utils.fileutil as fileutil
import azurelinuxagent.common.utils.shellutil as shellutil
import azurelinuxagent.common.utils.textutil as textutil
from azurelinuxagent.common.osutil.default import DefaultOSUtil

class ArchOSUtil(DefaultOSUtil):
    def __init__(self):
        super(ArchOSUtil, self).__init__()

    def restart_ssh_service(self):
        return shellutil.run("systemctl restart sshd.service", chk_err=False)

    def stop_agent_service(self):
        return shellutil.run("systemctl stop waagent.service", chk_err=False)

    def start_agent_service(self):
        return shellutil.run("systemctl start waagent.service", chk_err=False)
    
    def register_agent_service(self):
        return shellutil.run("systemctl enable waagent.service", chk_err=False)
    
    def unregister_agent_service(self):
        return shellutil.run("systemctl disable waagent.service", chk_err=False)
    
    def get_dhcp_lease_endpoint(self):
        return self.get_endpoint_from_leases_path('/var/lib/dhclient/dhclient.leases')
    
    def is_dhcp_enabled(self):
        return True
    
    def stop_dhcp_service(self):
        return shellutil.run("systemctl stop dhclient@eth0.service")
    
    def start_dhcp_service(self):
        return shellutil.run("systemctl start dhclient@eth0.service")
