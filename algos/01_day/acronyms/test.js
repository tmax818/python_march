var assert = require('assert');
const file = require('./acronymize')



describe('Day 01', function () {
  describe('acronymize', function () {
    it('should return true for "ABC" and "abc".', function () {
      assert.equal(testFunc("ABC", "abc"), true);
    });
  });
});


describe('Case Insensitive String', function () {
  describe('', function () {
    it('should return false for "ABC" and "abd".', function () {
      assert.equal(testFunc("ABC", "abd"), false);
    });
  });
});


describe('Case Insensitive String', function () {
  describe('', function () {
    it('should return false for "ABC" and "bc".', function () {
      assert.equal(testFunc("ABC", "bc"), false);
    });
  });
});

