import pip
import importlib

def importWithAutoInstall(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        pip.main(['install', package])
    return importlib.import_module(package)
# Example
if __name__ == '__main__':
    scrapy = importWithAutoInstall('scrapy')
    print(scrapy)