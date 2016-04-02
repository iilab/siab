
var extname = require('path').extname;
var yaml = require('js-yaml');
var Papa = require('papaparse');

/**
 * Expose `plugin`.
 */

module.exports = plugin;

/**
 * Supported metadata parsers.
 */

var parsers = {
  '.csv': Papa.parse,
  '.json': JSON.parse,
  '.yaml': yaml.safeLoad,
  '.yml': yaml.safeLoad
};

function slugify(text)
{
  return text.toString().toLowerCase()
    .replace(/\s+/g, '-')           // Replace spaces with -
    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
    .replace(/\-\-+/g, '-')         // Replace multiple - with single -
    .replace(/^-+/, '')             // Trim - from start of text
    .replace(/-+$/, '');            // Trim - from end of text
}

function keyify(text)
{
  return text.toString().toLowerCase()
    .replace(/\s+/g, '_')           // Replace spaces with -
    .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
    .replace(/\-\-+/g, '_')         // Replace multiple - with single -
    .replace(/\-/g, '_')         // Replace multiple - with single -
    .replace(/^-+/, '')             // Trim - from start of text
    .replace(/-+$/, '');            // Trim - from end of text
}

hashCode = function(s){
  return s.split("").reduce(function(a,b){a=((a<<5)-a)+b.charCodeAt(0);return a&a},0);              
}

/**
 * Metalsmith plugin to load metafiles in various formats.
 *
 * @param {Object} opts
 * @return {Function}
 */

function plugin(opts){
  opts = opts || {};

  return function(files, metalsmith, done){
    var metadata = metalsmith.metadata();
    var exts = Object.keys(parsers);

    for (var key in opts) {
      var file = opts[key];
      var ext = extname(file);
      if (!~exts.indexOf(ext)) throw new Error('unsupported metadata type "' + ext + '"');
      if (!metadata[key] || files[file]) {
        if (!files[file]) throw new Error('file "' + file + '" not found');

        var parse = parsers[ext];
        var str = files[file].contents.toString();
        delete files[file];

        try {
          if (ext == ".csv") {
            var data = parse(str, {header: true}).data;
            data.forEach(function(item) {
              Object.keys(item).forEach(function(k,v) {
                if (k !== keyify(k)) {
                  Object.defineProperty(item, keyify(k),
                      Object.getOwnPropertyDescriptor(item, k));
                  delete item[k];
                } 
              })
              if (item.id == undefined) {
                item.id = ( item['name'] != undefined ) ? slugify(item['name']) : hashCode(item.toString())
              }
            })
          } else {
            var data = parse(str);
          }
        } catch (e) {
          return done(new Error('malformed data in "' + file + '"'));
        }

        metadata[key] = data;
      }
    }

    done();
  };
}
