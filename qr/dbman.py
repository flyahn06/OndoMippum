# +------------+--------------+-----------------------------------------------------------+
# |   Author   |     Date     |                         Changed                           |
# +------------+--------------+-----------------------------------------------------------+
# |  Andrew A. |  2022/09/28  | Initial release (basic db interaction)                    |
# +------------+--------------+-----------------------------------------------------------+
# |  Andrew A. |  2022/09/29  | Minor debug                                               |
# +------------+--------------+-----------------------------------------------------------+
# |  Andrew A. |  2022/09/29  | Wrote insert_data()                                       |
# +------------+--------------+-----------------------------------------------------------+

import sqlite3
import datetime

db = sqlite3.connect("../resources/main.db")
cur = db.cursor()


def find_name(code: int) -> str:
    """
    데이터베이스에서 학번을 검색해 이름을 돌려줍니다.
    :param code: 검색할 학번입니다.
    :return: 학생 이름을 돌려줍니다. 찾지 못하면 빈 문자열을 돌려줍니다.
    """

    if not code.isdigit():
        return ""

    res = cur.execute(f"SELECT * FROM students WHERE code={code}")
    data = res.fetchone()

    if data:
        return data[2]
    else:
        return ""


def insert_data(code: int, name: str, temp: float):
    print(f"INSERT INTO log(checktime, classcode, name, temp) VALUES (datetime(), {int(code)}, {name}, {temp})")
    cur.execute(f'INSERT INTO log(checktime, classcode, name, temp) VALUES ("{str(datetime.datetime.now()).split(".")[0]}", {int(code)}, "{name}", {temp})')
    db.commit()