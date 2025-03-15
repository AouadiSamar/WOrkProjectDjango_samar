import graphene
from graphene_django.types import DjangoObjectType
from .models import UploadedImage  # Ensure you import the correct model

# GraphQL Type for Images
class ImageType(DjangoObjectType):
    class Meta:
        model = UploadedImage  # Ensure it matches your model

# Query to retrieve all images
class Query(graphene.ObjectType):
    all_images = graphene.List(ImageType)

    def resolve_all_images(self, info):
        return UploadedImage.objects.all()

# Mutation to upload an image
class UploadImage(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        image = graphene.String(required=True)

    image = graphene.Field(ImageType)

    def mutate(self, info, title, image):
        img = UploadedImage(title=title, image=image)
        img.save()
        return UploadImage(image=img)

# Mutation to delete an image
class DeleteImage(graphene.Mutation):
    class Arguments:
        image_id = graphene.ID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, image_id):
        image = UploadedImage.objects.get(id=image_id)
        image.delete()
        return DeleteImage(success=True)
class UpdateImage(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        description = graphene.String()

    success = graphene.Boolean()  # Champ ajouté
    image = graphene.Field(ImageType)

    def mutate(self, info, id, title=None, description=None):
        img = UploadedImage.objects.get(id=id)
        if title:
            img.title = title
        if description:
            img.description = description
        img.save()
        return UpdateImage(success=True, image=img)  # Retourne success=True

# Mutation class
class Mutation(graphene.ObjectType):
    upload_image = UploadImage.Field()
    delete_image = DeleteImage.Field()
    update_image = UpdateImage.Field()

# Define the GraphQL Schema
schema = graphene.Schema(query=Query, mutation=Mutation)
