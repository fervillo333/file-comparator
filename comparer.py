import os

class FileHandler:
    """Клас для читання та запису файлів."""
    
    @staticmethod
    def read_lines(filepath):
        """Зчитує унікальні рядки з файлу."""
        if not os.path.exists(filepath):
            return set()
        with open(filepath, 'r', encoding='utf-8') as f:
            # Використовуємо set comprehension для очищення від пробілів
            return {line.strip() for line in f if line.strip()}

    @staticmethod
    def write_lines(filepath, lines):
        """Записує список рядків у файл."""
        with open(filepath, 'w', encoding='utf-8') as f:
            for line in sorted(lines):
                f.write(f"{line}\n")
class DataComparator:
    
    def __init__(self, data1, data2):
        self.data1 = set(data1)
        self.data2 = set(data2)

    def get_common(self):
        """Повертає спільні рядки (перетин)."""
        return self.data1.intersection(self.data2)

    def get_different(self):
        """Повертає рядки, що не повторюються (симетрична різниця)."""
        return self.data1.symmetric_difference(self.data2)