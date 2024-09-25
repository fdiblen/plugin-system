# ReSoQu

Example code shows how to develop a Python code that can be extended with plugins.

## Requirements

- Python 3.12
- Pipenv

## How to run
```shell
pipenv shell
pipenv run python main.py
```

## Plugins

Default plugins are in `plugins` folder.

The application will download the online plugins described in `plugin-config.yaml` file. The online plugins will be saved in `plusings/extra` folder.

During the execution the application will discuver all the available plugins, register and run tem.

## Online Plugins

Online plugins are stored at
https://github.com/fdiblen/plugin-registry
