Date: 2014-04-21
Title: Making __git_ps1 and virtualenvwrapper play nicely
Tagline: For a more beautiful bash prompt
Slug: git_ps1_virtualenvwrapper_friendly
Category: Blog
Tags: git, python, virtualenv

I had to reinstall my ubuntu installation today after I completely broke
it upgrading from 13.04 to 14.04. This meant that one of my first tasks
was to reconfigure my shell how I liked it. Upon searching around, I found
that the way I had been including the git branch status in my bash prompt
had been superceded by the following new syntax:

```bash
export GIT_PS1_SHOWUNTRACKEDFILES=1
export GIT_PS1_SHOWUPSTREAM="auto"
export GIT_PS1_SHOWCOLORHINTS=1
export GIT_PS1_SHOWDIRTYSTATE=1

export PROMPT_COMMAND='__git_ps1'
```

which has a few nice updates to it! It will not only tell you which branch
you are on, but it will also tell you the status of the branch AND colour
it accordingly. Notice the use of ``PROMPT_COMMAND`` in order to allow
the ``__git_ps1`` command to properly set colours in bash. ``PROMPT_COMMAND``
is a special bash command that is executed before every prompt is updated.
Hence the syntax used (excluding the ``$(...)``).

Unfortunately, this messed up how virtualenvwrapper was displaying my 
active virtualenv, which was no use to me at all. After some tinkering,
I found two pieces of important information:

  1. ``__git_ps1`` can take two parameters. The first a string to place
     before the branch information, and the second a string to place after.
  2. ``PROMPT_COMMAND`` can take a string of commands to call, seperated
     by semicolons.

Therefore, we can make a nice prompt that is friendly to both our git 
status and our virtualenv status as follows:

```bash
export GIT_PS1_SHOWUNTRACKEDFILES=1
export GIT_PS1_SHOWUPSTREAM="auto"
export GIT_PS1_SHOWCOLORHINTS=1
export GIT_PS1_SHOWDIRTYSTATE=1
export VIRTUAL_ENV_DISABLE_PROMPT=1

set_active_venv() {
    export ACTIVE_VENV=""
    if [ "$VIRTUAL_ENV" != "" ]; then
        export ACTIVE_VENV="(`basename \"$VIRTUAL_ENV\"`)"
    fi
}

export PROMPT_COMMAND='set_active_venv; __git_ps1 "${ACTIVE_VENV}\w" "\\\$ "'
```

We have to set ``VIRTUAL_ENV_DISABLE_PROMPT=1`` in order to prevent virtualenvwrapper
from providing its normal behaviour. We then just set our own environment variable to
provide the same functionality!
