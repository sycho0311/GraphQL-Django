import graphene
from graphene_django.types import DjangoObjectType

from .models import Dictionary


# model Type
class DictionaryType(DjangoObjectType):
    class Meta:
        model = Dictionary


# Input Data Type 설정
class DictionaryInput(graphene.InputObjectType):
    id = graphene.ID()
    word = graphene.String()
    definition = graphene.String()
    example = graphene.String()
    pos = graphene.String()


# Create
class CreateDictionary(graphene.Mutation):
    class Arguments:
        input = DictionaryInput(required=True)

    dictionary = graphene.Field(DictionaryType)

    def mutate(self, info, input=None):
        dictionary = Dictionary(word=input.word, definition=input.definition,
                                example=input.example, pos=input.pos)
        dictionary.save()

        return CreateDictionary(dictionary=dictionary)


# Update
class UpdateDictionary(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = DictionaryInput(required=True)

    # return Data, values...
    dictionary = graphene.Field(DictionaryType)

    def mutate(self, info, id, input=None):
        '''
        category_instance = Category.objects.get(pk=id)
        if category_instance:
            ok = True
            Category.objects.filter(pk=id).update(word=input.word)
            return UpdateCategory(ok=ok, category=category)
        return UpdateCategory(ok=ok, category=category)
        '''
        Dictionary.objects.filter(pk=id).update(word=input.word)
        dictionary = Dictionary.objects.get(pk=id)

        return UpdateDictionary(dictionary=dictionary)


# Delete
class DeleteDictionary(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    dictionary = graphene.Field(DictionaryType)

    def mutate(self, info, id):
        dictionary = Dictionary.objects.get(pk=id)
        dictionary.delete()

        return DeleteDictionary(dictionary=dictionary)


# Mutation
class Mutation(graphene.ObjectType):
    create_dictionary = CreateDictionary.Field()
    update_dictionary = UpdateDictionary.Field()
    delete_dictionary = DeleteDictionary.Field()


# Query
class Query(object):
    dictionary = graphene.Field(DictionaryType, id=graphene.Int(), word=graphene.String())
    all_dictionaries = graphene.List(DictionaryType)

    def resolve_all_dictionaries(self, context):
        return Dictionary.objects.all()

    def resolve_dictionary(self, context, id=None, word=None):
        if id is not None:
            return Dictionary.objects.get(pk=id)

        if word is not None:
            return Dictionary.objects.get(word=word)

        return None


# Query example
'''
query {
    allDictionaries {
        word
        definition
        example
        pos
    }
}

query {
    dictionary (word: "사과") {
        word
        definition
        example
    }
}
'''

# Mutation example
'''
mutation createDictionary {
  createDictionary(input: {
    word: "시험"
    definition: "재능이나 실력 따위를 일정한 절차에 따라 검사하고 평가하는 일"
    example: "시험에 합격하다"
    pos: "명사"
  }) {
    dictionary {
      id
      word
    }
  }
}

mutation updateDictionary {
  updateDictionary(id: 3, input: {
    word: "테스트"
  }) {
    dictionary {
      id
      word
    }
  }
}

mutation deleteDictionary {
  deleteDictionary(id: 3) {
    dictionary {
      word
    }
  }
}
'''
