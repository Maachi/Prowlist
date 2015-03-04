angular.module('prowlist')
  .controller('HomeController', ['$scope','$state', '$ionicPopup', function($scope, $state, $ionicPopup) {
    $scope.$state = $state;
    $scope.userId = "default";
    

    $scope.gotoTrip = function(){
      $state.go('tripDetails');
    };

    $scope.newTrip = function(){
      //$state.go('callDetails');
    };


    //--------------------------------------------------------------

    

  }]);
