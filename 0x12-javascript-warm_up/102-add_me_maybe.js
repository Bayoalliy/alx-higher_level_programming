#!/usr/bin/node

exports.addMeMaybe = function (n, func) {
  nb = n + 1;
  func(nb);
};
