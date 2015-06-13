(function() {
  'use strict';

  angular
    .module('app')
    .config(routeConfig);

  routeConfig.$inject = ['$routeProvider'];
  function routeConfig($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'app/components/problems/problems.html',
        controller: 'ProblemsController',
        controllerAs: 'vm'
      })
      .when('/home', {
        templateUrl: 'app/components/problems/problems.html',
        controller: 'ProblemsController',
        controllerAs: 'vm'
      })
      .otherwise({
        redirect: '/home'
      });
  }

})();
