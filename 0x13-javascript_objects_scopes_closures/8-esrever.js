#!/usr/bin/node

exports.esrever = function (list) {
  const NewList = [];
  list.forEach(twist);

  function twist (element) {
    NewList.unshift(element);
  }
  return NewList;
};
