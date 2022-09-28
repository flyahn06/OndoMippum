import sqlite3

# db = sqlite3.connect("/Volumes/GoogleDrive/내 드라이브/온도미쁨 배움의 숲 프로젝트/src/db/main.db")
db = sqlite3.connect("../db/main.db")
cur = db.cursor()


def find_name(code: int) -> str:
    """
    데이터베이스에서 학번을 검색해 이름을 돌려줍니다.
    :param code: 검색할 학번입니다.
    :return: 학생 이름을 돌려줍니다. 찾지 못하면 빈 문자열을 돌려줍니다.
    """
    res = cur.execute(f"SELECT * FROM students WHERE code={code}")

    return res.fetchone()[2]