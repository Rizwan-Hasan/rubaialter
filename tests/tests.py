import os
import shutil
import subprocess

# Global Variables ↓
inputFileCSV: str = "files/test.csv"
outputFileCSV: str = "test.csv"

inputFileTSV: str = "files/test.tsv"
outputFileTSV: str = "test.tsv"

inputFileXLS: str = "files/test.xls"
outputFileXLS: str = "test.xls"

inputFileXLSX: str = "files/test.xlsx"
outputFileXLSX: str = "test.xlsx"

inputFileSQLITE3: str = "files/test.sqlite3"
outputFileSQLITE3: str = "test.sqlite3"

# Preparation ↓
def test_prepare():
    try:
        shutil.rmtree("rubaialter")
    except FileNotFoundError:
        pass
    shutil.copytree("../rubaialter", "rubaialter")


# CSV to CSV ↓
def test_csv_to_csv():
    global inputFileCSV, outputFileCSV
    shutil.copyfile(inputFileCSV, outputFileCSV)
    output = subprocess.check_output(
        ["python", "-m", "rubaialter", inputFileCSV, "--csv"]
    )
    output = output.decode("utf-8").strip()
    os.remove(outputFileCSV)
    assert output == "The file is already in csv format."


# CSV to TSV ↓
def test_csv_to_tsv():
    global inputFileCSV, outputFileTSV
    shutil.copyfile(inputFileCSV, outputFileTSV)
    output = subprocess.check_output(
        ["python", "-m", "rubaialter", inputFileCSV, "--tsv"]
    )
    output = output.decode("utf-8").strip()
    os.remove(outputFileTSV)
    assert output == "The file is already in tsv format."


# CSV to XLS ↓
def test_csv_to_xls():
    global inputFileCSV, outputFileXLS
    subprocess.check_call(["python", "-m", "rubaialter", inputFileCSV, "--xls"])
    assert os.path.exists(outputFileXLS)
    os.remove(outputFileXLS)


# CSV to XLSX ↓
def test_csv_to_xlsx():
    global inputFileCSV, outputFileXLSX
    subprocess.check_call(["python", "-m", "rubaialter", inputFileCSV, "--xlsx"])
    assert os.path.exists(outputFileXLSX)
    os.remove(outputFileXLSX)


# CSV to SQLITE3 ↓
def test_csv_to_sqlite3():
    global inputFileCSV, outputFileSQLITE3
    subprocess.check_call(["python", "-m", "rubaialter", inputFileCSV, "--sqlite3"])
    assert os.path.exists(outputFileSQLITE3)
    os.remove(outputFileSQLITE3)


# XLS to XLS ↓
def test_xls_to_xls():
    global inputFileXLS, outputFileXLS
    output = subprocess.check_output(
        ["python", "-m", "rubaialter", inputFileXLS, "--xls"]
    )
    output = output.decode("utf-8").strip()
    assert output == "The file is already in xls format."


# XLS to CSV
def test_xls_to_csv():
    global inputFileXLS, outputFileCSV
    subprocess.check_call(["python", "-m", "rubaialter", inputFileXLS, "--csv"])
    assert os.path.exists("Sheet1.csv")
    os.remove("Sheet1.csv")


# XLS to TSV
def test_xls_to_tsv():
    global inputFileXLS, outputFileTSV
    subprocess.check_call(["python", "-m", "rubaialter", inputFileXLS, "--tsv"])
    assert os.path.exists("Sheet1.tsv")
    os.remove("Sheet1.tsv")


# xls to XLSX ↓
def test_xls_to_xlsx():
    global inputFileXLS, outputFileXLSX
    subprocess.check_call(["python", "-m", "rubaialter", inputFileXLS, "--xlsx"])
    assert os.path.exists(outputFileXLSX)
    os.remove(outputFileXLSX)


# xls to SQLITE3 ↓
def test_xls_to_sqlite3():
    global inputFileXLS, outputFileSQLITE3
    subprocess.check_call(["python", "-m", "rubaialter", inputFileXLS, "--sqlite3"])
    assert os.path.exists(outputFileSQLITE3)
    os.remove(outputFileSQLITE3)


# XLSX to XLSX ↓
def test_xlsx_to_xlsx():
    global inputFileXLSX, outputFileXLSX
    shutil.copyfile(inputFileXLSX, outputFileXLSX)
    output = subprocess.check_output(
        ["python", "-m", "rubaialter", inputFileXLSX, "--xlsx"]
    )
    output = output.decode("utf-8").strip()
    assert output == "The file is already in xlsx format."


# XLSX to CSV
def test_xlsx_to_csv():
    global inputFileXLSX, outputFileCSV
    subprocess.check_call(["python", "-m", "rubaialter", inputFileXLSX, "--csv"])
    assert os.path.exists("Sheet1.csv")
    os.remove("Sheet1.csv")


# XLSX to CSV
def test_xlsx_to_tsv():
    global inputFileXLSX, outputFileTSV
    subprocess.check_call(["python", "-m", "rubaialter", inputFileXLSX, "--tsv"])
    assert os.path.exists("Sheet1.tsv")
    os.remove("Sheet1.tsv")


# XLSX to XLS ↓
def test_xlsx_to_xls():
    global inputFileXLSX, outputFileXLS
    subprocess.check_call(["python", "-m", "rubaialter", inputFileXLSX, "--xls"])
    assert os.path.exists(outputFileXLS)
    os.remove(outputFileXLS)


# XLSX to SQLITE3 ↓
def test_xlsx_to_sqlite3():
    global inputFileXLSX, outputFileSQLITE3
    subprocess.check_call(["python", "-m", "rubaialter", inputFileXLSX, "--sqlite3"])
    assert os.path.exists(outputFileSQLITE3)
    os.remove(outputFileSQLITE3)


# SQLITE3 to SQLITE3 ↓
def test_sqlite_to_sqlite():
    global inputFileSQLITE3, outputFileSQLITE3
    shutil.copyfile(inputFileSQLITE3, outputFileSQLITE3)
    output = subprocess.check_output(
        ["python", "-m", "rubaialter", inputFileSQLITE3, "--sqlite3"]
    )
    output = output.decode("utf-8").strip()
    os.remove(outputFileSQLITE3)
    assert output == "The file is already in sqlite3 format."


# SQLITE3 to CSV
def test_sqlite3_to_csv():
    global inputFileSQLITE3, outputFileCSV
    subprocess.check_call(["python", "-m", "rubaialter", inputFileSQLITE3, "--csv"])
    assert os.path.exists("Sheet1.csv")
    os.remove("Sheet1.csv")


# SQLITE3 to CSV
def test_sqlite3_to_csv():
    global inputFileSQLITE3, outputFileTSV
    subprocess.check_call(["python", "-m", "rubaialter", inputFileSQLITE3, "--tsv"])
    assert os.path.exists("Sheet1.tsv")
    os.remove("Sheet1.tsv")


# SQLITE3 to XLS ↓
def test_sqlite3_to_xls():
    global inputFileSQLITE3, outputFileXLS
    subprocess.check_call(["python", "-m", "rubaialter", inputFileSQLITE3, "--xls"])
    assert os.path.exists(outputFileXLS)
    os.remove(outputFileXLS)


# SQLITE3 to XLSX ↓
def test_sqlite3_to_xlsx():
    global inputFileSQLITE3, outputFileXLSX
    subprocess.check_call(["python", "-m", "rubaialter", inputFileSQLITE3, "--xlsx"])
    assert os.path.exists(outputFileXLSX)
    os.remove(outputFileXLSX)


# CSV to XLS XLSX SQLITE3 ↓
def test_csv_to_xls_xlsx_sqlite3():
    global inputFileCSV, outputFileXLS
    subprocess.check_call(
        [
            "python",
            "-m",
            "rubaialter",
            inputFileCSV,
            "--xls",
            "--xlsx",
            "--sqlite3",
            "--tsv",
        ]
    )
    assert os.path.exists(outputFileXLS)
    assert os.path.exists(outputFileXLSX)
    assert os.path.exists(outputFileSQLITE3)
    assert os.path.exists(outputFileTSV)
    os.remove(outputFileXLS)
    os.remove(outputFileXLSX)
    os.remove(outputFileSQLITE3)
    os.remove(outputFileTSV)


# Cleanup ↓
def test_clean():
    shutil.rmtree("rubaialter")
