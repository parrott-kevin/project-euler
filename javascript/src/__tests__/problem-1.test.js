const solver = require('../problem-1')

describe('problem 1', () => {
  test('solve', () => {
    const result = solver(3, 0, 1000)
    const answer = 233168
    expect(result).toEqual(answer)
  })
})
