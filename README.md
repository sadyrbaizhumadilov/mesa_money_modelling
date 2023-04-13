# mesa_money_modelling
Mesa: Agent-based modeling in Python 3+
=========================================

.. image:: https://github.com/projectmesa/mesa/workflows/build/badge.svg
        :target: https://github.com/projectmesa/mesa/actions

.. image:: https://codecov.io/gh/projectmesa/mesa/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/projectmesa/mesa

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
        :target: https://github.com/psf/black

.. image:: https://img.shields.io/matrix/project-mesa:matrix.org?label=chat&logo=Matrix
        :target: https://matrix.to/#/#project-mesa:matrix.org

Mesa allows users to quickly create agent-based models using built-in core components (such as spatial grids and agent schedulers) or customized implementations; visualize them using a browser-based interface; and analyze their results using Python's data analysis tools. Its goal is to be the Python 3-based alternative to NetLogo, Repast, or MASON.


.. image:: https://raw.githubusercontent.com/projectmesa/mesa/main/docs/images/Mesa_Screenshot.png
   :width: 100%
   :scale: 100%
   :alt: A screenshot of the Schelling Model in Mesa

*Above: A Mesa implementation of the Schelling segregation model,
being visualized in a browser window and analyzed in a Jupyter
notebook.*

.. _`Mesa` : https://github.com/projectmesa/mesa/


Features
------------

* Modular components
* Browser-based visualization
* Built-in tools for analysis
* Example model library

Using Mesa
------------

Getting started quickly:

.. code-block:: bash

    $ pip install mesa

You can also use `pip` to install the github version:

.. code-block:: bash

    $ pip install -U -e git+https://github.com/projectmesa/mesa@main#egg=mesa

Or any other (development) branch on this repo or your own fork:

.. code-block:: bash

    $ pip install -U -e git+https://github.com/YOUR_FORK/mesa@YOUR_BRANCH#egg=mesa

For resources or help on using Mesa, check out the following:

* `Intro to Mesa Tutorial`_ (An introductory model, the Boltzmann Wealth Model, for beginners or those new to Mesa.)
* `Complexity Explorer Tutorial`_ (An advanced-beginner model, SugarScape with Traders, with instructional videos)
* `Mesa Examples`_ (A repository of seminal ABMs using Mesa and examples of employing specific Mesa Features)
* `Docs`_ (Mesa's documentation, API and useful snippets)
* `Discussions`_ (GitHub threaded discussions about Mesa)
* `Matrix Chat`_ (Chat Forum via Matrix to talk about Mesa)

.. _`Intro to Mesa Tutorial` : http://mesa.readthedocs.org/en/main/tutorials/intro_tutorial.html
.. _`Complexity Explorer Tutorial` : https://www.complexityexplorer.org/courses/172-agent-based-models-with-python-an-introduction-to-mesa
.. _`Mesa Examples` : https://github.com/projectmesa/mesa-examples/tree/main/examples
.. _`Docs` : http://mesa.readthedocs.org/en/main/
.. _`Discussions` : https://github.com/projectmesa/mesa/discussions
.. _`Matrix Chat` : https://matrix.to/#/#project-mesa:matrix.org

Running Mesa in Docker
------------------------

You can run Mesa in a Docker container in a few ways.

If you are a Mesa developer, first `install Docker Compose <https://docs.docker.com/compose/install/>`_ and then, in the folder containing the Mesa Git repository, you run:

.. code-block:: bash

    $ docker compose up
    # If you want to make it run in the background, you instead run
    $ docker compose up -d

This runs the wolf-sheep predation model, as an example.

With the docker-compose.yml file in this Git repository, the `docker compose up` command does two important things:

* It mounts the mesa root directory (relative to the docker-compose.yml file) into /opt/mesa and runs pip install -e on that directory so your changes to mesa should be reflected in the running container.
* It binds the docker container's port 8521 to your host system's port 8521 so you can interact with the running model as usual by visiting localhost:8521 on your browser


If you are a model developer that wants to run Mesa on a model, you need to:

* make sure that your model folder is inside the folder containing the docker-compose.yml file
* change the ``MODEL_DIR`` variable in docker-compose.yml to point to the path of your model
* make sure that the model folder contains a run.py file

Then, you just need to run `docker compose up -d` to make it accessible from ``localhost:8521``.

Contributing to Mesa
----------------------------

Want to join the Mesa team or just curious about what is happening with Mesa? You can...

  * Join our `Matrix chat room`_ in which questions, issues, and ideas can be (informally) discussed.
  * Come to a monthly dev session (you can find dev session times, agendas and notes on `Mesa discussions`_).
  * Just check out the code on `GitHub`_.

If you run into an issue, please file a `ticket`_ for us to discuss. If possible, follow up with a pull request.

If you would like to add a feature, please reach out via `ticket`_ or join a dev session (see `Mesa discussions`_).
A feature is most likely to be added if you build it!

Don't forget to checkout the `Contributors guide`_.

.. _`Matrix chat room` : https://matrix.to/#/#project-mesa:matrix.org
.. _`Mesa discussions` : https://github.com/projectmesa/mesa/discussions
.. _`GitHub` : https://github.com/projectmesa/mesa/
.. _`ticket` : https://github.com/projectmesa/mesa/issues
.. _`Contributors guide` : https://github.com/projectmesa/mesa/blob/main/CONTRIBUTING.rst


Citing Mesa
----------------------------

To cite Mesa in your publication, you can use the `CITATION.bib`_.

.. _`CITATION.bib` : https://github.com/projectmesa/mesa/blob/main/CITATION.bib
