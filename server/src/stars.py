from flask import request, Blueprint

blueprint = Blueprint('stars', __name__, url_prefix='/stars') 

@blueprint.route('/count', methods=['GET'])
def count():
    """
    ---
    get:
        summary: Determine how many stars any given list of github repositories has received.
        description: Given a list of gigithub repositories in the form organization/repository, 
        the method will return the number of stars each repo has received, as well as a 
        cumulative value for all repos.
        requestBody:
            content:
                application/json:
                    schema: RequestSchema
        responses:
            200: 
                description: a successfull star count was returned
                content:
                    application/json:
                        starsCount: A map containing the number of stars for each repo.
                        totaalStars: An integer representing the sum of stars on all repos.
            400:
                description: invalid input provided to the api endpoint
            500: 
                description: unspecified server error
    """

    payload = request.get_json()
    print(f'PAYLOAD: {payload}')
    return "Future json body"
    



