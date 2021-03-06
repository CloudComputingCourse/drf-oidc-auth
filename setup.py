from setuptools import setup

setup(
    name='drf-oidc-auth-cmucc',
    version='0.8',
    packages=['oidc_auth'],
    url='https://github.com/ByteInternet/drf-oidc-auth',
    license='MIT',
    author='Maarten van Schaik',
    author_email='maarten@byte.nl',
    description='OpenID Connect authentication for Django Rest Framework',
    install_requires=[
        'pyjwkest>=1.0.3',
        'django>=1.6.0',
        'djangorestframework>=2.4.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
    ],
)
