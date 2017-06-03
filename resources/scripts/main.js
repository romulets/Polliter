/**
 * Created by romulo-farias on 01/06/17.
 */

'use strict';

var app = angular.module('Polliter', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

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
	}

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
	}

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
	  }

	getPoliticians()
});