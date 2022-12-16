#!/usr/bin/env python
# -*- coding: utf-8 -*-
u"""Entry point of this script/app.

Last modified in 2022-12-16

Python version 2.7.15 (Side Effects Software Houdini 18.0.460)

This is the file to run from Side Effects Software Houdini. It is advisable to
create a shelf button to run this app from there.

Important:
    Project structure:

Example:
    How a shelf button can be written::

        # -*- coding: utf-8 -*-
        u'''Houdini shelf button for a custom app to run.

        This is a (Houdini) shelf button example on how to create a button for custom
        python scripts.

        The ``mystuff`` module should be saved at the following folder (remember to
        change the username and the Houdini version)::

            C:\\\\Users\\\\web\\\\Documents\\\\houdini18.0\\\\python2.7libs

        The ``python2.7libs`` folder does not exist initally. It needs to be created
        (see References).

        Important:
            The ``mystuff`` module acts as a bridge. For some reason, Houdini crashes
            every time I try to add a path to the ``sys.path`` list from inside this
            shelf button.

            From the ``mystuff`` module, it works fine.

        References:
            `Python script locations`_

        .. _Python script locations:
        https://www.sidefx.com/docs/houdini/hom/locations.html#general-tips
        '''

        import mystuff
        reload(mystuff)

Example:
    How a bridge file can be written::

        # -*- coding: utf-8 -*-
        u'''Houdini bridge file to enable the import of custom scripts.

        This module acts as a bridge. It enables the import of custom python
        applications.

        Important:
            For some reason, Houdini crashes every time I try to add a path to the
            ``sys.path`` list from inside the shelf button.

            From the this module, I can add without problems.

        Note:
            This file should be placed at the following folder (remember to
            change the username and the Houdini version)::

                C:\\\\Users\\\\web\\\\Documents\\\\houdini18.0\\\\python2.7libs

            The ``python2.7libs`` folder does not exist initally. It needs to be created
            (see References).

        References:
            `Python script locations`_

        .. _Python script locations:
        https://www.sidefx.com/docs/houdini/hom/locations.html#general-tips

        '''

        import sys

        module_path = 'F:\\d_flux\\libraries\\scripts\\Houdini\\python-houdini-boilerplate\\src'

        # Includes the module path in sys.path if it is not already there:
        for path in sys.path:
            if path == module_path:
                break
        else:
            sys.path.insert(0, module_path)

        import main
        reload(main)

Note:
    If **unit tests** are in place, this is how they can be run::

        python -m unittest discover

    If coverage is being used too, this is how it can be run::

        coverage erase
        coverage run -m unittest discover
        coverage html

    In this starter kit, it is not necessary to run those commands manually,
    though. They are preconfigure in the ``package.json`` file as scripts.

Important:
    Sphinx (and its packages) **MUST** be installed in the virtual environment
    in order to avoid import errors.

    Having multiple Python versions on the machine and Sphinx installed in one
    of them, leads to confusion and hard to track bugs.

Note:
    How to generate the requirements.txt::

        pip freeze > requirements.txt

    How to install packages from requirements.txt::

        pip install -r requirements.txt

Note:
    To exclude certain modules from being documented, it is necessary to pass
    them as arguments to ``sphinx-apidoc``::

        sphinx-apidoc --force -o ./docs/sphinx/source ./src ./src/activerecord/db_credentials.py

    The example above is in the **package.json** file as the ``build:source:doc`` script.

References:
    `sphinx-apidoc ignoring some modules/packages`_

.. _sphinx-apidoc ignoring some modules/packages:
   https://chadrick-kwag.net/sphinx-apidoc-ignoring-some-modules-packages/
"""

import os
import sys

import hou

message = "Hello from the starter kit app for Houdini!"

def main():
    u"""The main function to execute the entire project/application.
    """
    print(message)


main()