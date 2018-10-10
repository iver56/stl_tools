from setuptools import setup, Extension

SRC_DIR = "stl_tools"
PACKAGES = [SRC_DIR]

setup(name='stl_tools',
      version='0.3.0',
      install_requires=['numpy', 'scipy', 'matplotlib'],
      description="Generate STL files from numpy arrays and text",
      author='Tristan Hearn',
      author_email='tristanhearn@gmail.com',
      url='https://github.com/thearn/stl_tools',
      license='Apache 2.0',
      packages=['stl_tools'],
      entry_points={
          'console_scripts':
          ['image2stl=stl_tools.image2stl:image2stl']
      }
      )
