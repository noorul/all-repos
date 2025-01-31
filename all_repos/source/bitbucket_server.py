from __future__ import annotations

import base64
from typing import NamedTuple

from all_repos import bitbucket_server_api
from all_repos.util import hide_api_key_repr


class Settings(NamedTuple):
    username: str
    app_password: str
    base_url: str
    project: str | None = None

    @property
    def auth_header(self) -> dict[str, str]:
        value = f'{self.username}:{self.app_password}'
        return {'Authorization': base64.b64encode(value.encode()).decode()}

    def __repr__(self) -> str:
        return hide_api_key_repr(self, key='app_password')


def list_repos(settings: Settings) -> dict[str, str]:
    return bitbucket_server_api.list_repos(
        settings.base_url,
        settings.auth_header,
        settings.project,
    )
