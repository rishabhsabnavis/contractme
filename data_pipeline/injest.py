from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path: str) -> str:
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return docs


def load_txt(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.read()