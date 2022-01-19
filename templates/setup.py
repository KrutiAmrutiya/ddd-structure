import setuptools
import os

setuptools.setup(
    name=os.path.basename(os.getcwd()),
    version="0.0.2",
    author="Rajat Mishra",
    author_email="rajat@turiean.com",
    description="ddd package for sunrise ",
    long_description="hi hello",
    long_description_content_type="text/markdown",
    url="https://github.com/rajatmishraintntra/djangpocimpro.git",
    project_urls={
        "Bug Tracker": "https://github.com/rajatmishraintntra/djangpocimpro.git/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    install_requires=[
        "pypika",
        "sqlalchemy",
        "django",
        "psycopg2-binary",
        "pinject",
        "python-dotenv",
    ],
    python_requires=">=3.8",
)
