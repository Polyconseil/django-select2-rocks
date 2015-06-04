;(function ($, window, document, undefined) {
  var pluginName = "Select2Rocks";

  $.fn.Select2RocksBackends = {
    'default': {
      ajax: {
        dataType: 'json',
        data: function (term, page) {
          return {q: term};
        },
        results: function (data, page) {
          return {results: data};
        }
      },
      initSelection: function(element, callback) {
        var data = [];

        $(element).data('text').split(',').forEach(function(item) {
          item = item.split(':');
          data.push({id: item[0], text: item[1]});
        });
        // Remove the list if there's only one element (won't change anything
        // in case of multiple select, but will break single select)
        if (data.length == 1) {
          data = data[0];
        }
        callback(data);
      },
      formatResult: function(item) {
        return item.text;
      },
      formatSelection: function(item) {
        return item.text;
      }
    }
  };

  function Plugin(element, options) {
    this.element = element;
    // User can select a backend by its name
    var backend;

    if ('backend' in options) {
      backend = options['backend'];
      delete options['backend'];
    } else {
      backend = 'default';
    }
    this.settings = $.extend(true, {}, $.fn.Select2RocksBackends[backend], options);
    this.settings['ajax']['url'] = this.settings.url;
    if ('queryKey' in this.settings) {
      var queryKey = this.settings.queryKey;
      this.settings['ajax']['data'] = function(term, page) {
        // Dynamic query key (eg. 'id__startswith')
        var query = {};
        query[queryKey] = term;
        return query;
      };
    }
    this._name = pluginName;
    this.init();
  }

  Plugin.prototype = {
    init: function () {
      $(this.element).select2(this.settings);
    }
  };

  $.fn[pluginName] = function (options) {
    return this.each(function() {
      if (!$.data(this, "plugin_" + pluginName)) {
	$.data(this, "plugin_" + pluginName, new Plugin(this, options));
      }
    });
  };

})(jQuery, window, document);
