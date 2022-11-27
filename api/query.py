import graphene
from graphene_django import DjangoObjectType

from .objects.ingredients import CategoryType, IngredientType
from ..cookbook.ingredients.models import Category, Ingredient

class QueryRoot(graphene.ObjectType):
    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(root, info):
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.objects.get(name=name):
            return None
