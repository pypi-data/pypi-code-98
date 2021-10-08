__all__ = ["main"]

import getpass
import os
from argparse import ArgumentParser, Namespace
from typing import Any

import requests.exceptions

import darwin.cli_functions as f
from darwin import __version__
from darwin.exceptions import InvalidTeam, Unauthenticated, Unauthorized
from darwin.options import Options


def main() -> Any:
    args, parser = Options().parse_args()
    try:
        _run(args, parser)
    except Unauthorized:
        f._error("Your API key is not authorized to do that action.")
    except Unauthenticated:
        f._error("You need to specify a valid API key to do that action.")
    except InvalidTeam:
        f._error("The team specified is not in the configuration, please authenticate first.")
    except requests.exceptions.ConnectionError:
        f._error("Darwin seems unreachable, please try again in a minute or contact support.")


def _run(args: Namespace, parser: ArgumentParser) -> Any:
    if args.command == "help":
        f.help(parser)
    # Authenticate user
    if args.command == "authenticate":
        api_key = os.getenv("DARWIN_API_KEY")
        if api_key:
            print("Using API key from DARWIN_API_KEY")
        else:
            api_key = getpass.getpass(prompt="API key: ", stream=None)
            api_key = api_key.strip()
            if api_key == "":
                print("API Key needed, generate one for your team: https://darwin.v7labs.com/?settings=api-keys")
                return
        f.authenticate(api_key)
        print("Authentication succeeded.")
    # Select / List team
    elif args.command == "team":
        if args.team_name:
            f.set_team(args.team_name)
        elif args.current:
            f.current_team()
        else:
            f.list_teams()
    # Version
    elif args.command == "version":
        print(__version__)

    elif args.command == "convert":
        f.convert(args.format, args.files, args.output_dir)
    elif args.command == "dataset":
        if args.action == "remote":
            f.list_remote_datasets(args.all, args.team)
        elif args.action == "local":
            f.local(args.team)
        elif args.action == "create":
            f.create_dataset(args.dataset)
        elif args.action == "path":
            path = f.path(args.dataset)
            if path:
                print(path)
        # Print the url of a remote project
        elif args.action == "url":
            f.url(args.dataset)
        elif args.action == "push":
            f.upload_data(args.dataset, args.files, args.exclude, args.fps, args.path, args.frames, args.preserve_folders, args.verbose)
        # Remove a project (remotely)
        elif args.action == "remove":
            f.remove_remote_dataset(args.dataset)
        elif args.action == "report":
            f.dataset_report(args.dataset, args.granularity or "day")
        elif args.action == "export":
            f.export_dataset(args.dataset, args.include_url_token, args.annotation_class, args.name)
        elif args.action == "files":
            f.list_files(args.dataset, args.status, args.path, args.only_filenames, args.sort_by)
        elif args.action == "releases":
            f.dataset_list_releases(args.dataset)
        elif args.action == "pull":
            f.pull_dataset(args.dataset, args.only_annotations, args.folders, args.video_frames)
        elif args.action == "import":
            f.dataset_import(args.dataset, args.format, args.files, args.append)
        elif args.action == "convert":
            f.dataset_convert(args.dataset, args.format, args.output_dir)
        elif args.action == "set-file-status":
            f.set_file_status(args.dataset, args.status, args.files)
        elif args.action == "split":
            f.split(args.dataset, args.val_percentage, args.test_percentage, args.seed)
        elif args.action == "help" or args.action is None:
            f.help(parser, "dataset")


if __name__ == "__main__":
    main()
