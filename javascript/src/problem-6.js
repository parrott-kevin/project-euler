const main = (limit) => {
  let sumSquares = 0
  let squareSum = 0
  for (let i = 1; i <= limit; i++) {
    sumSquares += i * i
    squareSum += i
  }
  return Math.abs(sumSquares - (squareSum ** 2))
}

module.exports = main
