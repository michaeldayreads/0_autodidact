// attempting to find the difference between exports and module.exports 
// https://stackoverflow.com/questions/7137397/module-exports-vs-exports-in-node-js#7142924

borked = (name) => {
  return{
    deeper: () => console.log(`it is borked ${name}!`)
  };
}

works = (name) => {
  return {
    deeper: () => console.log(`Looks like it works ${name}!`)
  };
}

exports.borked = borked;
module.exports.works = works;
