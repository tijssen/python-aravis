from setuptools import setup

setup(name = "aravis", 
      version = "0.5",
      description = "pythonic interface to auto-generated aravis python bindings",
      author = "Olivier Roulet-Dubonnet",
      url = 'https://github.com/oroulet/python-aravis',
      packages=["aravis"],
      license = "GNU General Public License",
      zip_safe = True,
      install_requires=["numpy>=1.5.0",
                       ]
      )
