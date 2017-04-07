MimiBot
=======

### Prerequisites

*TLDR -* Install python 2.7, pip, and virtualenv

Make sure you have python 2.7+ installed
```bash
zac@macbook ~/projects $ python
Python 2.7.10 (default, Jul 30 2016, 19:40:32) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()
```

Make sure you have the latest version of pip installed
```bash
# first run this
pip -V
```

If you see something like 
```bash
pip 1.5.6 from /Library/Python/2.7/site-packages/pip-1.5.6-py2.7.egg 
(python 2.7)
```

Then you're probably good... else visit https://pip.readthedocs.io/en/stable/installing/

Finally install virtualenv

```bash
zac@macbook ~/projects $ virtualenv --version
13.1.2
```

If you see something like
```bash
zac@macbook ~/projects $ virtualenv --version
-bash: virtualenv: command not found
```

Then see this for installation https://virtualenv.pypa.io/en/stable/installation/

### Getting Started

```bash
# clone this repo

# create and source a virtualenv
virtualenv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# you'll need some environment variables
# ask another contributor to this repo to get them to you

# create a .env file
touch .env

# and then put the secrets in that file -- it should look something like...
export MIMI_BOT_TOKEN="xxX-some-secret-Xxx"
export MIMI_BOT_ID="S0P3RS3CRE7"

# source it
source .env
```

### Running Tests
```bash
make test
```
