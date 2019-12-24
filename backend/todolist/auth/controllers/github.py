from flask import redirect, url_for
from flask_restful import Resource
from flask_dance.contrib.github import github

from ... import db

class GithubLogin(Resource):
    """ Login Controller """

    def get(self):
        if(not github.authorized):
            return redirect(url_for("github.login"))
        return "github login"
        