import graphene
from .query import QueryRoot

schema = graphene.Schema(query=QueryRoot)