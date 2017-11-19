import csv

def fix_turnstile_data(filenames):
    for name in filenames:
        with open(name, 'rb') as f:
            reader = csv.reader(f)
            all_rows = list()
            for row in reader:
                minus_first3 = row[3:]
                for i, j, k, l, m in zip(minus_first3[::5],minus_first3[1::5],minus_first3[2::5],minus_first3[3::5],minus_first3[4::5]):
                    new_row = row[:3] + [i, j, k, l, m]
                    all_rows.append(new_row)
            updated = 'updated_' + name
            with open(updated, 'wb') as ff:
                writer = csv.writer(ff)
                writer.writerows(all_rows)               
