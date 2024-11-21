from setuptools import setup, find_packages

setup(
    name="flyio-db-demo",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi>=0.115.5",
        "uvicorn>=0.32.1",
    ],
    extras_require={
        "test": [
            "pytest>=8.3.3",
            "httpx>=0.27.0",
        ],
    },
    python_requires=">=3.8",
)
