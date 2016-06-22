var app = angular.module('gotMoves', [])

app.factory("CateFactory", [
    "$http",
    function ($http){
        return $http.get("http://127.0.0.1:8000/api/categories/?format=json")
    }
])

app.controller("cateController", ["$scope", "CateFactory", function($scope, CateFactory){
    $scope.categories = null;
    CateFactory.then(function(response){
        $scope.categories = response;
    });
}])


app.factory("ClassicMoveFactory", [
    "$http",
    function ($http){
        return $http.get("http://127.0.0.1:8000/api/classic_moves/?format=json")
    }
])

app.controller("classicMoveController", [
    "$scope",
    "ClassicMoveFactory",
    function($scope, ClassicMoveFactory){
        $scope.classic_moves = null;
        ClassicMoveFactory.then(function(response){
            $scope.classic_moves = response.data;
    });
}])
