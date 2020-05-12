#defining NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
from setuptools import setup, find_packages, Extension

try:
    from Cython.Build import cythonize

    ext_modules = cythonize([
        Extension("fstokenizers.pyrobuf_list", ["fstokenizers/pyrobuf_list.pyx"]),
        Extension("fstokenizers.pyrobuf_util", ["fstokenizers/pyrobuf_util.pyx"]),
        Extension("fstokenizers.sentencepiece_proto", ["fstokenizers/sentencepiece_proto.pyx"]),
        Extension("fstokenizers.tokenization", ["fstokenizers/tokenization.pyx"]),
    ])
except ImportError:
    ext_modules = None

setup(
    name='fstokenizers',
    version='0.0.5',
    packages=find_packages(),
    description='Fairseq Tokenizers with SentencePiece',
    ext_modules=ext_modules
)




