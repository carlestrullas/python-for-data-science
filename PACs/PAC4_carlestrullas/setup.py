"""
Setup script for PAC4 Student Performance package.
Defines installation, dependencies, and metadata for packaging and distribution.
"""

from setuptools import find_packages, setup

setup(
    name="pac4_student_performance",
    version="0.1.0",
    description="Analysis tools for student performance in Catalonia (PAC4)",
    author="Carles Trullas",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas==1.5.3",
        "openpyxl==3.1.2",
        "numpy==1.26.0",
        "pytest==7.4.2",
    ],
    python_requires=">=3.12",
)
