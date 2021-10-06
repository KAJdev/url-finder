import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='url_finder',  
     version='0.1',
     author="kajdev",
     description="An easy utility to extract links from text.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/kajdev/url-finder",
     packages=["url_finder"],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )