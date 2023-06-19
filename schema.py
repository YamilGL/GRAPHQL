from ariadne import QueryType, MutationType, make_executable_schema
from ariadne.objects import ObjectType
from ariadne.resolvers import GraphQLResolveInfo,Any

type_defs = """
    type Query{
        users: [User]
    }

    #type Mutation{
    

    #}

    type User
    {
        id: String
        name: String
        email: String
    }
"""

query = QueryType()
user = ObjectType("User")
 
@query.field("users")
async def resolve_users(parent: Any, info:GraphQLResolveInfo):
    return[
        {
         'id': '12345',
         'name': 'Usuario 1',
         'email': 'usuario1@test.com'
        }
        ]
schema = make_executable_schema(type_defs,[query, user])