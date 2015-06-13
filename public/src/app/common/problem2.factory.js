(function() {
  'use strict';

  angular
    .module('problem2.factory', [])
    .factory('problem2', problem2);

  function problem2() {
    return {
      get: get
    };

    function get() {
      var timeStart = Date.now();
      var result = 0;
      var previousValue = 1;
      var currentValue = 2;
      while (currentValue < 4000000) {
        if (currentValue % 2 === 0) {
          result += currentValue;
        }
        var tempValue = previousValue + currentValue;
        previousValue = currentValue;
        currentValue = tempValue;
      }

      return {
        result: result,
        timer: Date.now() - timeStart
      };
    }

  }
})();
