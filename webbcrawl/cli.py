"""
Usage:
    webbcrawl [options] <path>

Options:
    --help                        show this help
    --include_path                include full path to all files

"""

from webbcrawl import webbcrawl
from webbcrawl.docopt import docopt


def main():
    """Main CLI entrypoint."""
    opt = docopt(__doc__, options_first=True)

    webbcrawl.webbcrawl(str(opt['<path>']), include_path=opt['--include_path'])