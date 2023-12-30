from sonnets import Sonnet
from sonnets import Document


class Query(Document):
    def __init__(self, query: str):
        super().__init__([query])


class Index(dict[str, set[int]]):
    def __init__(self, documents: list[Sonnet]):
        super().__init__()
        self.documents = documents
        for document in documents:
            self.add(document)

    def add(self, document: Sonnet):
        doc_id = document.id
        tokens = document.tokenize()

        for token in tokens:
            if token not in self:
                self[token] = set()
            self[token].add(doc_id)

    def search(self, query: Query) -> list[Sonnet]:
        tokenized_query = Document.tokenize(query)
        ids_per_token = {}
        for token in tokenized_query:
            # check if search term in index
            if token in self:
                ids_per_token[token] = set(self[token])
            # return empty list if one of search terms not in index
            else:
                return []

        result_ids = set.intersection(*ids_per_token.values())
        result_sonnets = [sonnet for sonnet in self.documents if sonnet.id in result_ids]
        return result_sonnets
