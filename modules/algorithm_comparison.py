# modules/algorithm_comparison.py

class AlgorithmComparison:
    def __init__(self, algorithms):
        self.algorithms = algorithms  # 字典，键为算法名称，值为算法函数

    def compare(self, maze, start, end, step):
        results = {}
        for name, algorithm in self.algorithms.items():
            start_time = time.time()
            path = algorithm(maze, start, end, step)
            end_time = time.time()
            results[name] = {
                'path': path,
                'time': end_time - start_time,
                'length': len(path) if path else float('inf')
            }
        return results
