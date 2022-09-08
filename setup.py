import setuptools
import pkg_resources

with open("README.md", "r", encoding="utf-8") as fh:
    long_description : str = fh.read()

def get_requirements() -> list:
    """Return requirements as list
	
	from: https://stackoverflow.com/questions/69842651/parse-error-in-pip-e-gith-expected-wabcd
	"""
    with open('requirements.txt') as f:
        packages : list = []
        for line in f:
            line = line.strip()
            # let's also ignore empty lines and comments
            if not line or line.startswith('#'):
                continue
            if 'https://' in line:
                # tail = line.rsplit('/', 1)[1]
                # tail = tail.split('#')[0]
                # line = tail.replace('@', '==').replace('.git', '')
                if (line.count('#egg=') != 1) or (not line.startswith('-e ')):
                    raise ValueError(f'cant parse required package: {line}')

                pckgname : str = line.split('#egg=')[-1]

                line = pckgname + ' @ ' + line.split('-e ', 1)[-1].strip()

            packages.append(line)
    return packages

setuptools.setup(
    name = "inline_todo",
    version = "0.0.1",
    author = "Michael Ivanitskiy",
    author_email = "mivanits@umich.edu",
    description = "configurable tool for scraping source files for todo comments",
    long_description = long_description,
    long_description_content_type = "text/markdown",
	install_requires = get_requirements(),
	scripts = ['scripts/inline_todo.py'],
    url = "https://github.com/mivanit/inline-todo",
    project_urls = {
        "Bug Tracker": "https://github.com/mivanit/inline-todo/issues",
    },
	classifiers = [
		"Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GPL-2.0 License",
        "Operating System :: OS Independent",
    ],
    packages = ["inline_todo"],
    python_requires = ">=3.10",
	keywords = "todo markdown pandoc html",
)