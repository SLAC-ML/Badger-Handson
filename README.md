# Badger Hands-on Session

Welcome to the Badger hands-on sessions! Please read through this simple guide before the hands-on session to get ready for it :)

## Prerequisites

Please do these before the hands-on session, since the setup could take tens of minutes or even longer, based on your network condition. Thank you!

### 0. Clone the repo

Run `git pull https://github.com/SLAC-ML/Badger-Handson.git` in terminal to get this repo on your computer, then `cd` to the root of the cloned repo.

### 1. Setup a Badger environment

Badger and its plugins are python-based packages/scripts, so a proper python environment is needed. The easiest way to play with Badger w/o messing w/ your system is through [docker](https://www.docker.com/). If you feel confident and would like to install Badger directly on your system, [conda](https://docs.conda.io/en/latest/) would be a good choice. Please choose one of the two paths below to get Badger installed on your computer.

#### Install Badger with docker

1. [Install docker](https://docs.docker.com/get-docker/) if you haven't done so already. You can follow the tutorial showed up when you launch docker for the first time to get a feeling of what docker is about
2. Run `docker pull slacml/badger:handson` to pull the pre-configured Badger docker image onto your computer. The docker image is around 6GB so it would take some time to get downloaded. When the pulling is done, run `docker images` to make sure the image is listed there
3. [Install XQuartz](https://www.xquartz.org/) if you are using a mac. In order to expose the GUI from within the Badger docker images, we need to forward the GUI to an X window system, which is provided by XQuartz

#### Install Badger with conda

1. [Install conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation) if you haven't done so already
2. Run `conda env list` to make sure you don't have an environment named `badger`, then run `conda env create -f environment.yml`. It would take some time (~30min) since there are some bulky packages to be resolved/installed in the predefined conda env

## Beginner's Tasks


Questions? Contact us on [slack](https://join.slack.com/share/enQtMzE2MjQ2OTI5MzY5OC00NzdkODkxY2NjN2IzYjIxOTBiMTBkMTQwMTVhYTYxOTc2NWEyYjczYTI2YjNkZjk4MzgzM2EyODJjNGY1YzE1), [email](mailto:zhezhang@slac.stanford.edu)