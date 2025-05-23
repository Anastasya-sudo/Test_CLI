from setuptools import setup, find_packages

setup(
    name="gh-summary",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",  # и другие зависимости
    ],
    entry_points={
        "console_scripts": [
            "gh-summary = gh_summary.__main__:main"
        ],
    },
)
