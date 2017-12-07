const solver = require('../problem-2')

describe('problem 2', () => {
  test('solve', () => {
    const result = solver(1, 2, 0, 4000000)
    const answer = 4613732
    expect(result).toEqual(answer)
  })
})
