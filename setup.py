from setuptools import setup, find_packages

setup(
    name="flow_ai_generix",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "sqlalchemy",
        "mysql-connector-python",
        "tabulate",
        "langchain",
        "langchain-community",
        "openai",
        "crewai",
        "analyst_generix",
        "pyyaml",
        "python-dotenv",
    ],
) 