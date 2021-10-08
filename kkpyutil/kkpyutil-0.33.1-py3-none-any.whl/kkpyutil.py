#!/usr/bin/env python

"""
Utility lib for personal projects, supports py3 only.

Covering areas:
    - Logging;
    - Config save/load;
    - Decoupled parameter server-client arch;
"""

# Import std-modules.
import argparse
import collections
import cProfile as profile
import difflib
import fnmatch
import functools
import gettext
import hashlib
import json
import locale
import logging
import logging.config
import multiprocessing
import os
import os.path as osp
from os.path import abspath, basename, dirname, expanduser, exists, isfile, join, splitext
# from pprint import pprint, pformat
import platform
import plistlib
import pprint as pp
import pstats
import shlex
import shutil
import subprocess
import sys
import tempfile
import threading
import traceback
from types import SimpleNamespace
import uuid


#
# Globals
#
_script_dir = abspath(dirname(__file__))
TXT_CODEC = 'utf-8'  # Importable.
MAIN_CFG_FILENAME = 'app.json'
DEFAULT_CFG_FILENAME = 'default.json'


class SingletonDecorator:
    """
    Decorator to build Singleton class, single-inheritance only.
    Usage:
        class MyClass: ...
        myobj = SingletonDecorator(MyClass, args, kwargs)
    """
    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


class _Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(_Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(_Singleton('SingletonMeta', (object,), {})):
    pass


class LowPassLogFilter(object):
    """
    Logging filter: Show log messages below input level.
    - CRITICAL = 50
    - FATAL = CRITICAL
    - ERROR = 40
    - WARNING = 30
    - WARN = WARNING
    - INFO = 20
    - DEBUG = 10
    - NOTSET = 0
    """
    def __init__(self, level):
        self.__level = level

    def filter(self, log):
        return log.levelno <= self.__level


class HighPassLogFilter(object):
    """Logging filter: Show log messages above input level."""
    def __init__(self, level):
        self.__level = level

    def filter(self, log):
        return log.levelno >= self.__level


class BandPassLogFilter(object):
    def __init__(self, levelbounds):
        self.__levelbounds = levelbounds

    def filter(self, log):
        return self.__levelbounds[0] <= log.levelno <= self.__levelbounds[1]


def build_default_logger(logdir, name=None, cfgfile=None, verbose=False):
    """
    Create per-file logger and output to shared log file.
    - If found config file under script folder, use it;
    - Otherwise use default config: save to /project_root/project_name.log.
    - 'filename' in config is a filename; must prepend folder path to it.
    :logdir: directory the log file is saved into.
    :name: basename of the log file,
    :cfgfile: config file in the format of dictConfig.
    :return: logger object.
    """
    try:
        os.makedirs(logdir)
    except:
        pass

    cfg_file = cfgfile or join(_script_dir, 'logging.json')
    logging_config = None
    try:
        if sys.version_info.major > 2:
            with open(cfg_file, 'r', encoding=TXT_CODEC,
                      errors='backslashreplace', newline=None) as f:
                text = f.read()
        else:
            with open(cfg_file, 'rU') as f:
                text = f.read()
        # Add object_pairs_hook=coll.OrderedDict hook for py3.5 and lower.
        logging_config = json.loads(text,
                                    object_pairs_hook=collections.OrderedDict)
        logging_config['handlers']['file']['filename'] = join(logdir, logging_config['handlers']['file']['filename'])
    except Exception:
        filename = name or basename(basename(logdir.strip('\\/')))
        log_path = join(logdir, '{}.log'.format(filename))
        logging_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "filters": {
                "info_lpf": {
                  "()": "kkpyutil.LowPassLogFilter",
                  "level": 10 if verbose else 20,
                },
                "info_bpf": {
                  "()": "kkpyutil.BandPassLogFilter",
                  "levelbounds": [10, 20] if verbose else [20, 20],
                },
                "warn_hpf": {
                  "()": "kkpyutil.HighPassLogFilter",
                  "level": 30
                }
            },
            "formatters": {
                "console": {
                    "format": "%(asctime)s: %(levelname)s: %(module)s: %(lineno)d: \n%(message)s\n"
                },
                "file": {
                    "format": "%(asctime)s: %(levelname)s: %(pathname)s: %(lineno)d: \n%(message)s\n"
                }
            },
            "handlers": {
                    "console": {
                        "level": "DEBUG" if verbose else "INFO",
                        "formatter": "console",
                        "class": "logging.StreamHandler",
                        "stream": "ext://sys.stdout",
                        "filters": ["info_bpf"]
                    },
                    "console_err": {
                        "level": "WARN",
                        "formatter": "console",
                        "class": "logging.StreamHandler",
                        "stream": "ext://sys.stderr",
                        "filters": ["warn_hpf"]
                    },
                    "file": {
                        "level": "DEBUG",
                        "formatter": "file",
                        "class": "logging.FileHandler",
                        "encoding": "utf-8",
                        "filename": log_path
                    }
            },
            "loggers": {
                "": {
                    "handlers": ["console", "console_err", "file"],
                    "level": "INFO",
                    "propagate": True
                },
                "default": {
                    "handlers": ["console", "console_err", "file"],
                    "level": "DEBUG",
                    "propagate": False
                }
            }
        }
    if name:
        logging_config['loggers'][name] = logging_config['loggers']['default']
    logging.config.dictConfig(logging_config)
    return logging.getLogger(name or 'default')


_logger = build_default_logger(logdir=join(_script_dir, os.pardir, 'temp'), name=splitext(basename(__file__))[0])


def catch_unknown_exception(exc_type, exc_value, exc_traceback):
    """Global exception to handle uncaught exceptions"""
    exc_info = exc_type, exc_value, exc_traceback
    _logger.error('Unhandled exception: ', exc_info=exc_info)
    # _logger.exception('Unhandled exception: ')  # try-except block only.
    # sys.__excepthook__(*exc_info)  # Keep commented out to avoid msg dup.


sys.excepthook = catch_unknown_exception


def build_logger(srcpath, logpath=None):
    """
    Build per-file logger.
    :param srcpath: Path to source file.
    :param logpath: Path to log file, default to /same/dir/basename.log.
    :return: Logger object.
    """
    src_basename = basename(srcpath)

    # Must have to see DEBUG/INFO at all
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(src_basename)
    logger.setLevel(logging.DEBUG)

    # Hide dependency module's logging
    logger.propagate = False

    # Avoid redundant logs from duplicated handlers created by other modules.
    if len(logger.handlers) > 1:
        return logger

    # Console log for end-users: no debug messages.
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(
        '%(levelname)s: %(name)s: %(message)s')
    )
    logger.addHandler(handler)

    if logpath is None:
        logpath = join(abspath(dirname(srcpath)), 'app.log')

    # Log file for coders: with debug messages.
    logdir = abspath(dirname(logpath))
    if not exists(logdir):
        os.makedirs(logdir)
    handler = logging.FileHandler(logpath)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(logging.Formatter(
        '%(levelname)s: %(pathname)s: %(lineno)d: %(asctime)s: \n%(message)s\n')
    )
    logger.addHandler(handler)

    return logger


def format_error_message(situation, expected, got, suggestions, action):
    return '{}.\n\tExpected: {};\n\tGot: {};\n\tSuggestions: {};\n\tAction: {}.'.format(situation, expected, got, suggestions, action)


def is_cli_mode(argv):
    """Use CLI mode if found command line options."""
    return len(argv) > 1


def is_gui_mode(argv):
    """Use GUI mode if no command line options are found."""
    return len(argv) == 1  # no command line options, so run GUI.


def is_multiline(text):
    return len(text.strip().split('\n')) > 1


def is_python3():
    return sys.version_info[0] > 2


def load_json(path):
    """
    Load Json configuration file.
    :param path: path to the config file
    :return: config as a dict
    """
    if is_python3():
        with open(path, 'r', encoding=TXT_CODEC, errors='backslashreplace', newline=None) as f:
            text = f.read()
    else:
        with open(path, 'rU') as f:
            text = f.read()
    # Add object_pairs_hook=collections.OrderedDict hook for py3.5 and lower.
    return json.loads(text, object_pairs_hook=collections.OrderedDict)

def load_json_obj(path):
    """
    Load Json configuration file.
    :param path: path to the config file
    :return: config as an object
    """
    if is_python3():
        with open(path, 'r', encoding=TXT_CODEC, errors='backslashreplace', newline=None) as f:
            text = f.read()
    else:
        with open(path, 'rU') as f:
            text = f.read()
    # Add object_pairs_hook=collections.OrderedDict hook for py3.5 and lower.
    return json.loads(text, object_hook=lambda d: SimpleNamespace(**d))


def save_json(path, config):
    """
    Use io.open(), aka open() with py3 to produce a file object that encodes
    Unicode as you write, then use json.dump() to write to that file.
    Validate keys to avoid JSON and program out-of-sync.
    """
    if is_python3():
        with open(path, 'w', encoding=TXT_CODEC) as f:
            json.dump(config, f, ensure_ascii=False, indent=4)
    else:
        with open(path, 'w') as f:
            json.dump(config, f, ensure_ascii=False, indent=4)


def parse_args_config(argv, app_info):
    """
    Argrument parser for config-based controls.
    :param argv: sys.argv;
    :param app_info: {'Script': /path/to/script, 'Task': for what,
    'Version': __version__};
    :return: argument parsed.
    """
    name = 'python {}'.format(app_info['Script'])
    script_dir = abspath(dirname(app_info['Script']))
    cfg_file = abspath(join(script_dir, MAIN_CFG_FILENAME))
    default_cfg_file = join(script_dir, DEFAULT_CFG_FILENAME)
    desc = """
{}

Parameters are defined in config files in app folder.
App folder has exactly one pair of config files.
    - app.json: used with -c option under CLI mode, and under GUI mode.
          Control values are saved here on launch.
    - default.json: used as fallback config and for resetting GUI.
                    It should be updated sparingly by user.
    """.format(app_info['Task'])

    epilog = """
examples:

# Run under command line (CLI) mode using main config file
python -c {}

# Run under CLI mode using specified config file
python -C /path/to/myconfig.json {}

# Run under GUI mode
python {} 
or use shell integration, e.g., Explorer or Finder.
        """.format(app_info['Script'], app_info['Script'], app_info['Script'])
    parser = argparse.ArgumentParser(
        prog=name,
        description=desc,
        add_help=True,
        epilog=epilog,
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='%(prog)s {}'.format(app_info['Version'])
    )
    parser.add_argument(
        '-c',
        '--commandline',
        action='store_true',
        default=False,
        help='Run in command line mode (CLI) with main config if set.'
    )
    parser.add_argument(
        '-C',
        '--config',
        # nargs=1,   # CAUTION: Ignore narg, otherwise you get a list.
        action='store',
        dest='cfg_file',
        default=cfg_file,
        help='Path to config file, default to {} .'.format(default_cfg_file))
    # CLI logging is quiet; log file is verbose.
    parser.add_argument(
        '-V',
        '--verbose',
        action='store_true',
        dest='verbose',
        default=False,
        help='Use verbose logging if true, otherwise quiet, default to False.'
    )

    # CAUTION:
    # Must ignore argv[0], i.e., script name,
    # to avoid "error: unrecognized arguments: test.py"
    return parser.parse_args(argv[1:])


def query_yes_no(question, default=True):
    """Ask a yes/no question via standard input and return the answer.

    If invalid input is given, the user will be asked until
    they acutally give valid input.

    Args:
        question(str):
            A question that is presented to the user.
        default(bool|None):
            The default value when enter is pressed with no value.
            When None, there is no default value and the query
            will loop.
    Returns:
        A bool indicating whether user has entered yes or no.

    Side Effects:
        Blocks program execution until valid input(y/n) is given.
    """
    input_ = input if sys.version_info.major > 2 else raw_input
    yes_list = ['yes', 'y']
    no_list = ['no', 'n']

    default_dict = {  # default => prompt default string
        None: '[y/n]',
        True: '[Y/n]',
        False: '[y/N]',
    }

    default_str = default_dict[default]
    prompt_str = '{}\n{}'.format(question, default_str) \
        if question else '{}'.format(default_str)

    while True:
        choice = input_(prompt_str).lower()

        if not choice and default is not None:
            return default
        if choice in yes_list:
            return True
        if choice in no_list:
            return False

        notification_str = "Please type in 'y' or 'n'"
        print(notification_str)


def trace_calls_and_returns(frame, event, arg):
    co = frame.f_code
    func_name = co.co_name
    if func_name == 'write':
        # Ignore write() calls from printing
        return
    line_no = frame.f_lineno
    filename = co.co_filename
    if event == 'call':
        print('* Call to {} on line {} of {}'.format(
            func_name, line_no, filename))
        return trace_calls_and_returns
    elif event == 'return':
        print('* {} => {}'.format(func_name, arg))
    return


def threaded_main(target, daemon=True):
    """
    Run main task without blocking GUI for realtime apps.
    Assume:
    - parameters are from config file.
    - no thread communication.
    :param target: main function.
    :param daemon: True if backend must finish work after GUI quits.
    :return:
    """
    thread = threading.Thread(target=target,
                              args=([sys.argv[0], '-c'],),
                              daemon=daemon)
    thread.start()


def get_md5_checksum(file):
    """Compute md5 checksum of a file."""
    if not isfile(file):
        return None
    myhash = hashlib.md5()
    with open(file, 'rb') as f:
        while True:
            b = f.read(8096)
            if not b:
                break
            myhash.update(b)
    return myhash.hexdigest()


def logprogress(msg='Task', loghook=_logger.info, errorhook=_logger.error):
    def wrap(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            loghook("Progress: Start {} ...".format(msg))
            try:
                response = function(*args, **kwargs)
            except Exception as error:
                errorhook("Function '{}' raised {} with error '{}'.".format(function.__name__, error.__class__.__name__, str(error)))
                raise error
            loghook("Progress: Done.")
            return response
        return wrapper
    return wrap


def logcall(msg='trace', loghook=_logger.debug, errorhook=_logger.error):
    def wrap(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            loghook("Calling function '{}' with args={} kwargs={}: {}.".format(function.__name__, args, kwargs, msg))
            try:
                response = function(*args, **kwargs)
            except Exception as error:
                loghook("Function '{}' raised {} with error '{}'.".format(function.__name__, error.__class__.__name__, str(error)))
                raise error
            loghook("Function '{}' returned {}.".format(function.__name__, response))
            return response
        return wrapper
    return wrap


def organize_concurrency(ntasks, nprocs=None, useio=False):
    """
    Suggest concurrency approach based on tasks and number of processes.
    - Use Processes when processes are few or having I/O tasks.
    - Use Pool for many processes or no I/O.
    - Use sequential when tasks are
    :param ntasks: number of total tasks.
    :param nprocs: number of processes, None means to let algorithm decide.
    :param useio: are we I/O-bound?
    :return: dict of all needed parameters.
    """
    if ntasks <= 1:
        return {'Type': 'Sequential'}

    # manual process allocation
    if not nprocs:
        nprocs = multiprocessing.cpu_count()

    # io-bound
    if useio:
        nprocs = 10
        return {
            'Type': 'Thread',
            'Count': nprocs
        }

    # cpu-bound
    # # brute-force schedule
    # tasks_per_proc = int(math.floor(float(ntasks) / float(nprocs)))
    # ranges = [(i * tasks_per_proc, (i + 1) * tasks_per_proc if i < nprocs - 1 else ntasks) for i in range(nprocs)]
    return {
        'Type': 'Process',
        'Count': nprocs
    }


def ranged_worker(worker, rg, shared, lock):
    results = [worker(shared['Tasks'][t]) for t in range(rg[0], rg[1])]
    # pprint(results)
    with lock:
        tmp = shared['Results']
        for r, result in enumerate(results):
            tmp.append(result)
        shared['Results'] = tmp
    # pprint('tmp: {}'.format(tmp))


def execute_concurrency(worker, shared, lock, algorithm):
    """
    Execute tasks and return results, based on algorithm.
    - worker is unit sequential worker, using single arg.
    - worker returns result as (task['Index'], value).
    - shared is a manager().dict().
    - shared has keys: Title, Tasks.
    - shared['Tasks']: tuple of args for each task worker instance
    - shared['Tasks'][i] has keys: Title, Index, Args, Result
        - Title: info for progress report
        - Index: order of tasks, None for unordered
        - Args: worker input args
        - Result: worker returned results in order
    """
    global _logger
    # TODO: measure timeout for .join()
    if algorithm['Type'] == 'Sequential':
        results = []
        for t, task in enumerate(shared['Tasks']):
            _logger.debug('Execute {} in order: {} of {}: {}'.format(shared['Title'], t+1, len(shared['Tasks']), task['Title']))
            results.append(worker(task))
        return [result[1] for result in results]
    elif algorithm['Type'] == 'Process':
        _logger.debug('Execute {} in pool of {} processes ...'.format(shared['Title'], algorithm['Count']))
        #
        # Known Issue:
        # - https://bugs.python.org/issue9400
        # - Python multiprocessing.Pool is buggy at join()
        # Reference:
        # - https://stackoverflow.com/questions/15314189/python-multiprocessing-pool-hangs-at-join
        #
        results = []
        try:
            with multiprocessing.Pool(processes=algorithm['Count']) as pool:
                results = pool.map(worker, shared['Tasks'])
                pool.close()
                pool.join()
        except Exception:
            traceback.print_exc()
        # Results are always sorted in pool.
        return [result[1] for result in results]
    elif algorithm['Type'] == 'Thread':
        import concurrent.futures
        _logger.debug('Execute {} in pool of {} threads ...'.format(shared['Title'], algorithm['Count']))
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=algorithm['Count'])
        results = executor.map(worker, shared['Tasks'])
        return [result[1] for result in results]
    raise ValueError(format_error_message('Found undefined concurrency algorithm.', expected='One of: {}, {}, {}'.format('Sequential', 'Pool', 'Process'), got=algorithm['Type'], suggestions=('Check if this API is up to date', 'retry me'), action='Aborted'))


def profile_runs(funcname, modulefile, nruns=5):
    module_name = splitext(basename(modulefile))[0]
    stats_dir = join(abspath(dirname(modulefile)), 'stats')
    try:
        os.makedirs(stats_dir)
    except Exception:
        traceback.print_exc()
    for i in range(nruns):
        stats_file = join(stats_dir, 'profile_{}_{}.pstats.log'.format(funcname, i))
        profile.runctx('import {}; print({}, {}.{}())'.format(module_name, i, module_name, funcname), globals(), locals(), stats_file)
    # Read all 5 stats files into a single object
    stats = pstats.Stats(join(stats_dir, 'profile_{}_0.pstats.log'.format(funcname)))
    for i in range(1, nruns):
        stats.add(join(stats_dir, 'profile_{}_{}.pstats.log'.format(funcname, i)))
    # Clean up filenames for the report
    stats.strip_dirs()
    # Sort the statistics by the cumulative time spent
    # in the function
    stats.sort_stats('cumulative')
    stats.print_stats()


def get_local_tmp_dir():
    plat = platform.system()
    if plat == 'Windows':
        return join(os.getenv('LOCALAPPDATA'), 'Temp')
    elif plat == 'Darwin':
        return join(expanduser('~'), 'Library', 'Caches')
    elif plat == 'Linux':
        return '/tmp'
    else:
        raise NotImplementedError(f'unsupported platform: {plat}')


def write_plist_fields(cfg_file, my_map):
    plist = {}
    with open(cfg_file, 'rb') as fp:
        plist = plistlib.load(fp, fmt=plistlib.FMT_XML)
    plist.update(my_map)
    with open(cfg_file, 'wb') as fp:
        plistlib.dump(plist, fp)


def substitute_keywords_in_file(file, str_map, useliteral=False):
    updated = ''
    with open(file) as f:
        original = f.read()
        if not useliteral:
            updated = original % str_map 
        else:
            updated = original
            for src, dest in str_map.items():
                tmp = updated
                updated = updated.replace(src, dest)
    with open(file, 'w') as f:
        f.write(updated)


def is_uuid(text, version=4):
    try:
        uuid_obj = uuid.UUID(text, version=4)
        return True
    except ValueError:
        return False


def get_clipboard_content():
    import tkinter as tk
    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    content = root.clipboard_get()
    root.quit()
    return content


def alert(title, content, action='Close'):
    if platform.system() == 'Windows':
        cmd = ['mshta', f'vbscript:Execute("msgbox ""{content}"", 0,""{title}"":{action}")']
        os.system(' '.join(cmd))
        return
    if platform.system() == 'Darwin':
        cmd = ['osascript', '-e', f'display alert "{title}" message "{content}"']
    else:
        cmd = ['echo', f'{title}: {content}: {action}']
    subprocess.run(cmd)


def convert_to_wine_path(path, drive='Z:'):
    path = abspath(path).replace('/', '\\')
    return drive + path


def convert_from_wine_path(path):
    path = path.strip()
    if path.startswith('Z:') or path.startswith('z:'):
        return path[2:].replace('\\', '/') if len(path) > 2 else '/'
    elif path.startswith('Y:') or path.startswith('y:'):
        return join(os.environ['HOME'], path[2:].replace('\\', '/').strip('/'))
    return path


def kill_process_by_name(name):
    if platform.system() == 'Windows':
        cmd = ['taskkill', '/IM', name, '/F']
    else:
        cmd = ['pkill', name]
    subprocess.run(cmd)


def init_translator(localedir, domain='all', langs=None):
    """
    - select locale and set up translator based on system language
    - the leading language in langs, if any, is selected to override current locale
    """
    cur_langs = None
    if langs:
        cur_langs = langs
    else:
        cur_locale, encoding = locale.getdefaultlocale()
        cur_langs = [cur_locale] if cur_locale else ['en']
    try:
        translator = gettext.translation(domain, localedir=localedir, languages=cur_langs)
        translator.install()
        trans = translator.gettext
    except FileNotFoundError as e:
        # No translation files found for domain. 
        # Ignore this message if called for the first time.
        trans = str
    return trans


def match_files_except_lines(file1, file2, excluded=None):
    with open(file1) as fp:
        content1 = fp.readlines()
    with open(file2) as fp:
        content2 = fp.readlines()
    if excluded:
        excluded = [excluded] if type(excluded).__name__ == 'int' else excluded
        content1 = [cont for c, cont in enumerate(content1) if c not in excluded]
        content2 = [cont for c, cont in enumerate(content2) if c not in excluded]
    return content1 == content2


class RerunLock:
    """Lock process from reentering when seeing lock file on disk."""
    def __init__(self, name, folder=None, infohook=_logger.info, warnhook=_logger.warning, errorhook=_logger.error):
        os.makedirs(folder, exist_ok=True)
        filename = 'lock_{}'.format(name) if name else 'lock_{}'.format(next(tempfile._get_candidate_names()))
        self.lockFile = join(folder, filename) if folder else join(_script_dir, os.pardir, filename)
        self.infoHook = infohook
        self.warnHook = warnhook
        self.errorHook = errorhook

    def lock(self):
        if not self.is_locked():
            with open(self.lockFile, 'w') as f:
                pass
            return True
        else:
            self.warnHook('Will not run the script while it is active with pid: {}.'.format(os.getpid()))
            return False

    def unlock(self):
        try:
            os.remove(self.lockFile)
        except FileNotFoundError:
            self.warnHook('Script reentrance is already enabled.')
        except Exception:
            failure = traceback.format_exc()
            self.errorHook('{}\nFailed to unlock the script. You must delete the lock by hand: {}.'.format(failure, self.lockFile))

    def is_locked(self):
        return exists(self.lockFile)


def rerun_lock(name, folder=None, infohook=_logger.info, warnhook=_logger.warning, errorhook=_logger.error):
    """Decorator for reentrance locking on functions"""
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            my_lock = None
            ret = None
            try:
                my_lock = RerunLock(name, folder, infohook, warnhook, errorhook)
                if not my_lock.lock():
                    return 1
                ret = f(*args, **kwargs)
                my_lock.unlock()
            except Exception as e:  
                my_lock.unlock()
                # leave exception to its upper handler or let the program crash
                raise e
            return ret
        return wrapper
    return decorator


def append_to_os_paths(bindir):
    """
    On macOS, PATH update will only take effect after calling `source ~/.bash_profile` directly in shell. It won't work 
    """
    if platform.system() == 'Windows':
        import winreg
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as reg:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_ALL_ACCESS) as key:
                user_paths, _ = winreg.QueryValueEx(key, 'Path')
                if bindir not in user_paths:
                    if user_paths[-1] != ';':
                        user_paths += ';'
                    user_paths += f'{bindir}'
                    winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, user_paths)
    else:
        cfg_file = os.path.expanduser('~/.bash_profile') if platform.system() == 'Darwin' else os.path.expanduser('~/.bashrc')
        if bindir in os.environ['PATH']:
            return
        with open(cfg_file, 'a') as fp:
            fp.write(f'\nexport PATH="$PATH:{bindir}"\n\n')
    os.environ['PATH'] += os.pathsep + bindir


def prepend_to_os_paths(bindir):
    if platform.system() == 'Windows':
        import winreg
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as reg:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_ALL_ACCESS) as key:
                user_paths, _ = winreg.QueryValueEx(key, 'Path')
                if bindir not in user_paths:
                    user_paths = f'{bindir};' + user_paths
                    winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, user_paths)
    else:
        cfg_file = os.path.expanduser('~/.bash_profile') if platform.system() == 'Darwin' else os.path.expanduser('~/.bashrc')
        if bindir in os.environ['PATH']:
            return
        lines = []
        with open(cfg_file) as fp:
            lines = fp.readlines()
        lines = [f'\nexport PATH="{bindir}:$PATH"\n\n'] + lines
        with open(cfg_file, 'w') as fp:
            fp.writelines(lines)
    os.environ['PATH'] = bindir + os.pathsep + os.environ['PATH']


def remove_from_os_paths(bindir):
    if platform.system() == 'Windows':
        import winreg
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as reg:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_ALL_ACCESS) as key:
                user_paths, _ = winreg.QueryValueEx(key, 'Path')
                start = user_paths.find(bindir)
                if not bindir in user_paths:
                    return
                import re
                # escape to handle metachars
                pattern = re.compile('|'.join(map(re.escape, bindir)))
                pattern.sub('', user_paths)
                winreg.SetValueEx(key, 'Path', 0, winreg.REG_EXPAND_SZ, user_paths)
    else:
        cfg_file = os.path.expanduser('~/.bash_profile') if platform.system() == 'Darwin' else os.path.expanduser('~/.bashrc')
        if not bindir in os.environ['PATH']:
            return
        keyword = r'^[\s](*)export PATH="{}:$PATH"'.format(bindir)
        # escape to handle metachars
        pattern_prepend = f'export PATH="{bindir}:$PATH"'
        pattern_append = f'export PATH="$PATH:{bindir}"'
        lines = []
        with open(cfg_file) as fp:
            lines = fp.readlines()
        for l, line in enumerate(lines):
            line = line.strip()
            if line.startswith(pattern_prepend):
                lines[l] = line.replace(pattern_prepend, '')
            if line.startswith(pattern_append):
                lines[l] = line.replace(pattern_append, '')
        with open(cfg_file, 'w') as fp:
            fp.writelines(lines)
    os.environ['PATH'] = os.environ['PATH'].replace(bindir, '')


def run_cmd(cmd, cwd='.', logger=None):
    if logger:
            logger.debug(' '.join(cmd))
    else:
        print(' '.join(cmd))
    proc = None
    try:
        proc = subprocess.run(cmd, check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
        log = proc.stdout.decode(TXT_CODEC)
        if logger:
            logger.debug(log)
        else:
            print(log)
    except subprocess.CalledProcessError as e:
        log = f'stdout: {e.stdout.decode(TXT_CODEC)}'
        err = f'stderr: {e.stderr.decode(TXT_CODEC)}'
        if logger:
            logger.info(log)
            logger.error(err)
        else:
            print(log)
            print(err)
        raise e
    except Exception as e:
        if logger:
            logger.error(e)
        raise e
    return proc

def run_daemon(cmd, cwd='.', logger=None):
    proc = None
    try:
        proc = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
        if logger:
            logger.debug(proc.stdout.decode(TXT_CODEC))
    except subprocess.CalledProcessError as e:
        if logger:
            logger.info(f'stdout: {e.stdout.decode(TXT_CODEC)}')
            logger.error(f'stderr: {e.stderr.decode(TXT_CODEC)}')
        raise e
    except Exception as e:
        if logger:
            logger.error(e)
        raise e
    return proc


def extract_call_args(file, caller, callee):
    """
    - only support literal args
    - will throw if an arg value is a function call itself
    """
    import ast
    import importlib
    import inspect
    mod_name = splitext(basename(file))[0]
    if mod_name in sys.modules:
        sys.modules.pop(mod_name)
    sys.path.insert(0, dirname(file))
    mod = importlib.import_module(mod_name)
    parsed = ast.parse(inspect.getsource(mod))
    raw_calls = { # lineno, args, keywords
        'func': [],
        'method': []
    }
    for node in parsed.body:
        if not isinstance(node, ast.FunctionDef) \
            or node.name != caller:
            continue
        # hit function definition
        # next: find function calls in this function
        caller_def = node
        callee_calls = []
        for node in caller_def.body:
            if 'value' not in dir(node) or not isinstance(node.value, ast.Call):
                continue
            # hit a function/method call
            call_type = None
            found_func_call = isinstance(node.value.func, ast.Name) and node.value.func.id == callee
            found_method_call = isinstance(node.value.func, ast.Attribute) and node.value.func.attr == callee
            if found_func_call:
                call_type = 'func'
            elif found_method_call:
                call_type = 'method'
            else:
                continue
            raw_calls[call_type].append(node.value)

    # collect args and kwargs
    calls = { # lineno, args, keywords
        'func': [],
        'method': []
    }
    def get_kwarg_value_const(kw):
        return kw.value.value
    def get_kwarg_value_name(kw):
        return kw.value.id
    def get_kwarg_value_list(kw):
        nodes = kw.value.elts
        values = []
        for node in nodes:
            if not isinstance(node, ast.Constant):
                values.append(None)
                continue
            values.append(node.value)
        return values
    def get_kwarg_value_misc(kw):
        return None

    for calltype, rc in raw_calls.items():
        for call in rc:
            args = []
            kwargs = []
            for arg in call.args:
                args.append(arg.value)
            for kw in call.keywords:
                key = kw.arg
                if isinstance(kw.value, ast.Constant):
                    value = get_kwarg_value_const(kw)
                elif isinstance(kw.value, ast.Name):
                    value = get_kwarg_value_name(kw)
                elif isinstance(kw.value, (ast.List, ast.Tuple)):
                    value = get_kwarg_value_list(kw)
                else:
                    print(f'Unsupported syntax node: {kw.value}. Will fallback to None.')
                    value = None
                kwargs.append((key, value))
            record = {
                'args': args,
                'kwargs': {k: v for k, v in kwargs},
                'lineno': call.lineno,
                'end_lineno': call.end_lineno,
            }
            calls[calltype].append(record)
    if mod_name in sys.modules:
        sys.modules.pop(mod_name)
    return calls['func'], calls['method']


def extract_class_attributes(file, classname):
    """
    assume
    - class is defined at the top-level of source file
    - all attributes are defined in constructor
    - all assignments must be about attributes, no local variable are allowed
    - attributes can use type-annotated assignemts (taa)
    - types of attributes without taa can be inferred from constant values
    """
    import ast
    import importlib
    import inspect
    mod_name = splitext(basename(file))[0]
    if mod_name in sys.modules:
        sys.modules.pop(mod_name)
    sys.path.insert(0, dirname(file))
    mod = importlib.import_module(mod_name)
    parsed = ast.parse(inspect.getsource(mod))
    
    class_node = None
    for node in parsed.body:
        if not isinstance(node, ast.ClassDef):
            continue
        if node.name != classname:
            continue
        class_node = node
    if not class_node:
        return None    
    ctor = None
    for node in ast.walk(class_node):
        if isinstance(node, ast.FunctionDef) and node.name == '__init__':
            ctor = node
            break;
    if not ctor:
        return None
    # parse ctor
    names = [node.attr for node in ast.walk(ctor) if isinstance(node, ast.Attribute)]
    # types = [node.annotation.id for node in ast.walk(ctor) if isinstance(node, ast.AnnAssign)]
    types = []
    values = []
    linenos = []
    end_linenos = []
    for node in ast.walk(ctor):
        if not isinstance(node, (ast.AnnAssign, ast.Assign)):
            continue
        attr_type = None
        attr_value = None
        if isinstance(node, ast.AnnAssign):
            attr_type = node.annotation.id
        if isinstance(node.value, ast.Constant):
            if not attr_type:
                attr_type = type(node.value.value).__name__
            attr_value = node.value.value
        elif isinstance(node.value, (ast.List, ast.Tuple)):
            nodes = node.value.elts
            raw_values = []
            for nd in nodes:
                # only support constants inside list
                # non-consts are taken as None
                rv = nd.value if isinstance(nd, ast.Constant) else None
                raw_values.append(rv)
            if not attr_type:
                attr_type = 'list' if isinstance(nd.value, ast.List) else 'tuple'
            attr_value = raw_values
        types.append(attr_type)
        values.append(attr_value)
        linenos.append(node.lineno)
        end_linenos.append(node.end_lineno)
    attributes = [{'name': n, 'type': t, 'default': v, 'lineno': l, 'end_lineno': e} for n, t, v, l, e in zip(names, types, values, linenos, end_linenos)]
    if mod_name in sys.modules:
        sys.modules.pop(mod_name)
    return attributes


def extract_local_var_assignments(file, caller, varname):
    """
    - only support regular assignments (var_name = literal_value)
    """
    value = None
    import ast
    import importlib
    import inspect
    mod_name = splitext(basename(file))[0]
    if mod_name in sys.modules:
        sys.modules.pop(mod_name)
    sys.path.insert(0, dirname(file))
    mod = importlib.import_module(mod_name)
    parsed = ast.parse(inspect.getsource(mod))
    raw_calls = { # lineno, args, keywords
        'func': [],
        'method': []
    }
    assignments = []
    for node in parsed.body:
        if not isinstance(node, ast.FunctionDef) \
            or node.name != caller:
            continue
        # hit function definition
        # next: find function calls in this function
        func_def = node
        for node in ast.walk(func_def):
            if not isinstance(node, ast.Assign) or len(node.targets) > 1:
                continue
            var = node.targets[0]
            if not isinstance(var, ast.Name) or var.id != varname:
                continue
            if not isinstance(node.value, ast.Constant):
                continue
            ass = {
                'lineno': node.lineno,
                'end_lineno': node.end_lineno,
                'value': node.value.value
            }
            assignments.append(ass)
    if mod_name in sys.modules:
        sys.modules.pop(mod_name)
    return assignments


def extract_imported_modules(file):
    def _extract_import_module(node):
        return [alias.name for alias in node.names]

    def _extract_from_module_import(node):
        return node.module
    imported = []
    import ast
    import importlib
    import inspect
    mod_name = splitext(basename(file))[0]
    if mod_name in sys.modules:
        sys.modules.pop(mod_name)
    sys.path.insert(0, dirname(file))
    mod = importlib.import_module(mod_name)
    parsed = ast.parse(inspect.getsource(mod))
    for node in ast.walk(parsed):
        if not isinstance(node, (ast.Import, ast.ImportFrom)):
            continue
        if isinstance(node, ast.Import):
            extracted = _extract_import_module(node)
            if extracted:
                imported += extracted
            continue
        extracted = _extract_from_module_import(node)
        if extracted:
            imported.append(extracted)
    if mod_name in sys.modules:
        sys.modules.pop(mod_name)
    return sorted(list(set(imported)))


def substitute_lines_between_keywords(lines, file, opkey, edkey, startlineno=0, withindent=True):
    """
    - assume input lines all have line ends
    - align inserted text with tags via identical indents
    - optimize with search range slicing
    - returns original indices
    """
    all_lines = []
    with open(file) as fp:
        all_lines = fp.readlines()
    selected_lines = all_lines[startlineno:] if startlineno > 0 else all_lines
    # find range
    rg_insert = [None, None]
    rg_insert[0] = next((l for l, line in enumerate(selected_lines) if line.strip().startswith(opkey) ), None)
    if not rg_insert[0]:
        return rg_insert
    rg_insert[1] = next((l for l, line in enumerate(selected_lines[rg_insert[0]:]) if line.strip().startswith(edkey) ), None)
    if not rg_insert[1]:
        return (startlineno+rg_insert[0], None)
    # back to all lines with offset applied
    rg_insert[0] += startlineno
    rg_insert[1] += rg_insert[0]
    if withindent:
        indent = all_lines[rg_insert[0]].find(opkey)
        indent_by_spaces = 0
        for idt in range(indent):
            indent_by_spaces += 4 if all_lines[rg_insert[0]][idt] == '\t' else 1
        assert indent_by_spaces >= 0
        lines = ['{}{}'.format(' '*indent_by_spaces, line) for line in lines]
    # remove lines in b/w
    has_lines_between_keywords = rg_insert[1] - rg_insert[0] > 1
    if has_lines_between_keywords:
        del all_lines[rg_insert[0]+1 : rg_insert[1]]
    all_lines[rg_insert[0]+1 : rg_insert[0]+1] = lines
    with open(file, 'w') as fp:
        fp.writelines(all_lines)
    rg_inserted = [rg_insert[0], rg_insert[0]+len(lines)]
    return rg_inserted


def convert_compound_cases(snake_text, style='pascal'):
    if style == 'oneword':
        return snake_text.replace('_', '').lower()
    if style == 'ONEWORD':
        return snake_text.replace('_', '').upper()
    if style == 'SNAKE':
        return snake_text.upper()
    if style == 'kebab':
        return snake_text.replace('_', '-')
    out_text = [s.capitalize() for s in snake_text.split('_')]
    if style == 'camel':
        out_text[0] = out_text[0].lower()
    return ''.join(out_text)


def combine_words(words, style='snake'):
    out_text = '_'.join(words)
    if style == 'snake':
        return out_text
    if style == 'sentence':
        return ' '.join(words)
    if style == 'Sentence':
        return ' '.join(words).capitalize()
    if style == 'title':
        return ' '.join([word.capitalize() for word in words])
    return convert_compound_cases(out_text, style)


def append_lineends_to_lines(lines, style='posix'):
    lineend = '\r\n' if style == 'windows' else '\n'
    return [line + lineend for line in lines]


def zip_dir(srcdir, dstbasename=None):
    """
    zip the entire folder into a zip file under the same parent folder.
    """
    def _zip_dir_windows(srcdir, dstbasename):
        src_par, src_name = osp.split(srcdir)
        if not dstbasename:
            dstbasename = src_name
        elif dstbasename != src_name:
            dst_dir = osp.join(src_par, dstbasename)
            duplicate_dir(srcdir, dst_dir)
        out_file = osp.join(src_par, dstbasename+'.zip')
        cmd = ['tar', '-cf', out_file, '-C', src_par, dstbasename]
        run_cmd(cmd, src_par)

    def _zip_dir_macos(srcdir, dstbasename):
        src_par, src_name = osp.split(srcdir)
        rename_option = []
        if not dstbasename:
            dstbasename = src_name
        elif dstbasename != src_name:
            dst_dir = osp.join(src_par, dstbasename)
            rename_option = ['-s', f'/^{src_name}/{dstbasename}/']
        out_file = osp.join(src_par, dstbasename+'.zip')
        cmd = ['tar', '-czf', out_file, '--exclude', '.DS_Store', '--exclude', '*/__MACOSX'] + rename_option + ['-C', src_par, f'{src_name.strip(os.path.sep)}/']
        run_cmd(cmd, src_par)

    if platform.system() == 'Windows':
        _zip_dir_windows(srcdir, dstbasename)
        return
    _zip_dir_macos(srcdir, dstbasename)


def unzip_dir(srcball, destpardir):
    """
    assume srcball has a top-level folder "product".
    unzip to destpardir/product.
    """
    untar_option = '-xf' if platform.system() == 'Windows' else '-xzf'
    os.makedirs(destpardir, exist_ok=True)
    cmd = ['tar', untar_option, srcball, '-C', destpardir]
    run_cmd(cmd, destpardir)
    

def duplicate_dir(srcdir, dstdir):
    def _dup_dir_posix(srcdir, dstdir):
        if not srcdir.endswith('/'):
            srcdir += '/'
        cmd = ['rsync', '-a', '--delete', srcdir, dstdir.strip('/')]
        run_cmd(cmd, '/')

    def _dup_dir_windows(srcdir, dstdir):
        cmd = ['xcopy', '/I', '/E', '/Q', '/Y', srcdir, f'{dstdir}\\']
        run_cmd(cmd, srcdir)

    if platform.system() == 'Windows':
        _dup_dir_windows(srcdir, dstdir)
        return
    _dup_dir_posix(srcdir, dstdir)


def compare_textfiles(file1, file2, showdiff=False, contextonly=True, logger=None):
    with open(file1) as fp1, open(file2) as fp2:
        lines1 = fp1.readlines()
        lines2 = fp2.readlines()
        if showdiff:
            diff_func = difflib.context_diff if contextonly else difflib.Differ().compare
            diff = diff_func(lines1, lines2)
            lazy_logging(''.join(diff))
    assert lines1 == lines2, f'content different: {file1} vs. {file2}'


def lazy_logging(msg, logger=None):
    if logger:
        logger.info(msg)
    else:
        print(msg)


def copy_file(src, dst, isdstdir=False):
    if isdstdir:
        par_dir = dst
    else:
        par_dir = osp.split(dst)[0]
    os.makedirs(par_dir, exist_ok=True)
    try:
        shutil.copy(src, dst)
    except shutil.SameFileError:
        _logger.warning(f'source and destination are identical. will not copy: {osp.abspath(src)} -> {osp.abspath(dest)}. skipped.')


def compare_dirs(dir1, dir2, ignoreddirpatterns=(), ignoredfilepatterns=(), showdiff=True):
    def _collect_folders_files(my_dir):
        n_truncates = len(my_dir)
        my_dir_contents = {
            'dirs': [],
            'files': [],
        }
        for root, folders, files in os.walk(my_dir):
            for folder in folders:
                folder_matching_pattern = next((pat for pat in ignoreddirpatterns if pat in folder), None)
                if folder_matching_pattern:
                    continue
                my_dir_contents['dirs'].append(osp.join(root, folder)[n_truncates+1:])
            for file in files:
                file_matching_pattern = next((pat for pat in ignoredfilepatterns if fnmatch.fnmatch(file, pat)), None)
                if file_matching_pattern:
                    continue
                my_dir_contents['files'].append(osp.join(root, file)[n_truncates+1:])
        
        my_dir_contents['dirs'] = sorted(my_dir_contents['dirs'])
        my_dir_contents['files'] = sorted(my_dir_contents['files'])
        return my_dir_contents
    dir1_contents = _collect_folders_files(dir1)
    dir2_contents = _collect_folders_files(dir2)
    if showdiff:
        import filecmp
        dc = filecmp.dircmp(dir1, dir2, ignore=list(ignoreddirpatterns))
        dc.report_full_closure()
        pp.pprint(f'dir1: {dir1_contents}')
        pp.pprint(f'dir2: {dir2_contents}')
    assert dir1_contents['dirs'] == dir2_contents['dirs'], 'folders different:\n{}\n\nvs.\n\n{}'.format(pp.pformat(dir1_contents['dirs'], indent=2), pp.pformat(dir2_contents['dirs'], indent=2))
    assert dir1_contents['files'] == dir2_contents['files'], 'files different:\n{}\n\nvs.\n\n{}'.format(pp.pformat(dir1_contents['files'], indent=2), pp.pformat(dir2_contents['files'], indent=2))


def _test():
    pass


if __name__ == '__main__':
    _test()
