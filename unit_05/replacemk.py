#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
from tempfile import mkstemp
from shutil import move
from os import remove
import sys
 
def replace(source_file_path, pattern, substring):
    fh, target_file_path = mkstemp()
    with open(target_file_path, 'w') as target_file:
        with open(source_file_path, 'r') as source_file:
            for line in source_file:
                target_file.write(line.replace(pattern, substring))
    remove(source_file_path)
    move(target_file_path, source_file_path)
 
 
if __name__ == '__main__':
    if len(sys.argv) == 4:
        replace(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print """Invalid command
        Usage: python replacelinesinfile.py [source_file_path] [pattern] [substring]
        """