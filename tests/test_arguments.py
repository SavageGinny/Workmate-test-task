import sys
from unittest import mock
import main

def test_parse_args_all_args():
    test_args = ['main.py', '--file', 'products.csv', '--where', 'price<1000', '--aggregate', 'rating=avg']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        assert args.file == 'products.csv'
        assert args.where == 'price<1000'
        assert args.aggregate == 'rating=avg'


def test_parse_args_only_required():
    test_args = ['main.py', '--file', 'products.csv']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        assert args.file == 'products.csv'
        assert args.where is None
        assert args.aggregate is None

