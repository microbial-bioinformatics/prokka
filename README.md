# Prokka


# Introduction

[![Build Status](https://travis-ci.org/microbial_bioinformatics/prokka.svg?branch=master)](https://travis-ci.org/microbial_bioinformatics/prokka)

# Usage 
```
usage: prokka [options] *.fa

Prokka: xxxx

positional arguments:
  input_files           FASTA files which may be gzipped

optional arguments:
  -h, --help            show this help message and exit
  --threads THREADS, -t THREADS
                        Number of threads [1]
  --verbose, -v         Turn on more debugging output [False]
  --version             show program's version number and exit
```

# Installation
There are a number of installation methods. Choosing the right one for the system you use will make life easier. 

* Linux/OSX/Windows/Cloud
  * Docker
  * Anaconda/Bioconda
* Linux 
  * Debian Testing/Ubuntu 16.04 (Xenial)
  * Linuxbrew
* OSX
  * HomeBrew

# Linux/OSX/Windows/Cloud
## Docker 
Install [Docker](https://www.docker.com/).  We have a docker container which gets automatically built from the latest version of Prokka. To install it:

```
docker pull microbial_bioinformatics/prokka
```

To use it you would use a command such as this (substituting in your directories), where your files are assumed to be stored in /home/ubuntu/data:
```
docker run --rm -it -v /home/ubuntu/data:/data sangerpathogens/prokka prokka xxxxx
```

## Anaconda
Install [Anaconda](https://www.continuum.io/downloads) with Python 3. Then install the dependancies using conda and the software using pip:

```
conda config --add channels bioconda
conda install git
pip install git+git://github.com/microbial_bioinformatics/prokka.git
```

## Linux
The instructions for Linux assume you have root (sudo) on your machine. 

### Debian Testing/Ubuntu 16.04 (Xenial)
```
apt-get update -qq
apt-get install -y git python3 python3-setuptools python3-biopython python3-pip
pip3 install git+git://github.com/microbial_bioinformatics/prokka.git
```

### Linuxbrew
First install [LinuxBrew](http://linuxbrew.sh/), then follow the instructions below.

```
brew tap homebrew/science
brew update
brew install python3
pip3 install git+git://github.com/microbial_bioinformatics/prokka.git
```

## OSX

### Homebrew
First install [HomeBrew](http://brew.sh/), then follow the instructions below.

```
brew tap homebrew/science
brew update
brew install python3
pip3 install git+git://github.com/microbial_bioinformatics/prokka.git
```

