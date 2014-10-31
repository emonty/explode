=======
explode
=======

Sometimes you need to drop some data onto a server.

YAML and JSON are both great for that, except that they suck to be
consumed in shell scripts. `jq` is an excellent tool for consuming parts
of a JSON file in a shell script, but similar to `find` it has its own syntax
and semantics that need to be learned.

Shell scripts are already great at consuming text files and processing
directory trees, and if you need to do fancy things and you're doing them
in shell, you probably have already learned all of the finer points of `find`.

`explode` will take a JSON or a YAML file and turn it into a directory
structure with simple text files containing the values. Dictionary keys
become directories. Lists become directories named for the list index. Booleans
are rendered as True or False. There is no support for anything else.

* Free software: Apache license
* Source: http://github.com/emonty/explode
