var testApp = angular.module('testApp', []);


testApp.controller('timeController', function($scope, $http){
    $scope.name = 'xyz';
    $scope.getTime = $http.get('/api/v1/server-time/')
        .then(function(response){
            $scope.timeSection = response.data.time;
        });
    $scope.refreshTimeButton = function(){
        console.log('Refresh time')
    };
    console.log($scope.name);
});

testApp.directive("myDirective", function() {
    return {
        template : "<h1>Made by a directive!!!</h1>"
    };
});
