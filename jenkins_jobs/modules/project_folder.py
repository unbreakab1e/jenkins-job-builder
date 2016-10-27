# -*- coding: utf-8 -*-
# Copyright (C) 2016 Ivan Kukharchuk <ikukharchuk@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


"""
The folder Project module handles creating Folders.
You may specify ``folder`` in the ``project-type`` attribute of
the :ref:`Job` definition.

Requires the Jenkins :jenkins-wiki:`CloudBees Folders Plugin
<CloudBees+Folders+Plugin>`.

In order to use it for job-template you have to escape the curly braces by
doubling them in the DSL: { -> {{ , otherwise it will be interpreted by the
python str.format() command.

:Job Parameters:
    * **None**

Job example:

    .. literalinclude::
      /../../tests/yamlparser/fixtures/project_flow_template001.yaml

Job template example:

    .. literalinclude::
      /../../tests/yamlparser/fixtures/project_flow_template002.yaml

Job example runninng a DSL file from the workspace:

    .. literalinclude::
      /../../tests/yamlparser/fixtures/project_flow_template003.yaml

"""

import xml.etree.ElementTree as XML

import jenkins_jobs.modules.base


class Folder(jenkins_jobs.modules.base.Base):
    sequence = 0

    def root_xml(self, data):
        xml_parent = XML.Element('com.cloudbees.hudson.plugins.folder.Folder')

        return xml_parent
