import secrets

import pytest

from hatch.utils.shells import detect_shell, get_shell_names


@pytest.fixture(autouse=True)
def default_shells(platform):
    shell = detect_shell(platform)
    return get_shell_names(shell, platform)


@pytest.fixture(autouse=True)
def isolated_python_directory(config_file):
    config_file.model.dirs.python = 'isolated'
    config_file.save()


@pytest.fixture(autouse=True)
def path_append(mocker):
    return mocker.patch('userpath.append')


@pytest.fixture(autouse=True)
def disable_path_detectors(mocker):
    mocker.patch('userpath.in_current_path', return_value=False)
    mocker.patch('userpath.in_new_path', return_value=False)


@pytest.fixture
def dist_name(compatible_python_distributions):
    return secrets.choice(compatible_python_distributions)
