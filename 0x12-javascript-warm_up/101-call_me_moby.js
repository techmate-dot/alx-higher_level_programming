#!/usr/bin/node

exports.callMeMoby = function (time, func) {
  let i = 0;
  while (i < time) {
    func();
    i++;
  }
};
