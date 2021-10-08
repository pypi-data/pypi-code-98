import inspect
import os

import pytest
from mock import Mock, patch

import vessl
from openapi_client.api.api_v1_api import APIV1Api
from openapi_client.models import (
    SignInAPIPayload,
    SignInCliConfirmAPIPayload,
    SignUpAPIPayload,
)
from vessl.util.config import VesslConfigLoader
from vessl.util.exception import SavvihubApiException

USE_MOCK = not os.environ.get("VESSL_TEST_MOCK_OFF", False)
TEST_CONFIG_PATH = "test/config"

vessl.EXEC_MODE = "TEST"


def pytest_sessionstart(session):
    vessl.vessl_api.config_loader = VesslConfigLoader(TEST_CONFIG_PATH)

    if USE_MOCK:
        vessl.vessl_api.organization = Mock()
        vessl.vessl_api.organization.name = "test-org"
        vessl.vessl_api.project = Mock()
        vessl.vessl_api.project.name = "project"
        patch_api_calls()

    else:
        vessl.vessl_api.api_client.configuration.host = os.environ.get(
            "VESSL_API_HOST", "http://localhost:10000"
        )
        setup_test_account()


def pytest_sessionfinish(session, exitstatus):
    try:
        os.remove(TEST_CONFIG_PATH)
    except OSError:
        pass


def generate_patch_fixture(name, return_value):
    @pytest.fixture(scope="session", autouse=True)
    def func():
        with patch(name, return_value=return_value) as _fixture:
            yield _fixture

    return func


def patch_api_calls():
    for name, value in inspect.getmembers(APIV1Api, predicate=inspect.isfunction):
        if name.endswith("api"):
            patch_name = f"savvihub.vessl_api.{name}"
            globals()[name] = generate_patch_fixture(patch_name, Mock())


def setup_test_account():
    name = "test-name"
    username = "test-username"
    password = "test-password"
    email = "test@email.com"

    # Setup user
    try:
        jwt_token = vessl.vessl_api.sign_in_api(
            sign_in_api_payload=SignInAPIPayload(
                email_or_username=email,
                password=password,
            )
        ).token
    except SavvihubApiException:
        jwt_token = vessl.vessl_api.sign_up_api(
            sign_up_api_payload=SignUpAPIPayload(
                name=name,
                username=username,
                password=password,
                email=email,
                invitation_token="invitation_token_for_cli_test",
            )
        ).token

    # Configure access token
    cli_token = vessl.vessl_api.sign_in_cli_token_api().cli_token
    vessl.vessl_api.api_client.set_default_header(
        "Authorization",
        f"JWT {jwt_token}",
    )
    vessl.vessl_api.sign_in_cli_confirm_api(
        sign_in_cli_confirm_api_payload=SignInCliConfirmAPIPayload(
            cli_token=cli_token,
        )
    )
    access_token = vessl.vessl_api.sign_in_cli_check_api(
        cli_token=cli_token
    ).access_token
    vessl.update_access_token(access_token=access_token)

    # Configure organization
    organization_name = "test-org"
    organizations = vessl.list_organizations()
    if organization_name not in {x.name for x in organizations}:
        vessl.create_organization(
            organization_name=organization_name,
            region=vessl.vessl_api.region_list_api().default_region,
        )
    vessl.update_organization(organization_name=organization_name)

    # Configure project
    project_name = "test-project"
    projects = vessl.list_projects()
    if project_name not in {x.name for x in projects}:
        vessl.create_project(
            project_type="cli-driven",
            project_name=project_name,
        )
    vessl.update_project(project_name=project_name)
