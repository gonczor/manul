loginApp = angular.module('loginApp', [])

loginApp.controller 'loginController',
class LoginController
    constructor: (@scope, @http) ->
        console.log(login_url)
        @scope.something = () -> 'Hello, world'
