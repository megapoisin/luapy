import pathlib
import setuptools

setuptools.setup(
    name="lua.py",
    version="0.1.0",
    description="A package that implements the Roblox API easily.",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/megapoisin/luapy",
    author="megapoisin",
    license="The Unlicense",
    project_urls={
        "Source Code": "https://github.com/megapoisin/luapy",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Utilities"
    ],
    python_requires=">=3.10,<3.14",
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["luapy = luapy.cli:main"]}
)