from setuptools import setup

setup(
    name='MyApp',
    version='1.0',
    long_description=__doc__,
    packages=['flaskdemo'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10',
        'Flask-SQLAlchemy>=2.1'
    ]
)