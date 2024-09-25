from typing import TYPE_CHECKING
from motormongo import Document, StringField, IntegerField, EmbeddedDocument, EmbeddedDocumentField, ReferenceField


class Work(EmbeddedDocument):
    position = StringField()
    organization = StringField()

class Address(EmbeddedDocument):
    street = StringField()
    city = StringField()


class User(Document):
    loggin = StringField(required=True, min_length=3, max_length=50)
    first_name = StringField(required=True, min_length=3, max_length=50)
    last_name = StringField(required=True, min_length=3, max_length=50)
    age = IntegerField(min_value=0, max_value=120)
    address = EmbeddedDocumentField(document_type=Address)
    work = EmbeddedDocumentField(document_type=Work)



class Permission(Document):
    name = StringField(required=True)
    user = ReferenceField(document=User)