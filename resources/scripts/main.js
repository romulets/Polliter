/**
 * Created by romulo-farias on 01/06/17.
 */

'use strict';

var app = angular.module('Polliter', []);

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('[[');
  $interpolateProvider.endSymbol(']]');
});

app.controller('TopicsController', function($scope, $http) {
	$scope.topics = [];
	var page = 1;

    var getClients = function () {
		$http.get('/topics?json=1&page=' + page).then(function(response) {
			$scope.topics = response.data;
			console.log($scope.topics)
			page++;
		}, function(err){
		    console.error(err);
        });
	}

	getClients();
});