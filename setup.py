import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# taken from https://github.com/CEA-COSMIC/ModOpt/blob/master/setup.py
with open('requirements.txt') as open_file:
    install_requires = open_file.read()

setuptools.setup(
    name="score-mri",
    version="0.0.1",
    author="Hyungjin Chung",
    author_email="harry93001@gmail.com",
    description="Score-based diffusion models for accelerated MRI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HJ-harry/score-MRI",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    python_requires='>=3.6',
)
