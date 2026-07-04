import fitz

class PDFService:
    def extract_text(self,path:str) -> str:

        if not path.exists():
            raise FileNotFoundError(path)

        pages = []
        with fitz.open(path) as document:
            for index,page in enumerate(document):
                text = page.get_text("text").strip()

                if not text:
                    continue
                
                pages.append({
                    "page":index+1,
                    "text":text
                })
        return pages
