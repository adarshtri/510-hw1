import setuptools

setuptools.setup(
    name="Test_package", 
    version="1.0.0",
    author="Rashi",
    author_email="rashi9.agarwal96@gmail.com",
    description="a test package",
    url="https://github.com/adarshtri/510-hw1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.6',
)
