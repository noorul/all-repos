from __future__ import annotations

import pytest

from all_repos.source.bitbucket_server import list_repos
from all_repos.source.bitbucket_server import Settings


@pytest.mark.usefixtures('repos_response')
def test_list_repos():
    settings = Settings(
        'cool_user', 'app_password', 'bitbucket.domain.com',
    )
    ret = list_repos(settings)
    assert ret == {
        'fake_proj/fake_repo': 'ssh://git@bitbucket.domain.com/'
        'fake_proj/fake_repo.git',
    }


@pytest.mark.usefixtures('repos_project_response')
def test_list_repos_from_project():
    settings = Settings(
        'cool_user', 'app_password', 'bitbucket.domain.com', 'PRJ',
    )
    ret = list_repos(settings)
    assert ret == {
        'fake_proj/fake_repo': 'ssh://git@bitbucket.domain.com/'
        'fake_proj/fake_repo.git',
    }


def test_settings_repr():
    settings = Settings('cool_user', 'app_password', 'bitbucket.domain.com')
    assert repr(settings) == (
        'Settings(\n'
        "    username='cool_user',\n"
        '    app_password=...,\n'
        "    base_url='bitbucket.domain.com',\n"
        '    project=None,\n'
        ')'
    )
