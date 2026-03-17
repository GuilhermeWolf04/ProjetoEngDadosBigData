from src import Extract, Load


def salvar_universidades_por_pais(country: str, db_name: str = "universities") -> None:
    extract = Extract()
    load = Load()

    universities = extract.extract_country(country)
    load.create_sqlite_table(universities, db_name, country)

    print(
        f"Foram inseridos {len(universities)} registros na tabela '{country}' "
        f"do banco '{db_name}.db'."
    )


if __name__ == "__main__":
    salvar_universidades_por_pais("Brazil")
