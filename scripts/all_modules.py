import pkgutil
import sys

def module_names(excluded_names=None):
    if excluded_names is None:
        excluded_names = set()
    modules = list(pkgutil.iter_modules())
    names = [module[1] for module in modules]
    return [name for name in names if name not in excluded_names]


def main(excluded_names=None):
    for name in module_names(excluded_names=excluded_names):
        print name

if __name__=='__main__':
    filenames = sys.argv[1:]
    excluded_names = []
    for filename in filenames:
        with open(filename) as f:
            for line in f:
                excluded_names.append(line.strip())

    main(excluded_names = excluded_names)
