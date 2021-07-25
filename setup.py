from setuptools import setup, find_packages
import glob

def requirements():
    """List requirements from requirement.txt file
    """
    if glob.glob('requirements.txt'):
        with open('requirements.txt') as requirement_file:
            return [req.strip() for req	in requirement_file.readlines()]
    else:
        return []

setup(name="media_controller",
      version="0.0.1",
      description="A play/pause media button using webcam",
      author="Valentin Gautier",
      author_email="valentueur@gmail.com",
      packages=find_packages('src'),
      package_dir={'': 'src'},
      install_requires=requirements(),
      entry_points = {
          "console_scripts": [
              "media_controller=media_controller.app:app"
          ]
      },
      license="Apache 2.0")