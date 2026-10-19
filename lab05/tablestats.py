def read_rows(lines):
    header = None
    rows = []
    for line in lines:
        cleaned_line = line.strip()
        if not cleaned_line:
            continue
        fields = [field.strip() for field in cleaned_line.split(',')]
        if header is None:
            header = fields
            continue
        if len(fields) != len(header):
            continue
        row_dict = {header[i]: fields[i] for i in range(len(header))}
        rows.append(row_dict)
    return rows

def count_types(rows):
    counts = {}
    for row in rows:
        kind = row.get("тип")
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows, kind):
    total = 0.0
    has_kind = False
    for row in rows:
        if row.get("тип") == kind:
            has_kind = True
            minutes_str = row.get("минуты", "").replace(",", ".")
            try:
                total += float(minutes_str)
            except ValueError:
                continue
    if not has_kind:
        return 0.0
    return round(total, 1)

def to_csv(counts):
    result = ["тип,количество"]
    for kind in sorted(counts.keys()):
        result.append(f"{kind},{counts[kind]}")
    return "\n".join(result) + "\n"