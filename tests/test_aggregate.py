import sys
from unittest import mock
import main

def test_aggregate_rating_avg():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'rating=avg']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {'avg': [4.55]}

def test_aggregate_rating_min():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'rating=min']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {'min': [4.4]}

def test_aggregate_rating_max():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'rating=max']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {'max': [4.7]}

def test_aggregate_price_avg():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'price=avg']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {'avg': [1474]}

def test_aggregate_price_min():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'price=min']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {'min': [199]}

def test_aggregate_price_max():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'price=max']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {'max': [2599]}

def test_aggregate_brand_avg():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'brand=avg']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {' ': ['error']}

def test_aggregate_brand_min():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'brand=min']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {' ': ['error']}

def test_aggregate_brand_max():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'brand=max']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {' ': ['error']}

def test_aggregate_name_avg():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'name=avg']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {' ': ['error']}

def test_aggregate_name_min():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'name=min']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {' ': ['error']}

def test_aggregate_name_max():
    test_list_dicts = [
        {'name': 'MacBook Air 12 pro', 'brand': 'apple', 'price': '2599', 'rating': '4.7'},
        {'name': 'geforce rtx 5090 ti', 'brand': 'geforce', 'price': '2199', 'rating': '4.5'},
        {'name': 'samsung galaxy a35', 'brand': 'samsung', 'price': '199', 'rating': '4.6'},
        {'name': 'iphone 16 mini', 'brand': 'apple', 'price': '899', 'rating': '4.4'}
    ]
    test_args = ['main.py', '--file', 'products.csv', '--aggregate', 'name=max']
    with mock.patch.object(sys, 'argv', test_args):
        args = main.args_parse()
        products = main.aggregate(args.aggregate, test_list_dicts)
        assert products == {' ': ['error']}
