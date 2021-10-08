from datetime import datetime
from json import loads
from os import getenv
from sys import getsizeof
from time import sleep
from typing import Optional, Tuple

import chromedriver_binary
from pydantic.networks import HttpUrl
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome, DesiredCapabilities, Remote
from selenium.webdriver.chrome.options import Options

from ecoindex.ecoindex import get_ecoindex
from ecoindex.models import Page, PageMetrics, PageType, Result, WindowSize


async def get_page_analysis(
    url: HttpUrl,
    window_size: Optional[WindowSize] = WindowSize(width=1920, height=1080),
) -> Result:
    page_metrics, page_type = await scrap_page(url=url, window_size=window_size)
    ecoindex = await get_ecoindex(
        dom=page_metrics.nodes, size=page_metrics.size, requests=page_metrics.requests
    )
    return Result(
        score=ecoindex.score,
        ges=ecoindex.ges,
        water=ecoindex.water,
        grade=ecoindex.grade,
        url=url,
        date=datetime.now(),
        width=window_size.width,
        height=window_size.height,
        nodes=page_metrics.nodes,
        size=page_metrics.size,
        requests=page_metrics.requests,
        page_type=page_type,
    )


async def scrap_page(
    url: HttpUrl, window_size: WindowSize
) -> Tuple[PageMetrics, PageType]:
    remote_chrome = getenv("REMOTE_CHROME_URL")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"--window-size={window_size}")
    chrome_options.add_argument("--no-sandbox")

    capbs = DesiredCapabilities.CHROME.copy()
    capbs["goog:loggingPrefs"] = {"performance": "ALL"}

    driver = (
        Remote(
            command_executor=remote_chrome,
            options=chrome_options,
            desired_capabilities=capbs,
        )
        if remote_chrome
        else Chrome(
            desired_capabilities=capbs,
            chrome_options=chrome_options,
        )
    )

    driver.set_script_timeout(10)
    driver.get(url)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # TODO : Find a way to wait for all elements downloaded after scrolling to bottom
    sleep(1)

    page_type = await get_page_type(driver)
    page_metrics = await get_page_metrics(driver)

    driver.quit()

    return page_metrics, page_type


async def get_page_metrics(driver: Chrome) -> PageMetrics:
    page = Page(
        logs=driver.get_log("performance"),
        outer_html=driver.execute_script("return document.documentElement.outerHTML"),
        nodes=driver.find_elements_by_xpath("//*"),
    )
    downloaded_data = [
        loads(log["message"])["message"]["params"]["encodedDataLength"]
        for log in page.logs
        if "INFO" == log["level"] and "Network.loadingFinished" in log["message"]
    ]

    return PageMetrics(
        size=(sum(downloaded_data) + getsizeof(page.outer_html)) / (10 ** 3),
        nodes=len(page.nodes),
        requests=len(downloaded_data),
    )


async def get_page_type(driver: Chrome) -> Optional[PageType]:
    try:
        page_type = driver.find_element_by_xpath(
            "//meta[@property='og:type']"
        ).get_attribute("content")
    except (NoSuchElementException):
        page_type = None

    return page_type
