import setuptools

setuptools.setup(
  name = 'headerz',
  packages = ['headerz'],
  version = '0.1',
  license='MIT',
  description = 'A simple package for parsing a header string from sniffer app An android/browser on PC',
  author = 'Karjok Pangesty',
  author_email = 'karjok.pangesty@gmail.com',
  url = 'https://github.com/karjok/headerz',
  download_url = 'https://github.com/karjok/headerz/archive/v_01.tar.gz',
  keywords = ['header parser', 'header string', 'parsing header string'],
 
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3'
  ],
)
