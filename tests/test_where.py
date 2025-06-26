import sys
from unittest import mock
import main

def test_where_name_equal():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'name=geforce rtx 5090 ti']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [{'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'}]

def test_where_name_less():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'name<geforce rtx 5090 ti']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [{' ': ['error']}]

def test_where_name_more():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'name>geforce rtx 5090 ti']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [{' ': ['error']}]


def test_where_brand_equal():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'brand=apple']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [
            {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
            {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
        ]

def test_where_brand_less():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'brand<apple']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [{' ': ['error']}]

def test_where_brand_more():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'brand>apple']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [{' ': ['error']}]


def test_where_price_equal():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'price=2199']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [
            {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'}
        ]

def test_where_price_less():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'price<2199']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [
            {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
            {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
        ]

def test_where_price_more():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'price>2199']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [
            {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'}
        ]

def test_where_rating_equal():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'rating=4.5']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [
            {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'}
        ]

def test_where_rating_less():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'rating<4.6']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [
            {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
            {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
        ]

def test_where_rating_more():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--where', 'rating>4.6']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.where(args.where, test_list_dicts)
        assert products == [
            {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'}
        ]