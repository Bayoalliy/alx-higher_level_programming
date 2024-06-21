#!/usr/bin/node

exports.callMeMoby = function (n, func) {
  for (; n > 0; n--) {
    func();
  }
};
