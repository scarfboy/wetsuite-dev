from setuptools import setup, find_packages

setup(
    name='wetsuite',
    version='0.0.10',
    classifiers=['Development Status :: 2 - Pre-Alpha', 'Programming Language :: Python :: 3', 'Topic :: Text Processing :: Linguistic'],
    url='https://github.com/scarfboy/wetsuite.git',
    author='scarfboy',
    author_email='scarfboy@gmail.com',
    description='Wetsuite',
    packages=['wetsuite.datasets', 'wetsuite.helpers', 'wetsuite.phrases'],
    package_dir={"": "src"},
    python_requires=">=3",
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1', 'spacy', 'spacy-transformers', 'requests'], # merely suggested: 'easyocr', 
    extras_require={
        'spacy-cpu': 'spacy',
        'spacy-cuda110': 'spacy[cuda110]',
        'fastlang': ['spacy_fastlang','fasttext'],
        'ocr':'easyocr',
        # all?
    },
)
