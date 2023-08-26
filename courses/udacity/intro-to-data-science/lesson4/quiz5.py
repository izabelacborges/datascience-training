import csv

def fix_turnstile_data(filenames):
    for name in filenames:
        with open(name, 'rb') as f:
            reader = csv.reader(f)
            all_rows = []
            for row in reader:
                minus_first3 = row[3:]
                all_rows.extend(
                    row[:3] + [i, j, k, l, m]
                    for i, j, k, l, m in zip(
                        minus_first3[::5],
                        minus_first3[1::5],
                        minus_first3[2::5],
                        minus_first3[3::5],
                        minus_first3[4::5],
                    )
                )
            updated = f'updated_{name}'
            with open(updated, 'wb') as ff:
                writer = csv.writer(ff)
                writer.writerows(all_rows)               
