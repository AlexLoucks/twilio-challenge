import re
from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validates
)


class StarCountRequestSchema(Schema):
    """
        Schema class representing the expected format of our payload to our api endpoint.
    """
    repositoryList = fields.List(fields.String(), required=True)

    @validates('repositoryList')
    def validate_length(self, data):
        if len(data) < 1:
            raise ValidationError('Repository list must have at least one item')
        
        repo_pattern = '^[a-zA-Z0-9-]+/[a-zA-Z0-9-]+$'
        for repo in data:
            if not re.search(repo_pattern, repo):
                raise ValidationError(f'The repo named {repo} does not match the expected pattern ogranziation/repository')


       

