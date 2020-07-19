from setuptools import setup, find_packages
setup(
    name="apx_test",
    version="0.1",
    packages=find_packages(),
    scripts=['APXClass.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=['docutils>=0.3'],

    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst', '*.asprojx', '*.dll'],
        # And include any *.msg files found in the 'hello' package, too:
        'hello': ['*.msg'],
    },

    # metadata for upload to PyPI
    author="Me",
    author_email="2533450204@qq.com",
    description="This is an Example Package",
    license="PSF",
    keywords="APX examples",

    # could also include long_description, download_url, classifiers, etc.
)