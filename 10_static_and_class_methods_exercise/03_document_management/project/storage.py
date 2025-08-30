from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    @staticmethod
    def add_new_object(new, other):
        '''Adds an object if it does not exist'''
        if new not in other:
            other.append(new)

    @staticmethod
    def edit_find_id(obj_id: int, new_file_name: str, collection):
        categories = next((x for x in collection if x.id == obj_id), None)
        if categories:
            categories.name = new_file_name

    @staticmethod
    def edit_obj(obj_id: int, new_name, new_folder, collection):
        new_topic = next((x for x in collection if x.id == obj_id), None)
        if new_topic:
            new_topic.topic = new_name
            new_topic.storage_folder = new_folder

    @staticmethod
    def delete(file, collection):
        object_delete = next((obj for obj in collection if obj.id == file), None)
        if object_delete:
            collection.remove(object_delete)

    def add_category(self, category: Category):
        return self.add_new_object(category, self.categories)

    def add_topic(self, topic: Topic):
        return self.add_new_object(topic, self.topics)

    def add_document(self, documents: Document):
        self.add_new_object(documents, self.documents)

    def edit_category(self, category_id: int, new_name: str):
        self.edit_find_id(category_id, new_name, self.categories)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_fonder: str):
        self.edit_obj(topic_id, new_topic, new_storage_fonder ,self.topics)

    def edit_document(self, document_id: int, new_file_name: str):
        for document in self.documents:
            if document.id == document_id:
                document.file_name = new_file_name

    def delete_category(self, category_id):
        self.delete(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.delete(topic_id, self.topics)

    def delete_document(self, document_id):
        self.delete(document_id, self.documents)


    def get_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                return repr(d)

    def __repr__(self):
        return ''.join(str(d) for d in self.documents)

