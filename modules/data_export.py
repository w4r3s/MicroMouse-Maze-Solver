# modules/data_export.py

import csv

class DataExporter:
    def export_results(self, results, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Algorithm', 'Time', 'Path Length']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for alg, data in results.items():
                writer.writerow({
                    'Algorithm': alg,
                    'Time': data['time'],
                    'Path Length': data['length']
                })
