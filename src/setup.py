from setuptools import setup, find_packages

setup(
    name="marl-msac",
    version="0.1.0",
    packages=find_packages(),
    py_modules=[
        "runner_msac",
        "runner_mcsac",
        "runner_mcac",
        "runner_qmix",
        "runner_coma",
        "main",
        "main_qmix_coma",
    ],
)
