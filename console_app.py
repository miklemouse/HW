"""Console app

A simple console application that allows user to look up information
about files and rename them.

Sample usage:

$ python3 console_app.py -f testfile -m --tformat=gmt

For more details, please consult help:

$ python3 console_app.py -h
"""

import os
from time import strftime, localtime, gmtime, ctime
import argparse


def main(args):

    print()
    if not args.file:
        if args.size:
            parser.error('-s argument misses the input file. '
                         'Please include it using -f argument')
        if args.mtime:
            parser.error('-m argument misses the input file. '
                         'Please include it using -f argument')
        if args.rename:
            parser.error('--rename argument misses the input file. '
                         'Please include it using -f argument')
    else:
        print(f'Input file name: {args.file}\n')

        if not (args.size or args.mtime or args.rename):
            raise UserWarning('The input file is defined but there '
                              'is nothing to be done with it.')

        stats = os.stat(args.file)

        if args.size:
            print(f'File size in Bytes: {stats.st_size}\n')
        if args.mtime:
            if args.tformat == 'dflt':
                print('Last modified: {Time}\n'.format(
                        Time=strftime("%d %b %H:%M:%S", localtime())
                      ))

            elif args.tformat == 'dtld':
                print('Last modified: {Time}\n'.format(
                        Time=ctime(stats.st_mtime)
                      ))

            elif args.tformat == 'gmt':
                # Outputs time according to the RFC 2822 email standard
                # See https://docs.python.org/3/library/time.html
                print('Last modified (Greenwich Mean Time):\n'
                      '{Time}\n'.format(
                        Time=strftime(
                                '%a, %d %b %Y %H:%M:%S +0000',
                                gmtime()
                            )
                        )
                      )
            else:
                parser.error('Unknown time output format. Please '
                             'define the format as either dflt, '
                             'dtld or gmt using the --tformat flag.')

        if args.rename:
            os.rename(args.file, args.rename)
            print('Renamed successfully!\n'
                  'Old name: {old_name}, '
                  'New name: {new_name}\n'.format(old_name=args.file,
                                                  new_name=args.rename))

    if args.ls:
        print('List of all the files in this directory:')
        files = os.listdir('.')
        for filename in files:
            print(filename)
        print()

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Look up file info and rename files.')

    parser.add_argument('-f',
                        '--file',
                        help='the input file')

    parser.add_argument('-s',
                        '--size',
                        help='print file size in MB',
                        action='store_true')

    parser.add_argument('-m',
                        '--mtime',
                        help='print modification time',
                        action='store_true')

    parser.add_argument('--tformat',
                        help='change the format of the time output '
                             '(choose dflt, dtld or gmt)',
                        default='dflt')

    parser.add_argument('--rename',
                        help='change filename')

    parser.add_argument('--ls',
                        help='list all files in the current dir',
                        action='store_true')

    parser_args = parser.parse_args()

    main(parser_args)
