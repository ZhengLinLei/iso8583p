from setuptools import find_packages, setup

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

if __name__ == "__main__":

    with open("README.rst", "r", encoding="utf-8") as f:
        readme = f.read()

    setup(
        name="iso8583p",
        version="1.0.0",
        author="Zheng Lin Lei",
        author_email="zheng9112003@icloud.com",
        description="A serializer and deserializer of ISO8583 data. Modificable and readable",
        long_description=readme,
        long_description_content_type="text/x-rst",
        license="Apache-2.0",
        url="https://github.com/ZhengLinLei/iso8583-parser",
        package_data={"iso8583": ["py.typed"]},
        zip_safe=False,
        classifiers=classifiers,
        python_requires=">=3.7",
        keywords="iso8583 8583 banking protocol library",
    )
