(function() {
  'use strict';

  angular
    .module('problems.controller', [])
    .controller('ProblemsController', ProblemsController);

  ProblemsController.$inject = ['problem1', 'problem2', 'problem3'];
  function ProblemsController(problem1, problem2, problem3) {
    var vm = this;
    var problem1 = problem1.get();
    var problem2 = problem2.get();
    var problem3 = problem3.get();
    vm.problems = [
      {
        number: '1',
        title: 'Multiples of 3 and 5',
        answer: problem1.result,
        timer: problem1.timer
      },
      {
        number: '2',
        title: 'Even Fibonacci numbers',
        answer: problem2.result,
        timer: problem2.timer
      },
      {
        number: '3',
        title: 'Largest prime factor',
        answer: problem3.result,
        timer: problem3.timer
      }

    ];

  }
})();
