// poc of random page selection
// to assist nephew on project

var pages = ["salary", "fans", "season"];

function useRandomPage(pageArray) {
  var seed = Math.random();
  var targetIndex = Math.floor(seed * pageArray.length);
  var nextPage = pageArray[targetIndex];
  console.log("We would jump to:", nextPage);
  pageArray.splice(targetIndex, 1);
  return pageArray;
}

while (pages.length > 0) {
  console.log("Pages at start:", pages);
  pages = useRandomPage(pages);
  console.log("Pages left:", pages);
  console.log("-----");
}
