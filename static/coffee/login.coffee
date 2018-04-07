loginApp = angular.module('loginApp', [])

loginApp.controller 'loginController',
class LoginController
    constructor: (@scope, @http) ->
        @scope.something = () -> 'Hello, world'
