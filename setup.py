import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gdeck",
    version="0.0.1",
    author="CelebradoJonathan",
    description="A package for gdeck",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CelebradoJonathan/gdeck/tree/master",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    include_package_data=True,
)