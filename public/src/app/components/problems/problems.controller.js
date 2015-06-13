(function() {
  'use strict';

  angular
    .module('problems.controller', [])
    .controller('ProblemsController', ProblemsController);

  ProblemsController.$inject = ['problem1', 'problem2', 'problem3'];
  function ProblemsController(problem1, problem2, problem3) {
    var vm = this;

    vm.problems = [
      problem1.get(),
      problem2.get(),
      problem3.get()
    ];
  }
})();
