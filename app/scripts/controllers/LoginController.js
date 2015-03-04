angular.module('prowlist')
  .controller('LoginController',['$scope','$state', function($scope, $state) {
    $scope.$state = $state;
    $scope.user = {};
    $scope.user.username = "user@gmail.com";
    $scope.user.password = "user@gmail.com";

    $scope.signIn = function(user){
      $state.go('stay');
    };
  }]);
