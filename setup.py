from setuptools import setup, find_packages


setup(
    name='arcade',
    version="0.0.1",
    packages=find_packages(),
    install_requires=['numpy', 'gym'],

    # metadata for upload to PyPI
    author="Todd Young",
    author_email="youngmt1@ornl.gov",
    description="Algorithms for OpenAI's retro arcade games.",
    license="MIT",
    keywords="reinforcement learning, control",
    url="https://github.com/yngtodd/arcade",
)

