import os
import sqlite3
import typing

import pandas as pd


# xlsx functions
def xlsx_to_csv(inputFilePath: str) -> typing.NoReturn:
    excelDatafame = pd.ExcelFile(inputFilePath)
    # Traverse all the sheets in excel file
    for sheet in excelDatafame.sheet_names:
        print(f"Processing {sheet} ...")
        df = excelDatafame.parse(sheet)
        df.to_csv(sheet + ".csv", encoding="utf-8", index=False)
        print(f" Processing done. {sheet}.csv is ready!")
    print("All processes completed.")


def xlsx_to_tsv(inputFilePath: str) -> typing.NoReturn:
    excelDatafame = pd.ExcelFile(inputFilePath)
    # Traverse all the sheets in excel file
    for sheet in excelDatafame.sheet_names:
        print(f"Processing {sheet} ...")
        df = excelDatafame.parse(sheet)
        df.to_csv(sheet + ".tsv", encoding="utf-8", index=False, sep="\t")
        print(f" Processing done. {sheet}.tsv is ready!")
    print("All processes completed.")


def xlsx_to_sqlite(inputFilePath: str) -> typing.NoReturn:
    excelDatafame = pd.ExcelFile(inputFilePath)
    filename, file_extension = os.path.splitext(
        os.path.basename(inputFilePath)
    )  # Get File Name & Extension
    newFileName = filename + ".sqlite3"
    conn = sqlite3.connect(newFileName)
    # Traverse all the sheets in excel file
    for sheet in excelDatafame.sheet_names:
        print(f"Processing {sheet} ...")
        df = excelDatafame.parse(sheet)
        df.to_sql(name=sheet, con=conn, index=False)
        print(f" Processing {sheet} is done.")
    conn.commit()
    print(f"All processes completed.{newFileName} is ready!")
    conn.close()


def xlsx_to_xls(inputFilePath: str, extension="xls") -> typing.NoReturn:
    filename, file_extension = os.path.splitext(
        os.path.basename(inputFilePath)
    )  # Get File Name & Extension
    newFileName = f"{filename}.{extension}"
    excelDatafame = pd.ExcelFile(inputFilePath)
    with pd.ExcelWriter(newFileName) as writer:
        for sheet in excelDatafame.sheet_names:
            print(f"Processing {sheet} ...")
            df = excelDatafame.parse(sheet)
            df.to_excel(writer, sheet_name=sheet)
            print(f"Processing {sheet} is done.")
    print(f"All processes done. {newFileName} is ready!")


# xls functions
def xls_to_csv(inputFilePath: str) -> typing.NoReturn:
    xlsx_to_csv(inputFilePath)


def xls_to_tsv(inputFilePath: str) -> typing.NoReturn:
    xlsx_to_tsv(inputFilePath)


def xls_to_sqlite(inputFilePath: str) -> typing.NoReturn:
    xlsx_to_sqlite(inputFilePath)


def xls_to_xlsx(inputFilePath: str) -> typing.NoReturn:
    xlsx_to_xls(inputFilePath, extension="xlsx")


if __name__ == "__main__":
    print("Hello World")
