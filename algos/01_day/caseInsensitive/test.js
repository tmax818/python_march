var assert = require('assert');
const testFunc = require('./caseInsensitiveStringCompare').caseInsensitiveStringCompare

describe('Case Insensitive String', function () {
  describe('', function () {
    it('should return true for "ABC" and "abc".', function () {
      assert.equal(testFunc("ABC", "abc"), true);
    });
  });

  describe('', function () {
    it('should return false for "ABC" and "abd".', function () {
      assert.equal(testFunc("ABC", "abd"), false);
    });
  });

  describe('', function () {
    it('should return false for "ABC" and "bc".', function () {
      assert.equal(testFunc("ABC", "bc"), false);
    });
  });
});

