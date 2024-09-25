import json
from enum import Enum
from datetime import datetime
from typing import Annotated, List

from pydantic import BaseModel, Field
from pydantic.config import ConfigDict


class Platform(str, Enum):
    github = 'github'
    gitlab = 'gitlab'
    other = 'other'
    not_given = 'not_given'


class Repository(BaseModel):
    url: str


class Plugin(BaseModel):
    name: str = Field(
        json_schema_extra={
            'title': 'Plugin name',
            'description': 'Description of the plugin',
            'examples': ['DefaultPlugin'],
        }
    )


class Metric(BaseModel):
    name: str
    plugin: Plugin
    result: bool
    stdout: str


class MainModel(BaseModel):
    """
    This is the description of the main model
    """

    model_config = ConfigDict(title='Main')

    created_at: datetime = None
    platform: Annotated[Platform | None, Field(alias='Gender')] = None
    repository: Repository
    metrics: List[Metric]


main_model_schema = MainModel.model_json_schema()

# print(json.dumps(main_model_schema, indent=2))

# print(MainModel.model_json_schema(mode='validation'))
# print(MainModel.model_json_schema(mode='serialization'))
