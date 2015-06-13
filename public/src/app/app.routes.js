(function() {
  'use strict';

  angular
    .module('app')
    .config(routeConfig);

  routeConfig.$inject = ['$routeProvider'];
  function routeConfig($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'app/components/problem/problem.html',
        controller: 'ProblemController',
        controllerAs: 'vm'
      })
      .when('/home', {
        templateUrl: 'app/components/problem/problem.html',
        controller: 'ProblemController',
        controllerAs: 'vm'
      })
      .otherwise({
        redirect: '/home'
      });
  }

})();
