import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mt2x",
    version="0.0.1",
    author="berbeq",
    author_email="antonkotten@gmail.com",
    description="A math package for gymnasium studies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Berbeq/mt2x",
    project_urls={
        "Bug Tracker": "https://github.com/Berbeq/mt2x/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
)
