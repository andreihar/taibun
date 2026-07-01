import argparse
import sys
from taibun import Converter, Tokeniser

def main():
    parser = argparse.ArgumentParser(
        prog='taibun',
        description='Taiwanese Hokkien transliterator and tokeniser',
    )
    subparsers = parser.add_subparsers(dest='command', required=True)

    convert = subparsers.add_parser('convert', help='transliterate text into the chosen transliteration system')
    convert.add_argument('input', nargs='+')
    convert.add_argument(
        '-s', '--system', default='Tailo',
        choices=['Tailo', 'POJ', 'Zhuyin', 'TLPA', 'Pingyim', 'Tongiong', 'IPA'],
        help='transliteration system (default: Tailo)',
    )
    convert.add_argument(
        '-d', '--dialect', default='south',
        choices=['south', 'north', 'singapore'],
        help='dialect variant (default: south)',
    )
    convert.add_argument(
        '-f', '--format', default='mark',
        choices=['mark', 'number', 'strip'],
        help='tone representation (default: mark)',
    )

    tokenise = subparsers.add_parser('tokenise', help='split text into word tokens')
    tokenise.add_argument('input', nargs='+')
    tokenise.add_argument(
        '--no-keep-original', dest='keep_original', action='store_false', default=True,
        help='normalise tokens to traditional characters instead of preserving original input',
    )

    args = parser.parse_args()

    text = args.input if args.input is not None else sys.stdin.read()

    if args.command == 'convert':
        c = Converter(args.system, args.dialect, args.format)
        print(c.get(text))
    else:
        tokens = Tokeniser(keep_original=args.keep_original).tokenise(text)
        print('\n'.join(tokens))
