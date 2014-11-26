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

import argparse
import json
import logging
import os
import sys

import pbr.version
import yaml

__version__ = pbr.version.VersionInfo('explode').version_string()


def explode_data(data, path='output'):
    if type(data) is dict:
        logging.debug("Exploding dict")
        for (k, v) in data.items():
            logging.debug("Recursing to key {0}".format(k))
            explode_data(v, os.path.join(path, k))
    elif type(data) is list:
        logging.debug("Exploding list")
        for x in range(0, len(data)):
            logging.debug("Recursing to list element {0}".format(str(x)))
            explode_data(data[x], os.path.join(path, str(x)))
    else:
        logging.debug("Writing {data} to {path}".format(
            data=data, path=path))
        base_dir = os.path.dirname(path)
        if not os.path.isdir(base_dir):
            logging.debug("Making base directory {0}".format(base_dir))
            os.makedirs(base_dir)
        with open(path, 'w') as outfile:
            outfile.write(str(data))
            outfile.write('\n')


def setup_logging(debug=False):
        if debug:
            level = logging.DEBUG
        else:
            level = logging.INFO
        logging.basicConfig(
            level=level,
            format='%(asctime)s %(levelname)s %(name)s: %(message)s')


def get_arg_parser():
    parser = argparse.ArgumentParser(
        prog='explode',
        description='Explode turns yaml/json into directories and files.')
    parser.add_argument('--version', action='version', version=__version__,
                        help='show version')
    parser.add_argument('--debug', dest='debug', action='store_true',
                        help='show DEBUG level logging')
    parser.add_argument('infile', help='File to process')
    parser.add_argument(
        'outdir', default='.', nargs='?',
        help='Root directory to write into. (default current dir)')
    return parser

def main():

    args = get_arg_parser().parse_args()

    setup_logging(args.debug)

    if args.infile == '-':
        infile = sys.stdin
    else:
        infile = open(args.infile)

    intext = infile.read()
    try:
        data = json.loads(intext)
    except ValueError:
        data = yaml.load(intext)
    explode_data(data, args.outdir)

if __name__ == '__main__':
    main()
