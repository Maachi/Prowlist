angular.module('prowlist')
  .controller('CitySearchController',['$scope','$state', function($scope, $state) {
    $scope.$state = $state;
    $scope.userId = "default";
    $scope.searchData = {};
    $scope.searchData.results = ['San Francisco','Boston','New York'];


    //-----------------------------------------------------

    $scope.search = function() {
      //api.getCallSearch($scope.userId, $scope.searchData.searchText,undefined, displaySearchResults);
      $scope.searchData.results = ['San Francisco','Boston','New York'];
    };

    //-----------------------------------------------------
    function displaySearchResults(data) {
      $scope.searchData.results = data;
      //$scope.$apply();
    }

  }]);
