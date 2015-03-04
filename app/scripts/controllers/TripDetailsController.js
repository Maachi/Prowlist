angular.module('prowlist')
  .controller('TripDetailsController',['$scope','$state','$ionicTabsDelegate', function($scope, $state, $ionicTabsDelegate) {
    $scope.$state = $state;
    $scope.userId = "default";

    
  }]);
