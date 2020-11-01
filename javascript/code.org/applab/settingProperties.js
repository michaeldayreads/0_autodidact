function setAttributes(spec) {
    for (var item in spec) {
        for(var key in spec[item]) {
        var prop = spec[item][key];
        setProperty(item, key, prop);
        }
    }
}

var spec = {
    "label1": {
      "text": "Welcome to my app!"
    },
    "button1": {
      "background-color": "red",
      "text": "Red"
    },
    "button2":
      {
      "background-color": "blue",
      "text": "Blue"
      }
 };

setAttributes(spec);