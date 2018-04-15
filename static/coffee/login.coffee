loginApp = angular.module('loginApp', [])

loginApp.controller 'loginController',
class LoginController
    constructor: (@$scope, @$http) ->
        _scope = @$scope
        _http = @$http
        @$scope.submitLoginForm = () ->
            debugger
            data =
                'username': _scope.username
                'password': _scope.password
            console.log(apiLoginUrl)
            console.log(data)
            _http.post(apiLoginUrl, data)
                .then(
                    (response) -> console.log(response),
                    (response) -> console.log(response)
            )

LoginController.$inject = ['$scope', '$http']
