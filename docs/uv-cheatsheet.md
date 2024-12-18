# `uv` cheatsheet

## `uv add`

Add a package to the project

## `uv lock`

Update the project's lockfile

## `uv sync`

Synchronize the venv with the lockfile

## `uv run`

Run a script with your environment. Alternatively `source .venv/bin/activate`.

## Extras

```toml
[project.optional-dependencies]
extra1 = ["pandas"]
extra2 = ["polars"]
```

## Installing from git
If a project should be rebuilt whenever the commit hash changes, you can add the following to the project's `pyproject.toml`:

```toml
[tool.uv]
cache-keys = [{ git = { commit = true } }]
```

## Docs

### Packaging

https://docs.astral.sh/uv/concepts/projects/init/#packaged-applications 

### Reference

https://docs.astral.sh/uv/reference/cli/