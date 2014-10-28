#!/usr/bin/env python
# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import os
import sys

import yaml


def explode_data(data, path='output'):
    if type(data) is dict:
        for (k, v) in data.items():
            explode_data(v, os.path.join(path, k))
    elif type(data) is list:
        for x in range(0, len(data)):
            explode_data(data[x], os.path.join(path, str(x)))
    else:
        if not os.path.isdir(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
        with open(path, 'w') as outfile:
            outfile.write(str(data))
            outfile.write('\n')


def main():
    intext = open(sys.argv[1]).read()
    outpath = sys.argv[2]
    try:
        x = json.loads(intext)
    except ValueError:
        x = yaml.load(intext)
    explode_data(x, outpath)

if __name__ == '__main__':
    main()
