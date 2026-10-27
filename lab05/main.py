import tablestats

def main():
    file_name = input().strip()

    try:
        with open(file_name, encoding="utf-8") as table:
            rows = tablestats.read_rows(table)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден. Проверьте, что он лежит в той же папке, что и скрипт, и правильно введено имя.")
        return
    except UnicodeDecodeError:
        print(f"Не удалось прочитать файл '{file_name}' в кодировке UTF-8. Проверьте кодировку файла.")
        return

    counts = tablestats.count_types(rows)
    unique_types_count = len(counts)
    error_minutes = tablestats.total_minutes(rows, "ошибка")

    print(len(rows))
    print(unique_types_count)
    print(error_minutes)

    summary_csv = tablestats.to_csv(counts)
    with open("summary.csv", "w", encoding="utf-8") as out:
        out.write(summary_csv)

if __name__ == "__main__":
    main()
