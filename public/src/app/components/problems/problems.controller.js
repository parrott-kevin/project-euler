(function() {
  'use strict';

  angular
    .module('problems.controller', [])
    .controller('ProblemsController', ProblemsController);

  ProblemsController.$inject = ['problem1'];
  function ProblemsController(problem1) {
    var vm = this;
    vm.problems = [
      {
        title: 'Problem 1',
        answer: problem1.get()
      }
    ];

  }
})();
