import graphene
import images.schema

class Query(images.schema.Query, graphene.ObjectType):
    pass

class Mutation(images.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
