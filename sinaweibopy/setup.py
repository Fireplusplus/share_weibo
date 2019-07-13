from distutils.core import setup

import weibo

kw = {
    "name": 'sinaweibopy',
    "version": weibo.__version__,
    "description": 'Sina Weibo OAuth 2 API Python SDK',
    "long_description": open('README', 'r').read(),
    "author": 'Michael Liao',
    "author_email": 'askxuefeng@gmail.com',
    "url": 'https://github.com/michaelliao/sinaweibopy',
    "download_url": 'https://github.com/michaelliao/sinaweibopy',
    "py_modules": ['weibo'],
    "classifiers": [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
}

setup(**kw)
