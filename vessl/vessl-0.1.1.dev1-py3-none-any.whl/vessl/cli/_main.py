import os
import sys

project_root = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
# this line should be on the top to run it on a local environment as 'python vessl/cli/_main.py'
sys.path.append(project_root)

import click
import sentry_sdk
from click.decorators import pass_context
from sentry_sdk.integrations.logging import ignore_logger

import vessl
from vessl.cli._base import VesslGroup
from vessl.cli._util import prompt_choices
from vessl.cli.dataset import cli as dataset_cli
from vessl.cli.experiment import cli as experiment_cli
from vessl.cli.kernel_cluster import cli as kernel_cluster_cli
from vessl.cli.kernel_image import cli as kernel_image_cli
from vessl.cli.kernel_resource_spec import cli as kernel_resource_spec_cli
from vessl.cli.model import cli as model_cli
from vessl.cli.organization import cli as organization_cli
from vessl.cli.project import cli as project_cli
from vessl.cli.ssh_key import cli as ssh_key_cli
from vessl.cli.sweep import cli as sweep_cli
from vessl.cli.volume import cli as volume_cli
from vessl.cli.workspace import cli as workspace_cli
from vessl.util.config import DEFAULT_CONFIG_PATH, VesslConfigLoader
from vessl.util.exception import (
    InvalidOrganizationError,
    InvalidProjectError,
    InvalidTokenError,
    SavvihubApiException,
)

# Configure Sentry
sentry_sdk.init(
    "https://e46fcd750b3a443fbd5b9dbc970e4ecf@o386227.ingest.sentry.io/5911639",
    traces_sample_rate=1.0,
)
ignore_logger("vessl_logger")


def prompt_organizations() -> str:
    organizations = vessl.list_organizations()
    organization_count = len(organizations)

    new_organization_string = "Create new organization..."
    choices = [(x.name, i) for i, x in enumerate(organizations)] + [
        (new_organization_string, organization_count)
    ]
    choice = prompt_choices("Default organization", choices)

    if choice == organization_count:
        organization_name = click.prompt("Organization name", type=click.STRING)
        regions = vessl.vessl_api.region_list_api().regions
        region = prompt_choices("Region", [(x.name, x.value) for x in regions])
        vessl.create_organization(organization_name, region)
    else:
        organization_name = organizations[choice].name

    return organization_name


@click.command(cls=VesslGroup)
@click.version_option()
@pass_context
def cli(ctx: click.Context):
    vessl.EXEC_MODE = "CLI"
    ctx.ensure_object(dict)


@cli.group(cls=VesslGroup, invoke_without_command=True)
@click.pass_context
@click.option("-t", "--access-token", type=click.STRING)
@click.option("-o", "--organization", type=click.STRING)
@click.option("-p", "--project", type=click.STRING)
@click.option("-f", "--credentials-file", type=click.STRING)
@click.option("--renew-token", is_flag=True)
def configure(
    ctx,
    access_token: str,
    organization: str,
    project: str,
    credentials_file: str,
    renew_token: bool,
):
    if ctx.invoked_subcommand:
        return

    try:
        vessl.update_access_token(
            access_token=access_token,
            credentials_file=credentials_file,
            force_update=renew_token,
        )
    except InvalidTokenError:
        vessl.update_access_token(force_update=True)

    try:
        vessl.update_organization(
            organization_name=organization, credentials_file=credentials_file
        )
    except InvalidOrganizationError:
        organization_name = prompt_organizations()
        vessl.update_organization(organization_name)

    try:
        vessl.update_project(project_name=project, credentials_file=credentials_file)
    except InvalidProjectError:
        projects = vessl.list_projects()
        if len(projects) == 0:
            return

        project_name = prompt_choices("Default project", [x.name for x in projects])
        vessl.update_project(project_name)

    print(f"Welcome, {vessl.vessl_api.user.display_name}!")


@configure.vessl_command()
@click.argument("organization", type=click.STRING, required=False)
def organization(organization: str):
    if organization is None:
        organization = prompt_organizations()
    vessl.update_organization(organization)
    print(f"Saved to {DEFAULT_CONFIG_PATH}.")


@configure.vessl_command()
@click.argument("project", type=click.STRING, required=False)
def project(project: str):
    vessl.vessl_api.set_organization()

    if project is None:
        projects = vessl.list_projects()
        if len(projects) == 0:
            return

        project = prompt_choices("Default project", [x.name for x in projects])
    vessl.update_project(project)
    print(f"Saved to {DEFAULT_CONFIG_PATH}.")


@configure.command()
def list():
    config = VesslConfigLoader()

    username = ""
    email = ""
    organization = config.default_organization or ""
    project = config.default_project or ""

    if config.access_token:
        vessl.vessl_api.api_client.set_default_header(
            "Authorization", f"Token {config.access_token}"
        )

        try:
            user = vessl.vessl_api.get_my_user_info_api()
            username = user.username
            email = user.email
        except SavvihubApiException as e:
            pass

    print(
        f"Username: {username}\n"
        f"Email: {email}\n"
        f"Organization: {organization}\n"
        f"Project: {project}"
    )


cli.add_command(dataset_cli)
cli.add_command(experiment_cli)
cli.add_command(kernel_cluster_cli)
cli.add_command(kernel_image_cli)
cli.add_command(kernel_resource_spec_cli)
cli.add_command(model_cli)
cli.add_command(organization_cli)
cli.add_command(project_cli)
cli.add_command(ssh_key_cli)
cli.add_command(sweep_cli)
cli.add_command(volume_cli)
cli.add_command(workspace_cli)


if __name__ == "__main__":
    cli()
