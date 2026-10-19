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

