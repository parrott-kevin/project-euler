const solver = require('../problem-3')

describe('problem 3', () => {
  test('solve', () => {
    const result = solver(600851475143)
    const answer = 6857
    expect(result).toEqual(answer)
  })
})
