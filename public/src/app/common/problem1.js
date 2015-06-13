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
      var sum = 0;
      for (var i = 3; i < 1000; i++) {
        if (i % 3 === 0 || i % 5 === 0) {
          sum++;
        }
      }

      return sum;
    }

  }
})();
