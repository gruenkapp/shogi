import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name="shogi",
    version="1.1.1.",
    author="gruenkapp",
    author_email="carmensc88c@gmail.com",
    description="Shogi game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gruenkapp/shogi.git",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
)

