from api import app, db
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import listProducts_resolver, getProduct_resolver
from api.mutations import create_product_resolver, update_product_resolver, delete_product_resolver

query = ObjectType("Query")
mutation = ObjectType("Mutation")
query.set_field("listProducts", listProducts_resolver)
query.set_field("getProduct", getProduct_resolver)
mutation.set_field("createProduct", create_product_resolver)
mutation.set_field("updateProduct", update_product_resolver)
mutation.set_field("deleteProduct", delete_product_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code