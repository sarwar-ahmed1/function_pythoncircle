# this file tells us who wrote the code # pylint: disable=C0114,W4901
from distutils.core import setup

setup(
    name="pythoncircle",
    version="1.0",
    description="Python circle example",
    author="Nader Akmel",
    author_email="naderakmel@kubrickgroup.com",
    url="https://dev.azure.com/kubrick-training/ce05/_git/pythoncircle_bus02",
    license="MIT",
    packages=["pythoncircle"],
    tests_require=["pytest"],
)
