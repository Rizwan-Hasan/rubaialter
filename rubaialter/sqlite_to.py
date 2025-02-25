import os
import sqlite3
import typing

import pandas as pd


def sqlite_to_csv(inputFilePath: str) -> typing.NoReturn:
    conn = sqlite3.connect(inputFilePath)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()

    for table in table_names:
        print(f"Processing {table[0]} ...")
        df = pd.read_sql(sql=f"SELECT * FROM {table[0]}", con=conn)
        df.to_csv(f"{table[0]}.csv", encoding="utf-8", index=False)
        print(f"Processing {table[0]} is done. {table[0]}.csv is ready!")
    conn.close()
    print("All processes are done!")


def sqlite_to_tsv(inputFilePath: str) -> typing.NoReturn:
    conn = sqlite3.connect(inputFilePath)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()

    for table in table_names:
        print(f"Processing {table[0]} ...")
        df = pd.read_sql(sql=f"SELECT * FROM {table[0]}", con=conn)
        df.to_csv(f"{table[0]}.tsv", encoding="utf-8", index=False, sep="\t")
        print(f"Processing {table[0]} is done. {table[0]}.tsv is ready!")
    conn.close()
    print("All processes are done!")


def sqlite_to_xlsx(inputFilePath: str, extension="xlsx") -> typing.NoReturn:
    conn = sqlite3.connect(inputFilePath)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()
    filename, file_extension = os.path.splitext(
        os.path.basename(inputFilePath)
    )  # Get File Name & Extension
    newFileName = filename + f".{extension}"
    with pd.ExcelWriter(newFileName) as writer:
        for table in table_names:
            print(f"Processing {table[0]} ...")
            df = pd.read_sql(sql=f"SELECT * FROM {table[0]}", con=conn)
            df.to_excel(writer, sheet_name=table[0])
            print(f"Processing {table[0]} is done.")
    print(f"All processes done. {newFileName} is ready!")
    conn.close()


def sqlite_to_xls(inputFilePath: str) -> typing.NoReturn:
    sqlite_to_xlsx(inputFilePath, extension="xls")


if __name__ == "__main__":
    print("Hello World")
