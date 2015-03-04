angular.module('prowlist')
  .controller('StayController',['$scope','$state', function($scope, $state) {
    $scope.$state = $state;
    $scope.userId = "default";
    //-----------------------------------------------------

    $scope.createStay = function() {
      $state.go('products');
    };

    //-----------------------------------------------------


  }]);