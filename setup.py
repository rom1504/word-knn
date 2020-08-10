"""Setup script."""

from pathlib import Path
import re
import setuptools


if __name__ == "__main__":
    # Read metadata from version.py
    with Path("word_knn/version.py").open(encoding="utf-8") as file:
        metadata = dict(re.findall(r'__([a-z]+)__\s*=\s*"([^"]+)"', file.read()))

    # Read description from README
    with Path(Path(__file__).parent, "README.md").open(encoding="utf-8") as file:
        long_description = file.read()

    # Run setup
    setuptools.setup(
        name="word_knn",
        author=metadata["author"],
        version=metadata["version"],
        install_requires=["numpy", "faiss-cpu-noavx2", "flask", "flask-restful"],
        tests_require=["pytest", "black"],
        dependency_links=[],
        data_files=[(".", ["requirements.txt", "README.md"])],
        entry_points={"console_scripts": ["word_knn=word_knn.__main__:main"]},
        packages=setuptools.find_packages(),
        description=long_description.split("\n")[0],
        long_description=long_description,
        long_description_content_type="text/markdown",
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "Development Status :: 5 - Production/Stable",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
    )
