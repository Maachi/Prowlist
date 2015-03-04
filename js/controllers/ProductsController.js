angular.module('ConvAssist')
  .controller('ProductsController',['$scope','$state', function($scope, $state) {
    $scope.$state = $state;
    $scope.userId = "default";
    //-----------------------------------------------------

    $scope.createStay = function() {
      $state.go('products');
    };

    //-----------------------------------------------------


  }]);