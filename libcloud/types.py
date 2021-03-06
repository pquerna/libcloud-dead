# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# libcloud.org licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Base types used by other parts of libcloud
"""

class Provider(object):
    """
    Defines for each of the supported providers

    @cvar DUMMY: Example provider
    @cvar EC2: Amazon AWS
    @cvar EC2_EU: Amazon AWS EU
    @cvar RACKSPACE: Rackspace Cloud Servers
    @cvar SLICEHOST: Slicehost.com
    @cvar GOGRID: GoGrid
    @cvar VPSNET: VPS.net
    @cvar LINODE: Linode.com
    @cvar VCLOUD: vmware vCloud
    @cvar RIMUHOSTING: RimuHosting.com
    """
    DUMMY = 0
    EC2 = 1
    EC2_EU = 2
    RACKSPACE = 3
    SLICEHOST = 4
    GOGRID = 5
    VPSNET = 6
    LINODE = 7
    VCLOUD = 8
    RIMUHOSTING = 9

class NodeState(object):
    """
    Standard states for a node

    @cvar RUNNING: Node is running
    @cvar REBOOTING: Node is rebooting
    @cvar TERMINATED: Node is terminated
    @cvar PENDING: Node is pending
    @cvar UNKNOWN: Node state is unknown
    """
    RUNNING = 0
    REBOOTING = 1
    TERMINATED = 2
    PENDING = 3
    UNKNOWN = 4

class InvalidCredsException(Exception):
    """Exception used when invalid credentials are used on a provider."""
    def __init__(self, value='Invalid credentials with the provider'):
        self.value = value
    def __str__(self):
        return repr(self.value)
