(function() {
  'use strict';

  angular
    .module('problem3.factory', [])
    .factory('problem3', problem3);

  problem3.$inject = ['prime'];
  function problem3(prime) {
    return {
      get: get
    };

    function get() {
      var timeStart = Date.now();
      var question = 600851475143;
      var value = Math.floor(Math.sqrt(question));
      if (value % 2 === 0) {
        value--;
      }
      while (value > 2) {
        if (question % value === 0) {
          if(prime.check(value)) {
            return {
              result: value,
              timer: Date.now() - timeStart
            };
          }
        }

        value -= 2;
      }
    }

  }
})();
