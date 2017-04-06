'use strict'

function threeFive (num, answer, lastNum) {
  if (num >= lastNum) {
    return answer
  }
  const check = (() => num % 3 === 0 || num % 5 === 0)()
  if (check) {
    return threeFive(num + 1, answer + num, lastNum)
  }
  return threeFive(num + 1, answer, lastNum)
}

console.log(threeFive(3, 0, 1000))
