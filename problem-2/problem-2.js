'use strict'

function fibonacci (a, b, answer, maxNum) {
  if (b >= maxNum) {
    return answer
  }
  const check = val => val % 2 === 0
  const bCheck = check(b) ? b : 0
  return fibonacci(b, a + b, answer + bCheck, maxNum)
}
const result = fibonacci(1, 2, 0, 4000000)
console.log(result)
