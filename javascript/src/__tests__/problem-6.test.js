const solver = require('../problem-6')

describe('problem 6', () => {
  test('example', () => {
    const result = solver(10)
    const answer = 2640
    expect(result).toEqual(answer)
  })
  test('solve', () => {
    const result = solver(100)
    const answer = 25164150
    expect(result).toEqual(answer)
  })
})
