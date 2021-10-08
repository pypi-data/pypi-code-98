# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2021 AMOSSYS
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
import json
import time
from typing import Dict
from typing import List
from typing import Optional

import requests
from colorama import Fore
from loguru import logger

# Configuration access to Cyber Range endpoint
REDTEAM_API_URL = "http://127.0.0.1:5004"
# Expect a path to CA certs (see:
# https://requests.readthedocs.io/en/master/user/advanced/)
CA_CERT_PATH = None
# Expect a path to client cert (see:
# https://requests.readthedocs.io/en/master/user/advanced/)
CLIENT_CERT_PATH = None
# Expect a path to client private key (see:
# https://requests.readthedocs.io/en/master/user/advanced/)
CLIENT_KEY_PATH = None

# Module variables
attack_list = {}


# -------------------------------------------------------------------------- #
# Internal helpers
# -------------------------------------------------------------------------- #


def _get(route: str, **kwargs: str) -> requests.Response:
    return requests.get(
        f"{REDTEAM_API_URL}{route}",
        verify=CA_CERT_PATH,
        cert=(CLIENT_CERT_PATH, CLIENT_KEY_PATH),
        **kwargs,
    )


def _post(route: str, **kwargs: str) -> requests.Response:
    return requests.post(
        f"{REDTEAM_API_URL}{route}",
        verify=CA_CERT_PATH,
        cert=(CLIENT_CERT_PATH, CLIENT_KEY_PATH),
        **kwargs,
    )


def _put(route: str, **kwargs: str) -> requests.Response:
    return requests.put(
        f"{REDTEAM_API_URL}{route}",
        verify=CA_CERT_PATH,
        cert=(CLIENT_CERT_PATH, CLIENT_KEY_PATH),
        **kwargs,
    )


def _delete(route: str, **kwargs: str) -> requests.Response:
    return requests.delete(
        f"{REDTEAM_API_URL}{route}",
        verify=CA_CERT_PATH,
        cert=(CLIENT_CERT_PATH, CLIENT_KEY_PATH),
        **kwargs,
    )


def _handle_error(result: requests.Response, context_error_msg: str) -> None:
    if result.headers.get("content-type") == "application/json":
        error_msg = str(result.json())  # ["message"]
    else:
        error_msg = result.text

    raise Exception(
        f"{context_error_msg}. "
        f"Status code: '{result.status_code}'.\n"
        f"Error message: '{error_msg}'."
    )


def reset_redteam() -> None:
    result = _delete("/platform")
    result.raise_for_status()
    result = result.json()


def get_notification() -> dict:
    result = _get("/notification", headers={}, data={})

    if result.status_code != 200:
        _handle_error(result, "Cannot retrieve notification from redteam API")

    return result.json()


def available_attacks() -> List[str]:
    url = "/attack"

    result = _get(url, headers={}, data={})

    if result.status_code != 200:
        _handle_error(result, "Cannot retrieve available attacks from redteam API")

    return result.json()


def waiting_attack(id_attack: str, name: str, waiting_worker: bool = True) -> str:
    url = "/attack/" + str(id_attack)

    result = _get(url, headers={}, data={})

    if result.status_code != 200:
        _handle_error(result, "Cannot retrieve attack information from redteam API")

    status = result.json().get("status", None)
    while status not in ["success", "failed"]:  # not finished
        time.sleep(1)
        result = _get(url, headers={}, data={})

        if result.status_code != 200:
            _handle_error(result, "Cannot retrieve attack information from redteam API")

        status = result.json().get("status", None)
        if status == "waiting":
            logger.info(f"[+] ({id_attack}) Attack {name} is waiting.")
            if not waiting_worker:
                return status

        time.sleep(1)

    if status == "success":
        color = Fore.GREEN
    elif status == "failed":
        color = Fore.RED

    logger.info(
        f"[+] {Fore.BLUE}({id_attack}) Attack {name}{Fore.RESET} : {color}{status}{Fore.RESET}"
    )
    return status


def execute_attack(
    id_attack: int, name: str, waiting_worker: bool = True
) -> Optional[str]:
    url = "/attack/" + str(id_attack) + "?action=start"
    payload = {}
    headers = {}
    result = _get(url, headers=headers, data=payload)

    if result.status_code != 200:
        _handle_error(result, "Cannot start attack from redteam API")

    result = result.json()
    idAttack = result.get("idAttack", None)
    logger.info(f"[+] {Fore.BLUE}({idAttack}) Attack {name}{Fore.RESET} : started")
    logger.info(f"[+]     Values : {Fore.YELLOW}{result['values']}{Fore.RESET}")
    if idAttack is not None:
        return waiting_attack(idAttack, name, waiting_worker)


def execute_attack_name(attack_name: str, waiting_worker: bool = True) -> Optional[str]:
    url = "/attack"
    result = _get(url, headers={}, data={})

    if result.status_code != 200:
        _handle_error(result, "Cannot retrieve available attacks from redteam API")

    attack = next(
        (x for x in result.json() if x["worker"]["name"] == attack_name), None
    )

    if attack:
        return execute_attack(attack["idAttack"], attack_name, waiting_worker)
    else:
        logger.warning(f"[-] Attack {attack_name} not avalaible")


def execute_attack_with_value(
    attack_name: str, waiting_worker: bool = True, values: Optional[Dict] = None
) -> Optional[str]:
    url = "/attack"
    result = _get(url, headers={}, data={})

    if result.status_code != 200:
        _handle_error(result, "Cannot retrieve available attacks from redteam API")

    for attack in result.json():
        if attack["worker"]["name"] == attack_name:
            if values is not None:
                v_dict = json.loads(attack["values"])
                if set(values.items()).issubset(v_dict.items()):
                    target_attack = attack
                    break
            else:
                target_attack = attack
                break

    if target_attack:
        return execute_attack(
            id_attack=target_attack["idAttack"],
            name=attack_name,
            waiting_worker=waiting_worker,
        )
    else:
        logger.warning(f"[-] {Fore.RED} Attack {attack_name} not found.{Fore.RESET}")


def init_knowledge(data: List) -> bool:
    output = {}

    for elt in data:
        key = list(elt)[0]
        output[key] = elt[key]

    url = "/knowledge"
    headers = {"Content-type": "application/json"}
    result = _post(url, headers=headers, data=json.dumps(output), timeout=10)

    if result.status_code != 200:
        _handle_error(result, "Cannot initialize knowledge database from redteam API")
    else:
        return True


def execute_scenario(attack_list: List) -> bool:
    for elt in attack_list:
        if type(elt) is dict:
            for key in elt:
                waiting = True
                values = None
                for elt in elt[key]:
                    if "waiting" in elt:
                        waiting = elt["waiting"]
                    elif "values" in elt:
                        values = elt["values"]
                if values:
                    execute_attack_with_value(key, waiting, values)
                else:
                    execute_attack_name(key, waiting_worker=waiting)
        else:
            if execute_attack_name(elt) == "failed":
                logger.error(f"[-] Scenario failed : {elt}")
                return False
    return True


def execute_scenario_by_yaml(yaml_content: Dict) -> bool:
    data = yaml_content.get("data", None)
    if data:
        init_knowledge(data)
    attacks = yaml_content.get("attacks", None)
    if attacks:
        return execute_scenario(attacks)
    else:
        logger.error("[-] Missing attacks attribute")
        return False


def scenario_result() -> str:
    """Get attack scenario result."""

    url = "/report"

    result = _get(url, headers={}, data={})

    if result.status_code != 200:
        _handle_error(result, "Cannot get scenario result from redteam API")

    return result.json()
