from typing import Dict, Callable, List, Union

from django_koldar_utils.graphql_toolsbox.GraphQLHelper import GraphQLHelper
from django_koldar_utils.graphql_toolsbox.graphql_types import TGrapheneArgument, TGrapheneWholeQueryReturnType, \
    TDjangoModelType, TGrapheneType, TGrapheneInputType, TGrapheneQuery, TGrapheneMutation

from django_graphene_crud_generator.generator.AbstractGraphQLMutationGenerator import AbstractGraphQLMutationGenerator
from django_graphene_crud_generator.generator.AbstractGraphQLQueryGenerator import AbstractGraphQLQueryGenerator
from django_graphene_crud_generator.generator.LambdaGraphQLMutationGenerator import LambdaGraphQLMutationGenerator
from django_graphene_crud_generator.generator.LambdaGraphQLQueryGenerator import LambdaGraphQLQueryGenerator
from django_graphene_crud_generator.generator.TokenBasedAuthenticationComponent import TokenBasedAuthenticationComponent
from django_graphene_crud_generator.types import GrapheneBodyFunction


# ##################################################
# MUTATION
# ##################################################


def _create_simple_mutation_generator(
        class_name: str,
        arguments: Dict[str, TGrapheneArgument],
        return_value: TGrapheneWholeQueryReturnType,
        callable: GrapheneBodyFunction,
        description: Union[str, List[str]] = None
) -> AbstractGraphQLMutationGenerator:
    """
    Create a mutation generator where you can fully customize what the graphql resovler will do

    :param class_name: name of the class to generate
    :param arguments: arguments of the graphql mutation to generate
    :param return_value: dictioanry of values to return by the mutation
    :param callable: callable called whenever the mutation is called. first input is root, second is info, then the
        args and kwargs of the graphql
    :param description: description of the mutation. If left missing we will try to look at the documentation
        of the callable instead
    :return: generator of mutations
    """
    if description is None and hasattr(callable, "__doc__"):
        description = callable
    else:
        description = "No description"
    s = LambdaGraphQLMutationGenerator(
        class_name=class_name,
        description=description,
        arguments=arguments,
        return_value=return_value,
        callable=callable
    )
    return s


def create_simple_mutation(
        class_name: str,
        arguments: Dict[str, TGrapheneArgument],
        return_value: TGrapheneWholeQueryReturnType,
        callable: GrapheneBodyFunction,
        description: Union[str, List[str]] = None,
        **kwargs
) -> TGrapheneMutation:
    """
    Create a mutation type where you can fully customize what the graphql resovler will do

    :param class_name: name of the class to generate
    :param arguments: arguments of the graphql mutation to generate
    :param return_value: dictioanry of values to return by the mutation
    :param callable: callable called whenever the mutation is called. first input is root, second is info, then the
        args and kwargs of the graphql
    :param description: description of the mutation. If left missing we will try to look at the documentation
        of the callable instead
    :return: type representing the mutation
    """
    s = _create_simple_mutation_generator(
        class_name=class_name,
        description=description,
        arguments=arguments,
        return_value=return_value,
        callable=callable
    )
    return s.generate(**kwargs)


def create_token_authenticated_mutation(
    class_name: str,
    arguments: Dict[str, TGrapheneArgument],
    return_value: TGrapheneWholeQueryReturnType,
    callable: GrapheneBodyFunction,
    description: Union[str, List[str]] = None,
    token_name: str = None,
    permissions: List[str] = None,
) -> TGrapheneMutation:
    """
    Create a mutation where you can fully customize what the graphql resovler will do. The mutation requires you to
    be logger and have sufficient permissions. authentication is done via a token

    :param class_name: name of the class to generate
    :param arguments: arguments of the graphql mutation to generate
    :param return_value: dictioanry of values to return by the mutation
    :param callable: callable called whenever the mutation is called. first input is root, second is info, then the
        args and kwargs of the graphql
    :param description: description of the mutation. If left missing we will try to look at the documentation
        of the callable instead
    :param token_name: name of the argument representing the token used to authenticate
    :param permissions: list of permissions required in order to perform the action. If left empty, you nee dto be only
        logged
    :return: type representing the mutation
    """
    s = _create_simple_mutation_generator(
        class_name=class_name,
        description=description,
        arguments=arguments,
        return_value=return_value,
        callable=callable
    )
    s.register_component(TokenBasedAuthenticationComponent())
    if token_name is None:
        token_name = "token"
    if permissions is None:
        permissions = []
    return s.generate(
        token_name=token_name,
        permissions=permissions,
    )


def create_token_authentication_action(
    class_name: str,
    arguments: Dict[str, TGrapheneArgument],
    callable: GrapheneBodyFunction,
    ok_flag_name: bool = None,
    token_name: str = None,
    permissions: List[str] = None,
    description: Union[str, List[str]] = None,
):
    """
    Create a mutation where you can perform a side-effect action. The action return nothing, hence we will just
    return a booelan which will always be true if no errors occur.
    The mutation requires you to be logged and have sufficient permissions. authentication is done via a token

    :param class_name: name of the class to generate
    :param arguments: arguments of the graphql mutation to generate
    :param callable: callable called whenever the mutation is called. first input is root, second is info, then the
        args and kwargs of the graphql
    :param ok_flag_name: name of the return value fo the mutation
    :param description: description of the mutation. If left missing we will try to look at the documentation
        of the callable instead
    :param token_name: name of the argument representing the token used to authenticate
    :param permissions: list of permissions required in order to perform the action. If left empty, you nee dto be only
        logged
    :return: type representing the mutation
    """
    if ok_flag_name is None:
        ok_flag_name = "ok"

    def callable_wrapper(root, info, *args, **kwargs):
        nonlocal callable
        callable(root, info, *args, **kwargs)
        return True

    return create_token_authenticated_mutation(
        class_name=class_name,
        description=description,
        arguments=arguments,
        return_value={ok_flag_name: GraphQLHelper.return_ok("True if the operation is successful")},
        callable=callable_wrapper,
        token_name=token_name,
        permissions=permissions,
    )


def create_token_authentication_function(
    class_name: str,
    arguments: Dict[str, TGrapheneArgument],
    callable: GrapheneBodyFunction,
    return_value: TGrapheneWholeQueryReturnType,
    token_name: str = None,
    permissions: List[str] = None,
    description: Union[str, List[str]] = None,
):
    """
    Create a mutation where you can perform a side-effect action which return a single value.
    The mutation requires you to be logged and have sufficient permissions. authentication is done via a token

    :param class_name: name of the class to generate
    :param arguments: arguments of the graphql mutation to generate
    :param callable: callable called whenever the mutation is called. first input is root, second is info, then the
        args and kwargs of the graphql
    :param ok_flag_name: name of the return value fo the mutation
    :param description: description of the mutation. If left missing we will try to look at the documentation
        of the callable instead
    :param token_name: name of the argument representing the token used to authenticate
    :param permissions: list of permissions required in order to perform the action. If left empty, you nee dto be only
        logged
    :return: type representing the mutation
    """

    def callable_wrapper(root, info, *args, **kwargs):
        nonlocal callable
        result = callable(root, info, *args, **kwargs)
        return result

    return create_token_authenticated_mutation(
        class_name=class_name,
        description=description,
        arguments=arguments,
        return_value=return_value,
        callable=callable_wrapper,
        token_name=token_name,
        permissions=permissions,
    )


# ##################################################
# QUERY
# ##################################################


def create_simple_query_generator(
        class_name: str,
        description: Union[str, List[str]],
        output_name: str,
        arguments: Dict[str, TGrapheneArgument],
        return_value: TGrapheneWholeQueryReturnType,
        callable: GrapheneBodyFunction
) -> AbstractGraphQLQueryGenerator:
    s = LambdaGraphQLQueryGenerator(class_name, description, arguments, output_name, return_value, callable)
    return s


def create_simple_query(
        class_name: str,
        description: Union[str, List[str]],
        output_name: str,
        arguments: Dict[str, TGrapheneArgument],
        return_value: TGrapheneWholeQueryReturnType,
        callable: GrapheneBodyFunction,
        **kwargs
) -> TGrapheneQuery:
    s = create_simple_query_generator(class_name, description, arguments, output_name, return_value, callable)
    return s.generate(**kwargs)


def create_token_authenticated_query(
    class_name: str,
    description: Union[str, List[str]],
    arguments: Dict[str, TGrapheneArgument],
    return_value: TGrapheneWholeQueryReturnType,
    callable: GrapheneBodyFunction,
    token_name: str = None,
    permissions: List[str] = None,
) -> TGrapheneQuery:
    s = create_simple_query_generator(class_name, description, arguments, return_value, callable)
    s.register_component(TokenBasedAuthenticationComponent())
    if token_name is None:
        token_name = "token"
    if permissions is None:
        permissions = []
    return s.generate(
        token_name=token_name,
        permissions=permissions,
    )
