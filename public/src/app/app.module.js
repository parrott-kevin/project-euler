(function() {
  'use strict';

  angular
    .module('app', [
      'ngRoute',
      'problems.controller',
      'problem1.factory',
      'problem2.factory',
      'problem3.factory',
      'prime.factory'
    ]);
})();
