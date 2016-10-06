import os
from os import remove
import codecs
from shutil import move
import re
DIR = 'book'


def manifest(target_dir=DIR):
    """given a corpus directory, make indexed text objects from it"""
    texts = []
    for (root, _, files) in os.walk(target_dir):
        for fn in files:
            if fn[0] == '.':
                pass
            else:
                path = os.path.join(root, fn)
                texts.append(path)
    return texts


def add_header(fn, fin, fout):
    line = fin.readline().strip()
    path = os.path.split(fn)
    if line != '---' and path[0] == 'book':
        title = re.sub(r'#+', '', line)
        yaml_header = """---
layout: page
title: {title}
---""".format(**locals())
        fout.write(yaml_header)
    elif line != '---' and path[0] != 'book':
        title = re.sub(r'#+', '', line)
        yaml_header = """---
layout: lesson
title: {title}
---""".format(**locals())
        fout.write(yaml_header)
    else:
        fout.write('---\n')


def convert_file(fn, header=True):
    with codecs.open(fn, 'r+', 'utf8') as fin:
        with codecs.open(fn + '_temp', 'w', 'utf8') as fout:
            if header:
                add_header(fn, fin, fout)
            for line in fin.readlines():
                line = convert_link(line)
                fout.write(line)
        remove(fn)
        move(fn + '_temp', fn)


def convert_link(line):
    line = re.sub(r'\]\((?!\/)', '/', line)
    line = re.sub(r'\]\((?!\/book|\/assets)', '](/book/', line)    
    line = re.sub(r'\/\/', '/', line)
    line = re.sub(r'\.md\)$', ')', line)
    return line


def main():
    for fn in manifest():
        convert_file(fn)
    convert_file('_includes/SUMMARY.md', False)


if __name__ == '__main__':
    main()
