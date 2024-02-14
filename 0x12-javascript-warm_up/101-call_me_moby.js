#!/usr/bin/node

exports.callMeMoby = function (loop, func) {
  for (let i = 0; i < loop; i++) {
    func();
  }
};
