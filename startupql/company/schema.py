import graphene
from graphene_django import DjangoObjectType
from .models import link, Employ, city, title
from users.schema import UserType
from django.db.models import Q


class cityType(DjangoObjectType):
    class Meta:
        model = city


class titleType(DjangoObjectType):
    class Meta:
        model = title


class LinkType(DjangoObjectType):
    class Meta:
        model = link


class empType(DjangoObjectType):
    class Meta:
        model = Employ


# Query starts here//////////////////////////////////////


class Query(graphene.ObjectType):

    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return link.objects.all()

    searches = graphene.List(LinkType, search=graphene.String())

    def resolve_searches(self, info , search=None, **kwargs):
        if search:
            filter= (
            Q(url__icontains=search) | Q(description__icontains=search)
            )
            return link.objects.filter(filter)
        return link.objects.all()

    employs = graphene.List(empType)

    def resolve_employs(self, info, **kwargs):
        return Employ.objects.all()

    Ecity = graphene.List(cityType)

    def resolve_Ecity(self, info, **kwargs):
        return city.objects.all()

    titles = graphene.List(titleType)

    def resolve_titles(self, info, **kwargs):
        return title.objects.all()


# Mutation starts here /////////////////////////////////////////

class Createlink(graphene.Mutation):
    Link = graphene.Field(LinkType)
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, url, description):
        user = info.context.user or None
        Link = link(

            url=url,
            description=description,
            posted_by=user
        )
        Link.save()

        return Createlink(
            id=Link.id,
            url=Link.url,
            description=Link.description,
            posted_by=Link.posted_by
        )


# /////////////////////////////////////////////////////////////////

class CreateCity(graphene.Mutation):
    cities = graphene.Field(cityType)

    City = graphene.String()
    id = graphene.Int()

    class Arguments:
        City = graphene.String()
        id = graphene.Int()

    def mutate(self, info, City):
        cities = city(City=City)
        cities.save()

        return CreateCity(
            City=cities.City,
        )


# ////////////////////////////////////////////////////////////////////////////////

class UpdateLink(graphene.Mutation):
    update = graphene.Field(LinkType)

    class Arguments:
        id = graphene.Int(required=True)
        url = graphene.String()
        description = graphene.String()

    def mutate(self, info, id, url, description):
        user = info.context.user
        update = link.objects.get(id=id)

        if update.posted_by != user:
            raise Exception("Wrong user")

        update.url = url,
        update.description = description,
        update.save()

        return UpdateLink(update=update)


# //////////////////////////////////////////////////////////////////////////////////


class DeleteLink(graphene.Mutation):
    id = graphene.Int()

    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, id, description):
        user = info.context.user
        Link = link.objects.get(id=id)

        if Link.posted_by != user:
            raise Exception("wrong user")

        Link.delete()

        return DeleteLink(description=description)


# ///////////////////////////////////////////////////////////////////////////////


class Mutation(graphene.ObjectType):
    create_city = CreateCity.Field()
    create_link = Createlink.Field()
    update_link = UpdateLink.Field()
    delete_link = DeleteLink.Field()
