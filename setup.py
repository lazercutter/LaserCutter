from setuptools import setup, find_packages

setup(  name = "LaserSaver",
        version = "0.1",
        description = "A high level python framework for implementing the Lasersaver project to reuse scrap material",
        author = "LaserCutter Group",
        author_email = "acordero1532@gmail.com",
        license = "BSD",
        packages = find_packages('src'),
        package_dir = {'':'src'},
        install_requires = ['numpy', 'configparser', 'imutils', 'Pillow']
)
