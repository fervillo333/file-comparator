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
class ComparisonManager:
    """Клас-менеджер для координації процесу."""
    
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2
        self.handler = FileHandler()

    def run(self):
        # 1. Зчитуємо дані
        set1 = self.handler.read_lines(self.file1)
        set2 = self.handler.read_lines(self.file2)
        
        # 2. Порівнюємо
        comparator = DataComparator(set1, set2)
        common = comparator.get_common()
        different = comparator.get_different()
        
        # 3. Записуємо результат
        self.handler.write_lines("same.txt", common)
        self.handler.write_lines("diff.txt", different)
        print(f"Done! Found {len(common)} common and {len(different)} unique lines.")