/**
 * Created by romulo-farias on 01/06/17.
 */

'use strict';

var app = angular.module('Polliter', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

app.config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.controller('PrivateTopicsController', function($scope, $http) {
	$scope.topics = [];
	var page = 1;

  var getClients = function () {
    $http.get('/topics?json=1&page=' + page).then(function(response) {
      $scope.topics = response.data;
      page++;
    }, function(err){
      console.error(err);
      });
	};

	getClients();
});

app.controller('PublicTopicsController', function($scope, $http) {
	$scope.topics = [];
	var page = 1;

  var getClients = function () {
    $http.get('/topics/all?json=1&page=' + page).then(function(response) {
      $scope.topics = response.data;
      page++;
    }, function(err){
      console.error(err);
      });
	};

	getClients();
});

app.controller('PoliticiansController', function($scope, $http) {
	$scope.politicians = [];

  var getPoliticians = function () {
    $http.get('/politicians/list?json=1').then(function(response) {
      $scope.politicians = response.data;
    }, function(err){
       console.error(err);
    });
  };

  $scope.follow = function follow(politician, token) {
    $http.post('/politicians/follow/' + politician.id +'/?json=1').then(function(response) {
      politician.following = response.data.following;
    }, function(err){
       console.error(err);
    });
  };

  $scope.unfollow = function unfollow(politician) {
    $http.delete('/politicians/unfollow/' + politician.id +'/?json=1').then(function(response) {
      politician.following = response.data.following;
    }, function(err){
       console.error(err);
    });
  };

	getPoliticians()
});

app.controller('ThemesController', function($scope, $http) {
	$scope.themes = [];

  var getThemes = function () {
    $http.get('/themes/list?json=1').then(function(response) {
      $scope.themes = response.data;
    }, function(err){
       console.error(err);
    });
  };

  $scope.follow = function follow(theme, token) {
    $http.post('/themes/follow/' + theme.id +'/?json=1').then(function(response) {
      theme.following = response.data.following;
    }, function(err){
       console.error(err);
    });
  };

  $scope.unfollow = function unfollow(theme) {
    $http.delete('/themes/unfollow/' + theme.id +'/?json=1').then(function(response) {
      theme.following = response.data.following;
    }, function(err){
       console.error(err);
    });
  };

	getThemes()
});