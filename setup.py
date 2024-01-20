from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="jesse_image_processing",
    version="0.0.1",
    description="Image processing package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/henriquejessex",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3",
)