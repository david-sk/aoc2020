# AOC 2020

See <https://adventofcode.com/2020>.

Using Python 3 (version 3.8 or above recommended).

Execute a program with:

```
python3 -m days [day_number]
```

For example:

```
python3 -m days 3

python3 -m days 10
```

## Editor

If using VS Code as text editor, here is some handy config stuff for `.vscode/settings.json` file:

```
{
    "editor.formatOnSave": true,
    "files.trimTrailingWhitespace": true,
    "python.linting.enabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--config=.config/flake8.cfg"
    ],
    "python.linting.mypyEnabled": true,
    "python.linting.mypyArgs": [
        "--config-file=.config/mypy.cfg"
    ],
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": [
        "--config=.config/black.cfg"
    ]
}
```
