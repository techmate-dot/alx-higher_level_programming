#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const arr = list;
  const filtered = arr.filter(GetNum);

  function GetNum (element) {
    if (element === searchElement) {
      return element;
    }
  }
  return filtered.length;
};
