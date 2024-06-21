#!/usr/bin/node

exports.addMeMaybe = function (n, func) {
  n = n + 1;
  func(n);
};
