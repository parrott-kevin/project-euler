const prime = require('./prime')

const main = (input) => {
  let divisor = Math.floor(Math.sqrt(input)) + 1
  const primes = []
  let done = false
  while (!done) {
    if (input % divisor === 0 && prime.check(divisor)) {
      primes.push(divisor)
    }
    if (divisor === 2) {
      done = true
    } else {
      divisor -= 1
    }
  }

  return primes.sort((a, b) => a - b).pop()
}

module.exports = main
