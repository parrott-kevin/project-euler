(function() {
  'use strict';

  angular
    .module('problem1.factory', [])
    .factory('problem1', problem1);

  function problem1() {
    return {
      get: get
    };

    function get() {
      var problem = {
        number: '1',
        title: 'Multiples of 3 and 5'
      };

      var timeStart = Date.now();
      var result = 0;
      for (var i = 3; i < 1000; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
          result += i;
        }
      }

      problem.answer = result;
      problem.timer = Date.now() - timeStart;
      return problem;
    }

  }
})();
