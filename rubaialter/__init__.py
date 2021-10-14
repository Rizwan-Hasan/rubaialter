import argparse
import logging
import os
import pathlib
import sys
import typing

from rubaialter import converter

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")


class rubaialter:
    def __init__(self) -> typing.NoReturn:
        self.__args = self.__Arguments()
        self.__Checking()
        self.__Conversion()

    # Arguments Parser ↓
    def __Arguments(self) -> dict:
        parser = argparse.ArgumentParser(
            description="A module for altering datasets formats made on top of Pandas"
        )

        # Taking Files ↓
        parser.add_argument(
            "filenames",
            type=pathlib.Path,
            nargs="+",
            help=".csv, .xls, .xlsx, .sqlite3, .tsv",
        )

        # To CSV ↓
        parser.add_argument(
            "--csv",
            default=False,
            action="store_true",
            help="Convert to csv",
        )

        # To TSV ↓
        parser.add_argument(
            "--tsv",
            default=False,
            action="store_true",
            help="Convert to tsv",
        )

        # To XLS ↓
        parser.add_argument(
            "--xls",
            default=False,
            action="store_true",
            help="Convert to xls",
        )

        # To XLSX ↓
        parser.add_argument(
            "--xlsx",
            default=False,
            action="store_true",
            help="Convert to xlsx",
        )

        # To SQLITE3 ↓
        parser.add_argument(
            "--sqlite3",
            default=False,
            action="store_true",
            help="Convert to sqlite",
        )

        # Force ↓
        parser.add_argument(
            "--force",
            default=False,
            action="store_true",
            help="Enable overwriting",
        )

        return parser.parse_args().__dict__

    # Received File Checking ↓
    def __Checking(self) -> typing.NoReturn:
        valid: bool = True
        extensions: tuple = (".csv", ".xls", ".xlsx", ".sqlite3", ".tsv")

        for file in self.__args.get("filenames"):
            if not os.path.exists(file):
                logging.error(f'"{file}" doesn\'t exist.')
                valid = False
            if not os.path.isfile(file):
                logging.error(f'"{file}" is not a file')
                valid = False
            if os.path.splitext(file)[-1] not in extensions:
                logging.error(f'"{file}" is not a valid file')
                valid = False

        if not valid:
            sys.exit()

    # Conversion ↓
    def __Conversion(self) -> typing.NoReturn:
        for file in self.__args.get("filenames"):
            if self.__args.get("csv"):
                converter.toCSV(inputFilePath=file)
            if self.__args.get("tsv"):
                converter.toTSV(inputFilePath=file)
            if self.__args.get("xls"):
                converter.toXLS(inputFilePath=file)
            if self.__args.get("xlsx"):
                converter.toXLSX(inputFilePath=file)
            if self.__args.get("sqlite3"):
                converter.toSQLite(inputFilePath=file)


def main():
    try:
        rubaialter()
    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    print("Hello World")
