import json

import requests
from noteread.legado.shelf.base import BookSource
from notetool.log import logger
from tqdm import tqdm


def load_source(urls=None, cate1='1', book: BookSource = None):
    book = book or BookSource(lanzou_fid=4147049)
    for url in tqdm(urls):
        try:
            text = requests.get(url).text
            for line in json.loads(text):
                book.add_json(json.dumps(line), cate1=cate1)
        except Exception as e:
            logger.error(e)
