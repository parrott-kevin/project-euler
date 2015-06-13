(function() {
  'use strict';

  angular
    .module('problems.controller', [])
    .controller('ProblemsController', ProblemsController);

  ProblemsController.$inject = ['problem1', 'problem2', 'problem3'];
  function ProblemsController(problem1, problem2, problem3) {
    var vm = this;
    var p1 = problem1.get();
    var p2 = problem2.get();
    var p3 = problem3.get();
    vm.problems = [
      {
        number: '1',
        title: 'Multiples of 3 and 5',
        answer: p1.result,
        timer: p1.timer
      },
      {
        number: '2',
        title: 'Even Fibonacci numbers',
        answer: p2.result,
        timer: p2.timer
      },
      {
        number: '3',
        title: 'Largest prime factor',
        answer: p3.result,
        timer: p3.timer
      }

    ];

  }
})();
