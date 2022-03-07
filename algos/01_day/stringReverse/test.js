var assert = require('assert');
const testFunc = require('./../reverseString').reverseString
const args = require('./../reverseString')



describe('Reverse String', function () {
  describe('', function () {
    it('should return true for "erutaerc" and "creature".', function () {
      assert.equal(testFunc(str1_arg), expected1);
    });
  });
  describe('', function () {
    it('should return true for "god" and "dog".', function () {
      assert.equal(testFunc(str2_arg), expected2);
    });
  });
});

const str1_arg = "creature";
const expected1 = "erutaerc";

const str2_arg = "dog";
const expected2 = "god";
// module.exports = { reverseString, str1_arg, str2_arg, expected1, expected2 };

