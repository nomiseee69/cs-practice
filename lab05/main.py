import tablestats

def main():
    file_name = input().strip()
    
    with open(file_name, encoding="utf-8") as table:
        rows = tablestats.read_rows(table)
        
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
