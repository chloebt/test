#! /usr/bin/env python

import codecs, re, sys, os

def main():
    import argparse

    stream = codecs.open(sys.argv[1], 'r', 'utf-8')
    for line in stream:
        print line.strip()

if __name__ == '__main__':
    main()
