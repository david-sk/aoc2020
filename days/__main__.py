from importlib import import_module
import sys


if __name__ == '__main__':
    day_arg = sys.argv[1] if len(sys.argv) > 1 else None
    if not day_arg or not day_arg.isdigit():
        print('Usage: python3 -m days [day_number]')
    else:
        day_package_name = 'day' + ('0' + day_arg if len(day_arg) == 1 else day_arg)
        module = import_module(f'days.{day_package_name}.day{day_arg}')
        assert hasattr(module, 'main'), '`main` attribute expected in day modules'
        main = getattr(module, 'main')
        assert callable(main), '`main` attribute must be a callable'
        main()
