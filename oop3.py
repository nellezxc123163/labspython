class PDFDocument:
    def open(self):
        print('Открываю PDF-документ')

class WordDocument:
    def open(self):
        print('Открываю Word-документ')

class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        if doc_type == 'pdf':
            return PDFDocument()
        elif doc_type == 'word':
            return WordDocument()
        else:
            raise ValueError('Неизвестный тип документа')

