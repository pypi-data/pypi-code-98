import pickle
import pprint
from weakref import finalize
from pathlib import Path
from typing import Generator, List, Union, Iterator, Callable

DataSet = Union[Iterator, Callable[..., Generator[dict, None, None]]]


class Data:
    """A wrapper for data/data_stream.

    The class provides methods for working with data as a stream.

    Such approach to data analysis called........................................................
    """

    def __init__(self, data: DataSet, workflow: List[Callable] = None, cache=False):
        self._cache_filename = f"{id(self)}.pickle"
        self._data = data
        self._workflow = [] if workflow is None else workflow
        self._cache_status: bool = cache
        self._len = None
        self._length_hint = None  # The value is populated when we use limit method.
        self._finalizer = finalize(self, self.__remove)

    @property
    def len(self) -> int:
        """int: How many records in the Data stream.

        Notes:
        1. It is a wasteful operation if you are performing it on the Data object that has never been iterated before.

        2. If you want just to check emptiness, use is_empty property instead.
        """
        return self._len if self._len is not None else self.__calc_len()

    @property
    def is_empty(self) -> bool:
        """bool: Indicates that the Data object doesn't contain data."""
        for _ in self.__load_data(cache=self._cache_status, save_to_cache_during_iter=False):
            return False
        return True

    def __calc_len(self) -> int:
        # TODO - request rpt-data-provide provide "select count"
        for _ in self:
            pass
        return self._len

    def __remove(self):
        if self.__check_cache(self._cache_filename):
            path = Path("./").joinpath("temp").joinpath(self._cache_filename)
            path.unlink()
        del self._data

    def __length_hint__(self):
        if self._len is not None:
            return self._len
        elif self._length_hint != None:
            return self._length_hint
        else:
            # 2**13, though 8 - is a default value in CPython.
            # We usually have large number of data.
            return 8192

    def __iter__(self) -> DataSet:
        self._len = 0
        try:
            for record in self.__load_data(self._cache_status):
                yield record
                self._len += 1
        except StopIteration:
            return None

    def __load_data(self, cache: bool, save_to_cache_during_iter: bool = True) -> Generator[dict, None, None]:
        """Loads data from cache or data.

        Args:
            cache: Flag if you what write and read from cache.

        Returns:
            obj: Generator
        """
        if cache and self.__check_cache(self._cache_filename):
            working_data = self.__load_file(self._cache_filename)
            yield from working_data
        else:
            file = None
            if cache and save_to_cache_during_iter:
                filepath = f"./temp/{self._cache_filename}"
                file = open(filepath, "wb")
                try:
                    for record in self.__apply_workflow():
                        pickle.dump(record, file)
                        yield record
                finally:
                    if file:
                        file.close()
            else:
                yield from self.__apply_workflow()

    def __check_cache(self, filename: str) -> bool:
        """Checks whether file exist.

        Args:
            filename: Filename.

        Returns:
            File exists or not.

        """
        path = Path("./").joinpath("temp")
        path.mkdir(exist_ok=True)
        path = path.joinpath(filename)
        return path.is_file()

    def __load_file(self, filename: str) -> Generator[dict, None, None]:
        """Loads records from pickle file.

        Args:
            filename: Filepath.

        Yields:
            dict: Generator records.

        """
        path = Path("./").joinpath("temp").joinpath(filename)
        if not path.is_file():
            raise ValueError(f"{filename} isn't file.")

        if path.suffix != ".pickle":
            raise ValueError(f"File hasn't pickle extension.")

        with open(path.resolve(), "rb") as file:
            while True:
                try:
                    decoded_data = pickle.load(file)
                    yield decoded_data
                except EOFError:
                    break

    def __apply_workflow(self) -> Generator[dict, None, None]:
        """Creates generator records with apply workflow.

        Yields:
            dict: Generator records.

        """
        working_data = self._data() if callable(self._data) else self._data
        for record in working_data:
            for step in self._workflow:
                if isinstance(record, (list, tuple)):
                    record = [r for r in record if step["callback"](r) is not None]
                    if not record:
                        record = None
                        break
                else:
                    try:
                        record = step["callback"](record)
                    except StopIteration as e:
                        return
                    if record is None:
                        break

            if record is not None:
                if isinstance(record, (list, tuple)):
                    for r in record:
                        yield r
                else:
                    yield record

    def filter(self, callback: Callable) -> "Data":
        """Append `filter` to workflow.

        Args:
            callback: Filter function.
                This function should return True or False.
                If function returns False, the record will be removed from the dataflow.

        Returns:
            Data: Data object.

        """
        new_workflow = [*self._workflow.copy(), {"type": "filter", "callback": lambda record: record if callback(record) else None}]
        return Data(self._data, new_workflow, self._cache_status)

    def map(self, callback: Callable) -> "Data":
        """Append `transform` function to workflow.

        Args:
            callback: Transform function.

        Returns:
            Data: Data object.

        """
        new_workflow = [*self._workflow.copy(), {"type": "map", "callback": callback}]
        return Data(self._data, new_workflow, self._cache_status)

    def limit(self, num: int) -> "Data":
        """Limits the stream to `num` entries.

        Args:
            num: How many records will be provided.

        Returns:
            Data: Data object.

        """

        def callback(r):
            if callback.pushed < num:
                callback.pushed += 1
                return r
            else:
                callback.pushed = 0
                raise StopIteration

        callback.pushed = 0

        new_workflow = [*self._workflow.copy(), {"type": "limit", "callback": callback}]
        data_obj = Data(self._data, new_workflow, self._cache_status)
        data_obj._length_hint = num
        return data_obj

    def sift(self, limit: int = None, skip: int = None) -> Generator[dict, None, None]:
        """Skips and limits records.

        Args:
            limit: Limited records.
            skip: Skipped records.

        Yields:
            Generator records.

        """
        skipped = 0
        pushed = 0

        for record in self.__load_data(cache=self._cache_status, save_to_cache_during_iter=False):
            if skip is not None and skipped < skip:
                skipped += 1
                continue
            if limit is not None and pushed == limit:
                break
            yield record
            pushed += 1

    def use_cache(self, status: bool) -> "Data":
        """Change status cache.

        If True all requested data from rpt-data-provider will be saved to cache file.
        Further actions with Data object will be consume data from the cache file.

        Args:
            status(bool): Status.

        Returns:
            Data: Data object.

        """
        if status:
            self._cache_status = True
        else:
            self._cache_status = False

        return self

    def find_by(self, record_field, field_values) -> Generator:
        """Get the records whose field value is written in the field_values list.

        When to use:
            You have IDs of some messages and you want get them in the stream and stop searching
            when you find all elements.

        Args:
            record_field: The record field to be searched for in the field_values list.
            field_values: List of elements among which will be searched record[record_field].

        Yields:
            dict: Generator records.

        """
        values_for_find = list(field_values)
        for record in self:
            if values_for_find:
                if record[record_field] in values_for_find:
                    values_for_find.remove(record[record_field])
                    yield record
                else:
                    continue
            else:
                break

    def write_to_file(self, file: str) -> None:
        """Writes the stream data to txt file.

        Args:
            file: Path to file.

        """
        with open(file, "w") as txt_file:
            for record in self:
                txt_file.write(f"{pprint.pformat(record)}\n" + ("-" * 50) + "\n")

    def __str__(self):
        output = "------------- Printed first 5 records -------------\n"
        for index, record in enumerate(self.__load_data(cache=self._cache_status, save_to_cache_during_iter=False)):
            if index == 5:
                break
            output += pprint.pformat(record) + "\n"
        return output

    def __bool__(self):
        for _ in self.__load_data(cache=self._cache_status, save_to_cache_during_iter=False):
            return True
        return False
