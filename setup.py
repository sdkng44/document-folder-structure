from setuptools import setup, find_packages

setup(
    name="document-folder-structure",
    version="0.1.0",
    description="Automatic Markdown Documentation and Directory Tree Generator",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="sdkng44",
    author_email="sdkng44@gmail.com",
    url="https://github.com/sdkng44/document-folder-structure",
    license="Apache-2.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["openpyxl"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "document-folder-structure = document_folder_structure.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Documentation",
    ],
    project_urls={
        "Source": "https://github.com/sdkng44/document-folder-structure",
        "Bug Tracker": "https://github.com/sdkng44/document-folder-structure/issues",
    },
)
