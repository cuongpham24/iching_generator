from setuptools import setup, find_packages

setup(
    name="iching",
    version="0.1.0",
    description="Create iching hexagrams",
    author="Vinson Pham",
    author_email="vinsonpham24@gmail.com",
    packages=find_packages(),  # Automatically find package directories
    install_requires=[
        "numpy",
        "pandas",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
