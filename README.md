Setup env with pipenv (optional)
--------------------------------

Inside the project folder (after clone)

```console
$ pipenv install
$ pipenv shell
(simple_crgm env) % pipenv install --dev
```

Run
---

Select the exec shell

```console
$ pipenv shell
```

Test
----

Tests should be put on /tests folder and are executed with the following command.

```console
 $ pytest
```

Linter
------

```console
 $ flake8 --statistics
```

Dependency
----------

Add New Dependency
------------------

To add new dependencies use the following command.

```console
$ pipenv install [name]
```

This command will add the dependency to the Pipfile and Pipfile.lock assuring that the execution can be reproduced in another environment (after dependencies are updated with `pipenv install` command )

Add New Dev Dependency
----------------------
Same as previous dependencies, but for development libraries such as the ones used for test.

```console
$ pipenv install [name] --dev
```
Note that other systems after pulling updates will need a reexecution of `pipenv install --dev`