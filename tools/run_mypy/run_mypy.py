import sys
from pathlib import Path

import click
from mypy.api import run as mypy_check
from pathspec import PathSpec
from pathspec.patterns.gitwildmatch import GitWildMatchPattern


def gitignore_to_exclude_regex(gitignore_path: Path) -> list[str]:
    gitignore_content = gitignore_path.read_text()
    spec = PathSpec.from_lines(GitWildMatchPattern, gitignore_content.splitlines())

    # Convert PathSpec rules to a single regex
    exclude_regex_list = []
    for pattern in spec.patterns:
        exclude_regex = pattern.regex
        if exclude_regex is not None:
            exclude_regex_list.append(exclude_regex.pattern)

    return exclude_regex_list


@click.command('run_mypy')
@click.option('--check-path', type=click.Path(exists=True), required=True)
@click.option(
    '-c',
    '--config-file',
    type=click.Path(exists=True),
    default='mypy.ini',
    help='Config file used by mypy, like mypy.ini',
)
@click.option(
    '--gitignore-path',
    type=click.Path(exists=True),
    default='.gitignore',
    help='Path to .gitignore file',
)
def run_mypy(check_path, config_file, gitignore_path):
    """
    Check all managed py code in git repository
    """
    exclude_regex_list = gitignore_to_exclude_regex(Path(gitignore_path))
    stdout, _, exit_status = mypy_check(
        [str(check_path), '--config-file', config_file]
        + [f'--exclude={regex}' for regex in exclude_regex_list],
    )
    if exit_status:
        click.secho(stdout)
        click.secho('Mypy check failed, please modify your code to pass the check.', color='red')
        click.secho('You can run the following command to run mypy locally:')
        click.secho('\tpdm run tox -e mypy_check', fg='blue')
        sys.exit(1)


if __name__ == '__main__':
    run_mypy()
