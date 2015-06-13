(function() {
  'use strict';

  angular
    .module('prime.factory', [])
    .factory('prime', prime);

  function prime() {
    return {
      check: check
    };

    function check(value) {
      for (var i = 2; i <= Math.floor(Math.sqrt(value)); i++) {
        if (value % i === 0) {
          return false;
        }
      }
      return true;
    }

  }
})();
