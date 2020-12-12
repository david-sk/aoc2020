from importlib import import_module
import sys


if __name__ == '__main__':
    day_number = sys.argv[1] if len(sys.argv) > 1 else None
    if not day_number or not day_number.isdigit():
        print('Usage: python3 -m days [day_number]')
    else:
        module = import_module(f'days.day{day_number}.day{day_number}')
        assert hasattr(module, 'main'), 'main attribute expected in day modules'
        main = getattr(module, 'main')
        assert callable(main), 'main attribute must be a callable'
        main()
