import setuptools
import setuptools.command.build_py
import shutil
import os


class BuildPyCommand(setuptools.command.build_py.build_py):
    """Custom build command."""

    def run(self):
        """[summary]"""
        # data = os.listdir("./business")
        # basepath = "micro/"
        # newdata = []
        # for iu in data:
        #     if iu != "__init__.py":
        #         if iu != "__pycache__":
        #             newdata.append(iu)
        # for i in newdata:
        #     shutil.copytree(
        #         "./business/", "./" + basepath + i + "/business", dirs_exist_ok=True
        #     )
        #     folders = os.listdir(os.path.join(basepath + i, "business"))
        #     for ik in folders:
        #         if ik != i and ik != "__init__.py" and ik != "__pycache__":
        #             print(ik, i)
        #             shutil.rmtree(
        #                 os.path.join("./" + basepath + i, "business/" + ik + "/"),
        #                 ignore_errors=False,
        #             )

        #     shutil.copytree(
        #         "./enterprise/", "./" + basepath + i + "/enterprise", dirs_exist_ok=True
        #     )
        #     shutil.copytree(
        #         "./tests/business/" + i + "/",
        #         "./" + basepath + i + "/tests/business/",
        #         dirs_exist_ok=True,
        #     )
        #     shutil.copytree(
        #         "./tests/enterprise/",
        #         "./" + basepath + i + "/tests/enterprise/",
        #         dirs_exist_ok=True,
        #     )
        #     shutil.copytree(
        #         "./infrastructure/shared/",
        #         "./" + basepath + i + "/infrastructure/shared/",
        #         dirs_exist_ok=True,
        #     )
        #     shutil.copytree(
        #         "./tests/infrastructure/",
        #         "./" + basepath + i + "/tests/infrastructure/",
        #         dirs_exist_ok=True,
        #     )
        #     shutil.copytree(
        #         "./templates/", "./" + basepath + i + "/", dirs_exist_ok=True
        #     )
        setuptools.command.build_py.build_py.run(self)


setuptools.setup(
    cmdclass={
        "build_py": BuildPyCommand,
    },
    name="ddd_using_django",
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
