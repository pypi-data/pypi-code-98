import datetime
import os
import sys
import time
from typing import Any, Optional

from . import (getAllFileList, getFileBaseName, getPath, hold, makeFolder,
               readFile, remove, writeFile)
from .log import (error, getCountCritical, getCountError, getCountWarning,
                  info, initLogger, warning)
from .print import (BACKGROUND_DARKGREEN, BACKGROUND_DARKPINK,
                    BACKGROUND_DARKRED, BACKGROUND_DARKYELLOW,
                    FOREGROUND_BLACK, FOREGROUND_DARKRED, FOREGROUND_WHITE,
                    resetPrintColor, setPrintColor)

TaskDataType = tuple[str, Optional[dict[str, Any]]]

_workspacePath: str = ""


def initTask(exeWorkspace: str, devWorkspace: str, devTaskList: list[TaskDataType]):
    global _workspacePath
    if _isDev():
        _workspacePath = getPath(devWorkspace)
        _runTaskList(devTaskList)
    else:
        _workspacePath = getPath(exeWorkspace)
        _runTaskFile(sys.argv[-1])


def getPathByWorkspace(*parList: str) -> str:
    return getPath(_workspacePath, *parList)


def runTask(moduleName: str, **parDict: dict[str, Any]):
    exec(f"import {moduleName}")
    module = eval(moduleName)
    for k, v in parDict.items():
        if hasattr(module, k):
            setattr(module, k, v)
        else:
            warning(f"模块缺少属性定义 module={moduleName} k={k} v={v}")
    module.run()
    if hasattr(module, "clean"):
        module.clean()


def _isDev():
    return sys.executable.endswith("python.exe")


def _checkLockFile():
    lockFile = getPath(_workspacePath, "task.lock")
    if os.path.isfile(lockFile):
        print(f"不支持重复执行 {lockFile}")
        hold("如果确认上次执行是意外退出，输入unlock可继续", True, "unlock")
    writeFile(lockFile, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return lockFile


def _setPrintRedColor():
    setPrintColor(FOREGROUND_DARKRED)


def _runTaskFile(file: str):
    isException = False
    taskList: list[TaskDataType] = []
    try:
        fileContent = readFile(file)
        findStr = ":: ---------------------------------------- ::"
        startIndex = fileContent.index(findStr)
        endIndex = fileContent.index(findStr, startIndex + 1)
        content = fileContent[startIndex + len(findStr):endIndex].strip().replace("\r\n", "\n")
        lineAry = content.split("\n")
        lineAry = [x[2:].strip() for x in lineAry]
        for line in lineAry:
            sepIndex = line.find(" ")
            parDict: dict[str, Any] = {}
            if sepIndex > -1:
                moduleName = line[:sepIndex].strip()
                parDict = eval(line[sepIndex:])
                assert type(parDict) == dict, f"参数无法解析成字典类型 line={line}"
            else:
                moduleName = line
            taskList.append((moduleName, parDict))
        assert len(taskList) > 0
        os.system(f"title={getFileBaseName(file)}")
    except:
        isException = True
        import traceback
        _setPrintRedColor()
        traceback.print_exc()
        print("解析执行文件失败")
    finally:
        resetPrintColor()
    if not isException:
        _runTaskList(taskList)


# [[moduleName, parDict], ...]
def _runTaskList(taskList: list[TaskDataType]):
    startTime = datetime.datetime.now()
    lockFile = None
    try:
        lockFile = _checkLockFile()
        logFolder = getPath(_workspacePath, "log")
        makeFolder(logFolder)
        for logFile in sorted(getAllFileList(logFolder), reverse=True)[100:]:
            remove(logFile)
        logFile = getPath(logFolder, f"{time.strftime('%Y%m%d_%H%M%S')}.log")
        initLogger(logFile=logFile)
        for taskItem in taskList:
            moduleName = taskItem[0]
            parDict = taskItem[1]
            if parDict:
                runTask(moduleName, **parDict)
            else:
                runTask(moduleName)
    except Exception:
        import traceback
        _setPrintRedColor()
        traceback.print_exc()
        error("执行失败")
    finally:

        if getCountCritical():
            color = FOREGROUND_WHITE | BACKGROUND_DARKPINK
        elif getCountError():
            color = FOREGROUND_WHITE | BACKGROUND_DARKRED
        elif getCountWarning():
            color = FOREGROUND_BLACK | BACKGROUND_DARKYELLOW
        else:
            color = FOREGROUND_BLACK | BACKGROUND_DARKGREEN

        setPrintColor(color)
        info("---------------------------------------------------------------------------")

        msgAry = ["任务结束"]
        if getCountCritical():
            msgAry.append(f"critical({getCountCritical()})")
        if getCountError():
            msgAry.append(f"error({getCountError()})")
        if getCountWarning():
            msgAry.append(f"warning({getCountWarning()})")

        setPrintColor(color)
        info(" ".join(msgAry))

        passTime = str(datetime.datetime.now() - startTime)
        if passTime.startswith("0:"):
            passTime = "0" + passTime

        setPrintColor(color)
        info(f"用时：{passTime}")

        resetPrintColor()
        if lockFile:
            remove(lockFile)

        if not _isDev():
            while True:
                time.sleep(1)
