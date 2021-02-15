from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='Console script for clean snd relocate files in folder',
      url='http://github.com/',
      author='Volodymyr "Skiff" Dunkin',
      author_email='v.dunkan@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:clean'],
                    })
