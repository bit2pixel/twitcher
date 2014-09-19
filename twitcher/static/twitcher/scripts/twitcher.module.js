twitcher = angular.module('twitcher', ['ngResource', 'ngAnimate', 'ngSanitize']);

twitcher.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});