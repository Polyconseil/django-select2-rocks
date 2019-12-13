/**
 * Extend list of Select2 backends.
 *
 */
(function ($) {
    "use strict";

    $.extend(true, $.fn.Select2RocksBackends, {
      restframework: {
        ajax: {
          dataType: 'json',
          data: function (term, page) {
            return {search: term};
          },
          results: function (data, page) {
            return {results: data};
          }
        },
        formatResult: function(item) {
          return item.name;
        },
        formatSelection: function(item) {
          // Handle restored form
          if (item.restored) {
            return item.text;
          } else {
            return item.name;
          }
        }
      }
    });
})(jQuery);
