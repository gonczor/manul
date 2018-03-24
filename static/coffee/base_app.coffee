testApp = angular.module('testApp', [])


testApp.controller('timeController', ($scope, $http) ->
    $scope.name = 'xyz'
    $scope.getTime = $http.get('/api/v1/server-time/')
        .then((response) ->
            $scope.timeSection = response.data.time
        )
    $scope.refreshTimeButton = ->
        console.log('Refresh time.')

    console.log($scope.name)
)
