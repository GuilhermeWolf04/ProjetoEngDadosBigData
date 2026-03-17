import re
import sqlite3
from typing import Any, Dict, List


class Load:
    def _normalize_table_name(self, table_name: str) -> str:
        normalized = re.sub(r"\W+", "_", table_name.strip().lower()).strip("_")
        if not normalized:
            raise ValueError("O nome da tabela nao pode ser vazio.")
        return normalized

    def create_sqlite_table(
        self,
        universities_list: List[Dict[str, Any]],
        db_name: str,
        table_name: str,
    ) -> None:
        normalized_table = self._normalize_table_name(table_name)
        connection = sqlite3.connect(f"{db_name}.db")
        cursor = connection.cursor()

        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {normalized_table}
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                country TEXT,
                state_province TEXT,
                web_pages TEXT,
                domains TEXT
            );
            """
        )

        for university in universities_list:
            cursor.execute(
                f"""
                INSERT INTO {normalized_table}
                (name, country, state_province, web_pages, domains)
                VALUES (?, ?, ?, ?, ?);
                """,
                (
                    university.get("name"),
                    university.get("country"),
                    university.get("state-province"),
                    ", ".join(university.get("web_pages", [])),
                    ", ".join(university.get("domains", [])),
                ),
            )

        connection.commit()
        connection.close()
