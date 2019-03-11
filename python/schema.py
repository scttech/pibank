import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Customer as CustomerModel

class Customer(SQLAlchemyObjectType):
    class Meta:
        model = CustomerModel
        interfaces = (relay.Node, )

class CustomerConnection(relay.Connection):
    class Meta:
        node = Customer

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_customers = SQLAlchemyConnectionField(CustomerConnection)

schema = graphene.Schema(query=Query)

