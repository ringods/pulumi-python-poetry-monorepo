# Monorepo example for a Python based Pulumi setup managed by Poetry

This monorepo contains the following for [Pulumi](https://www.pulumi.com) in Python:

* shared infrastructure code library in [`core`](/code)
* two Pulumi projects using the shared library as a local library dependency.
  * [`project1`](/project1)
  * [`project2`](/project2)

The Pulumi projects and the shared Python library are managed by [Poetry](https://python-poetry.org/).

## Things to know

### Python Virtual Environments

Pulumi works fluent with Python virtual environments available within the project folder. Therefore, we configure Poetry to create the virtual environment within the project folder. You can do this in 2 ways:

* per project using the config file `poetry.toml` with content:
  ```
  [virtualenvs]
  in-project = true
  ```
* globally using the command `poetry config virtualenvs.in-project true`

After cloning the repository, run `poetry install` in each of the folders to retrieve the Python dependencies.

When I set up `project1` and `project2`, I defined the dependency on `core` in such a way that any local change to the core library is immediately reflected in the projects. To have it this way, you define the dependency as editable:

```sh
./project1 $ poetry add --editable ../core
```

This creates a relative folder dependency from the project to `core`. If you forget the `--editable` flag, it copies the current state of `core` in the virtual environment of the project but any later changes will not ripple through.

### VSCode

If you use VSCode, open this setup using the workspace file `python-monorepo.code-workspace`:

> File -> Open Workspace from File...

Each folder is now a project to VSCode. For the Python virtual environments to be picked up automatically, a `.vscode/settings.json` file is available in each folder, pointing to the in-project virtual environment folder.

## References

* [Non-Pulumi Python monorepo with Poetry](https://github.com/dermidgen/python-monorepo)
