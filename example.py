import json
import graphene
import os

"""
    {
        name:"sumit",
        language: "python"
    }
"""


class Query(graphene.ObjectType):
    name = graphene.String()
    language = graphene.String()

    def resolve_name(self, info):
        return "Sumit"

    def resolve_language(self, info):
        return "Python"


schema = graphene.Schema(query=Query)
print(schema)

# ===========================Graph QL

grpah_ql = '''
query myquery{
    language
}
'''

result = schema.execute(grpah_ql)
print(result.data)