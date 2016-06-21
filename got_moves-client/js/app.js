var app = angular.module('gotMoves', [])

    .factory('categoryService', ["$http", function($http){

        var doRequest = function(){
            return $http({
                method: "JSONP",
                url: "http://127.0.0.1:8000/api/categories/"
            });
        }
        return {
            categories: function() { return doRequest(); },
        };
    }]);

app.controller("MovesController", function($scope, categoryService){
    $scope.categories;

    getCategories();

    function getCategories(){
            categoryService.categories()
                .success(function(cates){
                    $scope.categories = cates
                })
    }

});
