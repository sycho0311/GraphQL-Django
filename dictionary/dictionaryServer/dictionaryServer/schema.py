import dictionaryManager.schema

import graphene

from graphene_django.debug import DjangoDebug


class Query(
    dictionaryManager.schema.Query,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


class Mutation(
    dictionaryManager.schema.Mutation,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query, mutation=Mutation, types=[])
