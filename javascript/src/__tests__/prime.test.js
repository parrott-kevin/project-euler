const prime = require('../prime')

describe('prime number utilities', () => {
  describe('check', () => {
    test('is prime', () => {
      const result = prime.check(29)
      expect(result).toBeTruthy()
    })

    test('is prime', () => {
      const result = prime.check(32)
      expect(result).toBeFalsy()
    })
  })
})
