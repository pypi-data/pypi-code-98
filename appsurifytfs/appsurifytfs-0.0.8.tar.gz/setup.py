from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='appsurifytfs',
  version='0.0.8',
  description='Package used to integrate Appsurify with TFS',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type='text/markdown',
  url='https://appsurify.com',  
  author='James Farrier',
  author_email='jamesfarrier@appsurify.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='appsurify', 
  packages=find_packages(),
  entry_points={
        'console_scripts': ['appsurifytfs=appsurifytfs.appsurifytfs:appsurifytfs']
    },
  install_requires=['PyYAML', 'requests']
)
