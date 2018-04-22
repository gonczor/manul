loginApp = angular.module('loginApp', [])

loginApp.controller 'loginController',
class LoginController
    constructor: (@$scope, @$http, @$window) ->
        _scope = @$scope
        _http = @$http
        _window = @$window

        @$scope.submitLoginForm = () ->
            debugger
            data =
                'username': _scope.username
                'password': _scope.password
            headers =
                'Content-Type': 'application/json'
            console.log(apiLoginUrl)
            console.log(data)
            console.log(headers)
            _http.post(
                apiLoginUrl,
                data
                headers
            )
                .then(
                    (response) ->
                        console.log(response)
                        _window.sessionStorage.setItem('token', response.data.token)
                    (response) -> console.log(response)
            )

LoginController.$inject = ['$scope', '$http', '$window']
