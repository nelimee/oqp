"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))
PACKAGE_NAME = "oqp"

# Get the long description from the README file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

# try:
#     import pypandoc
# except ImportError:
#     print("pypandoc is not installed. Please install the [dev] dependencies with "
#           "'pip install {}[dev]'.".format(PACKAGE_NAME))

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(  # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    # There are some restrictions on what makes a valid project name
    # specification here:
    # https://packaging.python.org/specifications/core-metadata/#name
    name=PACKAGE_NAME,  # Required
    # Versions should comply with PEP 440:
    # https://www.python.org/dev/peps/pep-0440/
    #
    # For a discussion on single-sourcing the version across setup.py and the
    # project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version="0.0.1",  # Required
    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description="A collection of Open Quantum Parsers written in pure Python",  # Optional
    # This is an optional longer description of your project that represents
    # the body of text which users will see when they visit PyPI.
    #
    # Often, this is the same as your README, so you can just read it in from
    # that file directly (as we have already done above)
    #
    # This field corresponds to the "Description" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-optional
    long_description=long_description,  # Optional
    # Denotes that our long_description is in Markdown; valid values are
    # text/plain, text/x-rst, and text/markdown
    #
    # Optional if long_description is written in reStructuredText (rst) but
    # required for plain-text or Markdown; if unspecified, "applications should
    # attempt to render [the long_description] as text/x-rst; charset=UTF-8 and
    # fall back to text/plain if it is not valid rst" (see link below)
    #
    # This field corresponds to the "Description-Content-Type" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#description-content-type-optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    # This should be a valid link to your project's main homepage.
    #
    # This field corresponds to the "Home-Page" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#home-page-optional
    url="https://github.com/nelimee/oqp",  # Optional
    # This should be your name or the name of the organization which owns the
    # project.
    author="Adrien Suau",  # Optional
    # This should be a valid email address corresponding to the author listed
    # above.
    author_email="adrien.suau@grenoble-inp.org",  # Optional
    license="Apache 2.0",
    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # "Development Status :: 1 - Planning",
        "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        # "Development Status :: 6 - Mature",
        # "Development Status :: 7 - Inactive",
        # "Framework :: IPython",
        # "Framework :: Jupyter",
        # "Framework :: Pytest",
        # "Framework :: Sphinx",
        # "Framework :: Sphinx :: Extension",
        # "Framework :: Sphinx :: Theme",
        # "Framework :: tox",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        # "Intended Audience :: End Users/Desktop",
        # "Intended Audience :: Information Technology",
        # "Intended Audience :: Other Audience",
        "Intended Audience :: Science/Research",
        # "Intended Audience :: System Administrators",
        # "License :: Aladdin Free Public License (AFPL)",
        # "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        # "License :: CeCILL-B Free Software License Agreement (CECILL-B)",
        # "License :: CeCILL-C Free Software License Agreement (CECILL-C)",
        # "License :: DFSG approved",
        # "License :: Eiffel Forum License (EFL)",
        # "License :: Free For Educational Use",
        # "License :: Free For Home Use",
        # "License :: Free for non-commercial use",
        # "License :: Freely Distributable",
        # "License :: Free To Use But Restricted",
        # "License :: Freeware",
        # "License :: GUST Font License 1.0",
        # "License :: GUST Font License 2006-09-30",
        # "License :: Netscape Public License (NPL)",
        # "License :: Nokia Open Source License (NOKOS)",
        # "License :: OSI Approved",
        # "License :: OSI Approved :: Academic Free License (AFL)",
        "License :: OSI Approved :: Apache Software License",
        # "License :: OSI Approved :: Apple Public Source License",
        # "License :: OSI Approved :: Artistic License",
        # "License :: OSI Approved :: Attribution Assurance License",
        # "License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)",
        # "License :: OSI Approved :: BSD License",
        # "License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)",
        # "License :: OSI Approved :: Common Development and Distribution License 1.0 (CDDL-1.0)",
        # "License :: OSI Approved :: Common Public License",
        # "License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)",
        # "License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)",
        # "License :: OSI Approved :: Eiffel Forum License",
        # "License :: OSI Approved :: European Union Public Licence 1.0 (EUPL 1.0)",
        # "License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)",
        # "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        # "License :: OSI Approved :: GNU Affero General Public License v3",
        # "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        # "License :: OSI Approved :: GNU Free Documentation License (FDL)",
        # "License :: OSI Approved :: GNU General Public License (GPL)",
        # "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        # "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        # "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        # "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        # "License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)",
        # "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
        # "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        # "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        # "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        # "License :: OSI Approved :: IBM Public License",
        # "License :: OSI Approved :: Intel Open Source License",
        # "License :: OSI Approved :: ISC License (ISCL)",
        # "License :: OSI Approved :: Jabber Open Source License",
        # "License :: OSI Approved :: MirOS License (MirOS)",
        # "License :: OSI Approved :: MIT License",
        # "License :: OSI Approved :: MITRE Collaborative Virtual Workspace License (CVW)",
        # "License :: OSI Approved :: Motosoto License",
        # "License :: OSI Approved :: Mozilla Public License 1.0 (MPL)",
        # "License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)",
        # "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        # "License :: OSI Approved :: Nethack General Public License",
        # "License :: OSI Approved :: Nokia Open Source License",
        # "License :: OSI Approved :: Open Group Test Suite License",
        # "License :: OSI Approved :: PostgreSQL License",
        # "License :: OSI Approved :: Python License (CNRI Python License)",
        # "License :: OSI Approved :: Python Software Foundation License",
        # "License :: OSI Approved :: Qt Public License (QPL)",
        # "License :: OSI Approved :: Ricoh Source Code Public License",
        # "License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)",
        # "License :: OSI Approved :: Sleepycat License",
        # "License :: OSI Approved :: Sun Industry Standards Source License (SISSL)",
        # "License :: OSI Approved :: Sun Public License",
        # "License :: OSI Approved :: Universal Permissive License (UPL)",
        # "License :: OSI Approved :: University of Illinois/NCSA Open Source License",
        # "License :: OSI Approved :: Vovida Software License 1.0",
        # "License :: OSI Approved :: W3C License",
        # "License :: OSI Approved :: X.Net License",
        # "License :: OSI Approved :: zlib/libpng License",
        # "License :: OSI Approved :: Zope Public License",
        # "License :: Other/Proprietary License",
        # "License :: Public Domain",
        # "License :: Repoze Public License",
        "Natural Language :: English",
        # "Natural Language :: French",
        # "Operating System :: MacOS",
        # "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent",
        # "Operating System :: Other OS",
        # "Operating System :: POSIX",
        # "Operating System :: POSIX :: BSD",
        # "Operating System :: POSIX :: BSD :: BSD/OS",
        # "Operating System :: POSIX :: BSD :: FreeBSD",
        # "Operating System :: POSIX :: BSD :: NetBSD",
        # "Operating System :: POSIX :: BSD :: OpenBSD",
        # "Operating System :: POSIX :: Linux",
        # "Operating System :: POSIX :: Other",
        # "Operating System :: Unix",
        # "Programming Language :: C",
        # "Programming Language :: C++",
        # "Programming Language :: Cython",
        # "Programming Language :: Java",
        # "Programming Language :: JavaScript",
        # "Programming Language :: Other",
        # "Programming Language :: Other Scripting Engines",
        # "Programming Language :: Python",
        # "Programming Language :: Python :: 3",
        # "Programming Language :: Python :: 3.0",
        # "Programming Language :: Python :: 3.1",
        # "Programming Language :: Python :: 3.2",
        # "Programming Language :: Python :: 3.3",
        # "Programming Language :: Python :: 3.4",
        # "Programming Language :: Python :: 3.5",
        # "Programming Language :: Python :: 3.6",
        # "Programming Language :: Python :: 3.7",
        # "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        # "Programming Language :: Unix Shell",
        "Topic :: Artistic Software",
        # "Topic :: Documentation",
        # "Topic :: Documentation :: Sphinx",
        # "Topic :: Multimedia",
        # "Topic :: Multimedia :: Graphics",
        # "Topic :: Multimedia :: Graphics :: 3D Modeling",
        # "Topic :: Multimedia :: Graphics :: 3D Rendering",
        # "Topic :: Multimedia :: Graphics :: Capture",
        # "Topic :: Multimedia :: Graphics :: Capture :: Digital Camera",
        # "Topic :: Multimedia :: Graphics :: Capture :: Scanners",
        # "Topic :: Multimedia :: Graphics :: Capture :: Screen Capture",
        # "Topic :: Multimedia :: Graphics :: Editors",
        # "Topic :: Multimedia :: Graphics :: Editors :: Raster-Based",
        # "Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
        "Topic :: Multimedia :: Graphics :: Graphics Conversion",
        # "Topic :: Multimedia :: Graphics :: Presentation",
        # "Topic :: Multimedia :: Graphics :: Viewers",
        # "Topic :: Multimedia :: Sound/Audio",
        # "Topic :: Multimedia :: Sound/Audio :: Analysis",
        # "Topic :: Multimedia :: Sound/Audio :: Capture/Recording",
        # "Topic :: Multimedia :: Sound/Audio :: CD Audio",
        # "Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Playing",
        # "Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Ripping",
        # "Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Writing",
        # "Topic :: Multimedia :: Sound/Audio :: Conversion",
        # "Topic :: Multimedia :: Sound/Audio :: Editors",
        # "Topic :: Multimedia :: Sound/Audio :: MIDI",
        # "Topic :: Multimedia :: Sound/Audio :: Mixers",
        # "Topic :: Multimedia :: Sound/Audio :: Players",
        # "Topic :: Multimedia :: Sound/Audio :: Players :: MP3",
        # "Topic :: Multimedia :: Sound/Audio :: Sound Synthesis",
        # "Topic :: Multimedia :: Sound/Audio :: Speech",
        # "Topic :: Multimedia :: Video",
        # "Topic :: Multimedia :: Video :: Capture",
        # "Topic :: Multimedia :: Video :: Conversion",
        # "Topic :: Multimedia :: Video :: Display",
        # "Topic :: Multimedia :: Video :: Non-Linear Editor",
        # "Topic :: Scientific/Engineering",
        # "Topic :: Scientific/Engineering :: Artificial Intelligence",
        # "Topic :: Scientific/Engineering :: Artificial Life",
        # "Topic :: Scientific/Engineering :: Astronomy",
        # "Topic :: Scientific/Engineering :: Atmospheric Science",
        # "Topic :: Scientific/Engineering :: Bio-Informatics",
        # "Topic :: Scientific/Engineering :: Chemistry",
        # "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        # "Topic :: Scientific/Engineering :: GIS",
        # "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        # "Topic :: Scientific/Engineering :: Image Recognition",
        # "Topic :: Scientific/Engineering :: Information Analysis",
        # "Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator",
        # "Topic :: Scientific/Engineering :: Mathematics",
        # "Topic :: Scientific/Engineering :: Medical Science Apps.",
        # "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
        # "Topic :: Security",
        # "Topic :: Security :: Cryptography",
        # "Topic :: Software Development",
        # "Topic :: Software Development :: Assemblers",
        # "Topic :: Software Development :: Bug Tracking",
        # "Topic :: Software Development :: Build Tools",
        # "Topic :: Software Development :: Code Generators",
        # "Topic :: Software Development :: Compilers",
        # "Topic :: Software Development :: Debuggers",
        # "Topic :: Software Development :: Disassemblers",
        # "Topic :: Software Development :: Documentation",
        # "Topic :: Software Development :: Embedded Systems",
        # "Topic :: Software Development :: Internationalization",
        # "Topic :: Software Development :: Interpreters",
        # "Topic :: Software Development :: Libraries",
        # "Topic :: Software Development :: Libraries :: Application Frameworks",
        # "Topic :: Software Development :: Libraries :: Java Libraries",
        # "Topic :: Software Development :: Libraries :: Perl Modules",
        # "Topic :: Software Development :: Libraries :: PHP Classes",
        # "Topic :: Software Development :: Libraries :: Pike Modules",
        # "Topic :: Software Development :: Libraries :: pygame",
        "Topic :: Software Development :: Libraries :: Python Modules",
        # "Topic :: Software Development :: Libraries :: Ruby Modules",
        # "Topic :: Software Development :: Libraries :: Tcl Extensions",
        # "Topic :: Software Development :: Localization",
        # "Topic :: Software Development :: Object Brokering",
        # "Topic :: Software Development :: Object Brokering :: CORBA",
        # "Topic :: Software Development :: Pre-processors",
        # "Topic :: Software Development :: Quality Assurance",
        # "Topic :: Software Development :: Testing",
        # "Topic :: Software Development :: Testing :: Acceptance",
        # "Topic :: Software Development :: Testing :: BDD",
        # "Topic :: Software Development :: Testing :: Mocking",
        # "Topic :: Software Development :: Testing :: Traffic Generation",
        # "Topic :: Software Development :: Testing :: Unit",
        # "Topic :: Software Development :: User Interfaces",
        # "Topic :: Software Development :: Version Control",
        # "Topic :: Software Development :: Version Control :: Bazaar",
        # "Topic :: Software Development :: Version Control :: CVS",
        "Topic :: Software Development :: Version Control :: Git",
        # "Topic :: Software Development :: Version Control :: Mercurial",
        # "Topic :: Software Development :: Version Control :: RCS",
        # "Topic :: Software Development :: Version Control :: SCCS",
        # "Topic :: Software Development :: Widget Sets",
        "Topic :: Utilities",
    ],
    # This field adds keywords for your project which will appear on the
    # project page. What does your project relate to?
    #
    # Note that this is a string of words separated by whitespace, not a list.
    keywords="quantum visualisation openqasm qasm svg",  # Optional
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=["lark-parser"],  # Optional
    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        'dev':  ['pypandoc'],
        'test': ['parameterized'],
    },
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `sample` which
    # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        "Bug Reports": "https://github.com/nelimee/oqp/issues",
        "Source": "https://github.com/nelimee/oqp",
    },
)
